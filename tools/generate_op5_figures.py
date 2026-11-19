"""Rebuild the historical Julia panels and the current OP5 model illustration."""
import argparse
from io import BytesIO
from pathlib import Path
import re

import numpy as np
from PIL import Image
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


BLUE = '#126082'
ORANGE = '#ab461e'
INK = '#182c3b'
MUTED = '#435565'
GRID = '#dce4eb'
JULIA_NAMES = ('gamma0', 'delta_beta', 'delta_theta', 'delta_mu')
APPENDIX = ('sources/historical/01_historical_core_snapshot/'
            '05_appendices_and_computational_completeness.tex')


def advance(u, v, c):
    # Homogeneous coordinates keep the poles and infinity in the iteration.
    x = np.conj(v)**2
    y = np.conj(u)**2 + np.conj(c)*x
    scale = np.maximum(abs(x), abs(y))
    return x/scale, y/scale


def julia_panel(gamma, pixels=432):
    c = complex(-1, gamma)
    u, v = 0j, 1+0j
    for _ in range(300):
        u, v = advance(u, v, c)
    cycle = []
    for _ in range(3):
        cycle.append((u, v))
        u, v = advance(u, v, c)
    # Every panel uses the same window, capped iteration budget and threshold.
    axis = np.linspace(-1.8, 1.8, pixels)
    u = axis[None, :] + 1j*axis[::-1, None]
    v = np.ones_like(u)
    count = np.full(u.shape, 120, dtype=np.uint8)
    for n in range(120):
        distance = np.minimum.reduce([
            abs(u*b-v*a) / np.sqrt((abs(u)**2+abs(v)**2)*(abs(a)**2+abs(b)**2))
            for a, b in cycle
        ])
        count[(distance < 1e-5) & (count == 120)] = n
        u, v = advance(u, v, c)
    assert np.isfinite(u).all() and (count < 120).any()
    weights = np.sqrt(np.minimum(count.astype(float)/36, 1))[..., None]
    light = np.array([249, 251, 244])
    dark = np.array([26, 54, 91])
    rgb = np.uint8(light + weights*(dark-light))
    # Use indexed palettes for compact archival panels and identical rendering.
    image = Image.fromarray(rgb).quantize(colors=64)
    return image


def label(pdf, x, y, value, size=10, bold=False):
    pdf.setFillColor(HexColor(INK))
    pdf.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
    pdf.drawString(x, y, value)


def polyline(pdf, points, color, dash=None, width=1.5):
    pdf.setStrokeColor(HexColor(color))
    pdf.setLineWidth(width)
    pdf.setDash(dash or [])
    path = pdf.beginPath()
    path.moveTo(*points[0])
    for point in points[1:]:
        path.lineTo(*point)
    pdf.drawPath(path)
    pdf.setDash([])


def julia_figures(repo):
    import PIL.ImageDraw
    source = (repo / APPENDIX).read_text(encoding='utf-8-sig')
    caption = next(line for line in source.splitlines() if 'Diagnostic M\\"obius-reflected quadratic probe render' in line)
    scales = re.findall(r'\\approx\s*([0-9.]+)\\times\s*10\^\{(-[0-9]+)\}', caption)
    values = [float(m)*10**int(e) for m, e in scales]
    if len(values) != 3 or not np.allclose(values, [7.50e-5, 1.79e-4, 3.38e-4], rtol=1e-12, atol=0):
        raise ValueError('Historical caption scales differ from the documented comparison')
    store = repo / 'sources'
    titles = ['Baseline', 'Beta residual', 'Theta residual', 'Mu residual']
    overview = canvas.Canvas(str(store / 'julia_probe_residual_scales_v3841.pdf'),
                             pagesize=(490, 480), invariant=1, pageCompression=1)
    fallback = Image.new('RGB', (940, 984), 'white')
    fallback_draw = PIL.ImageDraw.Draw(fallback)
    from PIL import ImageFont
    fallback_font = ImageFont.load_default(size=22)
    for index, (name, title, gamma) in enumerate(zip(JULIA_NAMES, titles, [0, *values])):
        image = julia_panel(gamma)
        x, y = 22 + 238*(index % 2), 244 - 216*(index // 2)
        encoded = BytesIO()
        image.save(encoded, format='PNG', optimize=True)
        overview.drawImage(ImageReader(encoded), x, y, 188, 188)
        overview.setStrokeColor(HexColor(ORANGE))
        overview.setLineWidth(0.6)
        overview.setDash([3, 2])
        overview.circle(x + 94, y + 94, 188/3.6, stroke=1, fill=0)
        overview.setDash([])
        label(overview, x, y+196, f'{title}  |  gamma = {gamma:.3g}', 10, True)
        singular = image.convert('RGB')
        draw = PIL.ImageDraw.Draw(singular)
        center, radius = singular.width/2, singular.width/3.6
        draw.ellipse((center-radius, center-radius, center+radius, center+radius),
                     outline=ORANGE, width=2)
        singular.quantize(colors=80).save(store / f'{name}_julia_probe_v3841.png', optimize=True)
        left, top = 24 + 460*(index % 2), 42 + 462*(index // 2)
        fallback.paste(singular, (left, top))
        fallback_draw.text((left, top-29), f'{title}  |  gamma = {gamma:.3g}', font=fallback_font, fill=INK)
    label(overview, 22, 10,
          'Light: early capture by the selected cycle. Dark: later or no capture within 120 steps.', 9)
    overview.save()
    fallback_draw.text((24, 947), 'Light: early cycle capture. Dark: later or no capture within 120 steps.',
                      font=fallback_font, fill=INK)
    fallback.quantize(colors=100).save(store / 'julia_probe_residual_scales_v3841.png', optimize=True)


def model_figure(repo):
    dst = repo / 'sources/research/figures/op5_geometry_controls.pdf'
    dst.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(dst), pagesize=(520, 232), invariant=1, pageCompression=1)
    label(pdf, 20, 210, 'A  Bifocal contours at fixed major vertex', 12, True)
    label(pdf, 273, 210, 'B  Yukawa response near coincident foci', 12, True)
    w = 0.35
    theta = np.linspace(0, 2*np.pi, 241)
    ellipse = np.column_stack((np.cos(theta), np.sqrt(1-w*w)*np.sin(theta)))
    cos = np.cos(theta)
    lo, hi = np.full_like(cos, w), np.full_like(cos, 1.1)
    level = 2/(1-w*w)
    for _ in range(56):
        r = (lo+hi)/2
        far = np.sqrt(r*r+w*w+2*r*w*cos)
        near = np.sqrt(r*r+w*w-2*r*w*cos)
        high_signal = 1/far + 1/near > level
        lo = np.where(high_signal, r, lo)
        hi = np.where(high_signal, hi, r)
    r = (lo+hi)/2
    assert np.max(abs(1/np.sqrt(r*r+w*w+2*r*w*cos)
                      + 1/np.sqrt(r*r+w*w-2*r*w*cos)-level)) < 1e-12
    polyline(pdf, [(36, 121), (218, 121)], GRID, width=0.55)
    polyline(pdf, [(127, 37), (127, 200)], GRID, width=0.55)
    polyline(pdf, [(127+80*x, 121+80*y) for x, y in ellipse], BLUE)
    polyline(pdf, [(127+80*rr*np.cos(t), 121+80*rr*np.sin(t)) for rr,t in zip(r,theta)],
             ORANGE, [4, 2])
    for x in [127-80*w, 127+80*w]:
        pdf.setFillColor(HexColor(INK))
        pdf.circle(x, 121, 2.7, stroke=0, fill=1)
    label(pdf, 31, 22, 'Distance sum', 9)
    polyline(pdf, [(17, 26), (29, 26)], BLUE)
    label(pdf, 133, 22, 'Coulomb signal sum', 9)
    polyline(pdf, [(117, 26), (129, 26)], ORANGE, [4, 2])
    left, right, bottom, top = 311, 500, 61, 189
    sx = lambda x: left+(right-left)*x/4
    sy = lambda y: bottom+(top-bottom)*(y-1)/5.5
    for y in [1, 2, 3, 4, 5, 6]:
        polyline(pdf, [(left,sy(y)), (right,sy(y))], GRID, width=0.55)
        label(pdf, left-16, sy(y)-3, str(y), 9)
    polyline(pdf, [(left,bottom), (left,top)], MUTED, width=0.65)
    for x in range(5):
        label(pdf, sx(x)-2, bottom-13, str(x), 9)
    polyline(pdf, [(sx(x),sy(x+2+1/(1+x))) for x in np.linspace(0,4,121)],
             ORANGE, [4, 2])
    polyline(pdf, [(left,sy(1)), (right,sy(1))], BLUE)
    label(pdf, 377, 31, 'Screening scale (mu a)', 9)
    label(pdf, 311, 193, 'Relative leading inward shift', 9)
    label(pdf, 329, 15, 'Distance-monitor value = 1', 9)
    pdf.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path('.'))
    args = parser.parse_args()
    julia_figures(args.repo)
    model_figure(args.repo)
