"""Traegt CT-004 (Zaehlregel je Frame als Stringendpunkte, OP1 mit I1) zum vollen Stand CT-001 bis CT-003 ein.

Baut eine neue Datenbank: CT-001, CT-002, H102, CT-003 mit S-N, S-2T, S-GEN wie in register_ct003_2026_11_14.py, dazu
  CT-004   Tachyon-Frame zaehlt nur Endpunkte einzelner offener Strings (j = 1/2, Gewicht 2), Materie-Frame alle Kanten,
  S-COUNT  Zaehlregel je Frame: M alle Spins (gamma_M), T nur j = 1/2 (gamma_T)      (depends-on-counterterm CT-004).
Danach Aufloesung (geerbte Guards), LaTeX-Export der Auswahl {H102, S-2T, S-GEN, S-COUNT} mit Registeranhang und Bilanz.
Aufruf (aus dem Repo-Wurzelordner, mit PYTHONPATH=.):
  python notes/research/counterterms/register_ct004_2026_11_15.py [--db PFAD] [--out PFAD] [--export ORDNER]
"""
import argparse
import importlib.util
import json
from pathlib import Path

from qam.store.counterterms import read_lifecycle, register_scheme, register_transition, resolve_dependencies
from qam.store.latex_export import export_selection
from qam.store.registry import register, register_link
from qam.store.selection import select_versions
from qam.store.snapshots import create_snapshot
from qam.tools.store_db import initialize

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('ct3', HERE / 'register_ct003_2026_11_14.py')
ct3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ct3)
ct12 = ct3.ct12

FRAME_T = 'tachyon-frame'
NOTE = Path('notes/research/op1_i1_string_endpoints_2026_11_15/README.md')
H98 = Path('notes/research/predictions/Ergebnis_H98_Zaehlregel_Sonderstellung.md')
H15 = Path('notes/research/v4_9_0_r01_r16/llm/Vorab_Notiz_H15_W_Masse_gamma_L.md')
H46 = Path('notes/research/predictions/Vorab_Notiz_H46_theta23_bei_eps_eta.md')
H96 = Path('notes/research/predictions/Vorab_Notiz_H96_Omega_M_beta2.md')
WINDOWS = [
    {'label': 'beta_sym (Leptonfenster)', 'source': 'Companion v4.9.0-r61.1(e)', 'version': '2026-11', 'value': '[0.545, 0.570]'},
    {'label': 'm_W', 'source': 'PDG', 'version': '2025', 'value': 'Fenster 2 sigma'},
    {'label': 'Omega_M', 'source': 'DESI DR2', 'version': '2025', 'value': 'Fenster 2 sigma'},
]


def ct004(repo):
    return {'object_id': 'CT-004', 'frame': FRAME_T, 'status': 'conditional',
            'source': ct12.provenance(repo, NOTE, 'Kandidat C3, Befund'),
            'payload': {
                'title': 'CT-004 Zaehlregel je Frame als Stringendpunkte: T zaehlt nur Endpunkte einzelner offener Strings',
                'target_sector': 'Horizontzaehlung je Frame (OP1); Tachyon-Frame als String-Sektor (T11)',
                'operator_basis': {'kind': 'readout', 'frame': FRAME_T,
                                   'expression': 'g_T(j) = 2 delta_{j,1/2} (Endpunkt in der Fundamentaldarstellung), '
                                                 'g_M(j) = 2 (Saettigung m = +-j)'},
                'compensation_function': {
                    'symbolic': r'\sum_j g_X(j)\,e^{-2\pi\gamma_X\sqrt{j(j+1)}}=1',
                    'parameters': {'R_T': {'role': 'discrete_choice',
                                           'options': ['alle Spins', 'halbzahlige Spins (Kramers)',
                                                       'nur j = 1/2 (Stringendpunkte)', 'nur j = 1'],
                                           'value': 'nur j = 1/2 (Stringendpunkte)'}},
                    'form': None,
                },
                'reference_scale': 'Flaechenspektrum a(j) = sqrt(j(j+1)) in Einheiten 8 pi gamma l_P^2',
                'matching_condition': 'gamma_L = gamma_M/gamma_T = 1.8647 (H98: einziges Paar in allen drei Fenstern)',
                'rg_flow': None,
                'validity_domain': ct12.DOMAIN,
                'magnitude_convention': 'signed',
                'replacement_tolerance': '0',
                'open_guards': [
                    {'title': 'GUARD-CT004-T-GLEICH-STRING',
                     'obligation': 'Tachyon-Frame = String-Sektor ist Lesart (T11, Aequivalenz seit r04 offen)'},
                    {'title': 'GUARD-CT004-CHAN-PATON',
                     'obligation': 'Endpunkte in der Fundamentaldarstellung von SU(2); Horizont als Brane nur Analogie'},
                    {'title': 'GUARD-CT004-STATISTIK',
                     'obligation': 'T11 nennt den String-Sektor bosonisch, gezaehlt wird Spin 1/2'},
                    {'title': 'GUARD-CT004-SPEKTRUM',
                     'obligation': 'Sonderstellung des Paares haengt am festen Flaechenspektrum (H104)'},
                ],
                'assumptions': ['Zurueckgestellte Idee I1 (mehrere LQG-Systeme, String als Bruecke), Ausloeser 3',
                                'Chan-Paton-Faktor offener Strings aus Vorwissen, nicht nachgeprueft'],
                'scope': 'Lesart fuer OP1; keine Herleitung; bindet CT-002 (eine Querung) und den einen Kern aus OP3',
                'fitted_on': {'method': 'Auswahl im festgelegten Regelraum von H98 (36 Paare)', 'parameters': ['R_T'],
                              'data': WINDOWS, 'uncertainty': {},
                              'scan': {'trials': 36, 'hits': 1, 'chance_expectation': '2/25'}},
                'known_tensions': [
                    {'description': 'Kramers-Regel ueber die Umkehrwalze waehlt alle halbzahligen Spins',
                     'convention': 'Theta^2 = (-1)^(2j)', 'delta': 'gamma_L = 1.2559, beta = 0.3368',
                     'source': NOTE.as_posix()},
                    {'description': 'Freies Flaechenspektrum laesst ein zweites Paar zu', 'convention': 'H104',
                     'delta': 'gamma_L = 1.864824 gegen 1.864700', 'source': H98.as_posix()},
                    {'description': 'gamma_string ist nur dem Namen nach eine Stringkopplung; T11 ordnet String- und '
                                    'LQG-Sektor nach J-Paritaet, nicht nach Frame',
                     'convention': 'v4.8.0-r03 (F11): ABCK-Wert, kein Stringtheorie-Wert; DL: j = 1/2 aus einer '
                                   'unechten Nebenbedingung',
                     'delta': 'Guard T-GLEICH-STRING ohne Stuetze im Bestand; die Lesart haengt allein an I1',
                     'source': 'sources/research/parts/v480-post-release-layers.tex'},
                ],
            }}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', default='.')
    parser.add_argument('--db', default='build/ct_register_full_2026_11_15.sqlite3')
    parser.add_argument('--out', default=str(HERE / 'register_ct004_2026_11_15_report.json'))
    parser.add_argument('--export', default='build/ct_register_export_2026_11_15')
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    db = (repo / args.db).resolve()
    if db.exists() or (repo / args.export).exists():
        raise SystemExit('Datenbank oder Exportordner existiert schon; bitte neue Pfade waehlen')
    db.parent.mkdir(parents=True, exist_ok=True)
    initialize(db)
    # Voller Stand bis CT-003, wie in register_ct003_2026_11_14.py.
    s1 = register_scheme(db, repo, ct12.ct001(repo))['version_hash']
    s2 = register_scheme(db, repo, ct12.ct002(repo))['version_hash']
    h102 = register(db, repo, {
        'object_id': 'H102', 'kind': 'claim', 'frame': ct12.FRAME, 'status': 'conditional',
        'source': ct12.provenance(repo, ct12.H102, 'Vorhersage, Entscheidungskriterium'),
        'payload': {'title': 'H102 Tau-Masse aus dem Fluss pi/4 - gamma_M/2', 'latex': 'Φ_e = 3θ_e = π/4 − γ_M/2',
                    'assumptions': ['CT-001', 'CT-002'], 'dependencies': []}})['version_hash']
    for scheme in (s1, s2):
        register_link(db, {'source': h102, 'target': scheme, 'kind': 'depends-on-counterterm',
                           'status': 'declared', 'description': 'H102 benutzt den Gegenterm'})
    register_transition(db, repo, {
        'scheme': s1, 'previous': None, 'status': 'partially_constrained',
        'reviewer': 'Claude Opus 5.5 auf Autorenauftrag „Ja, eintragen“',
        'reason': 'Schritte 1-3: aeusserer Fluss; 1/2 als normierte Sektorflaeche fuer alle j; gamma_M als Winkel '
                  'aus Zaehlregel und Unruh-Bild. Kein Residuenbeleg (Optionen nicht rational), daher nicht structurally_matched.',
        'evidence': ct12.provenance(repo, ct12.STEP2, 'Sektorlesart, Abgleich mit der Konventionstabelle'),
        'replacement': None, 'receipt': None})
    s3 = register_scheme(db, repo, ct3.ct003(repo))['version_hash']
    n = ct3.statement(db, repo, 'S-N', ct3.CHARGE, 'ψ wirkt auf N als diag(1, ω)',
                      'Neutrales Qubit N = ker Q_* mit psi = diag(1, omega)', 'Ergebnis 4')
    t2 = ct3.statement(db, repo, 'S-2T', ct3.HURWITZ, 'Das ist die binäre Tetraedergruppe 2T',
                       'Hurwitz-Einheiten von H_n wirken auf N als 2T', 'Ergebnis 1')
    gen = ct3.statement(db, repo, 'S-GEN', ct3.GENERATIONS, 'genau **zwei vollständige Generationen**',
                        'C(x)S traegt unter Q_* zwei vollstaendige Generationen', 'Ergebnis 1')
    for source, why in ((n, 'N ist der Kern von Q_*'), (gen, 'Generationszaehlung unter Q_*')):
        register_link(db, {'source': source, 'target': s3, 'kind': 'depends-on-counterterm',
                           'status': 'declared', 'description': why})
    register_link(db, {'source': t2, 'target': n, 'kind': 'requires', 'status': 'declared',
                       'description': '2T wirkt auf das neutrale Qubit N'})
    # CT-004 und die abhaengige Zaehlregel.
    s4 = register_scheme(db, repo, ct004(repo))
    count = register(db, repo, {
        'object_id': 'S-COUNT', 'kind': 'claim', 'frame': FRAME_T, 'status': 'conditional',
        'source': ct12.provenance(repo, NOTE, 'Ziel und notwendige Bedingungen; Kandidat C3'),
        'payload': {'title': 'Zaehlregel je Frame: M alle Spins (gamma_M), T nur j = 1/2 (gamma_T)',
                    'latex': 'Ein Endpunkt eines einzelnen offenen Strings trägt die',
                    'assumptions': ['CT-004'], 'dependencies': []}})['version_hash']
    register_link(db, {'source': count, 'target': s4['version_hash'], 'kind': 'depends-on-counterterm',
                       'status': 'declared', 'description': 'Die Zaehlregel in T ruht auf der Stringendpunkt-Lesart'})
    # Autorenauftrag „H15/H46/H96 verknuepfen“ (15.11.): Die drei offenen Vorhersagen ruhen auf der Zaehlregel je Frame
    # (v4.10.0-r08.3) und erben ueber S-COUNT die Guards von CT-004.
    predictions = {}
    for object_id, path, latex, title in (
            ('H15', H15, 'm_W = m_Z · γ_L / √(1 + γ_L²)', 'H15 W-Masse aus gamma_L = gamma_BI/gamma_string'),
            ('H46', H46, 'sin²θ₂₃ ∈ [0.49, 0.50]', 'H46 sin^2 theta_23 in [0.49, 0.50] unter epsilon = eta'),
            ('H96', H96, 'Ω_M = β_sym² = (γ_L − 1)/(γ_L + 1)', 'H96 Omega_M = beta_sym^2')):
        key = register(db, repo, {
            'object_id': object_id, 'kind': 'claim', 'frame': ct12.FRAME, 'status': 'conditional',
            'source': ct12.provenance(repo, path, 'Hypothese bzw. Vorhersage'),
            'payload': {'title': title, 'latex': latex, 'assumptions': ['S-COUNT'], 'dependencies': []}})['version_hash']
        register_link(db, {'source': key, 'target': count, 'kind': 'requires', 'status': 'declared',
                           'description': 'gamma_L = gamma_BI/gamma_string ruht auf der Zaehlregel je Frame (r08.3)'})
        predictions[object_id] = key
    resolved = {name: resolve_dependencies(db, key) for name, key in
                (('H102', h102), ('S-N', n), ('S-2T', t2), ('S-GEN', gen), ('S-COUNT', count))
                + tuple(predictions.items())}
    snapshot = create_snapshot(db, 'ct-register-full-2026-11-15')['snapshot_hash']
    selection = select_versions(db, snapshot, [h102, t2, gen, count] + list(predictions.values()))
    exported = export_selection(selection, repo / args.export)
    tex = (Path(exported['directory']) / 'paper.tex').read_text(encoding='utf-8')
    schemes = {'CT-001': s1, 'CT-002': s2, 'CT-003': s3, 'CT-004': s4['version_hash']}
    balance = {name: read_lifecycle(db, key)['status'] for name, key in schemes.items()}
    report = {
        'database': args.db, 'snapshot': snapshot, 'selection_hash': selection['selection_hash'],
        'CT-004': {'version_hash': s4['version_hash'], 'guards': s4['guards'], 'lifecycle': balance['CT-004']},
        'statements': {name: {'version_hash': item['version'], 'inherited_guards': len(item['inherited_guards']),
                              'counterterms': sorted(c['status'] for c in item['counterterms'])}
                       for name, item in resolved.items()},
        'balance': {'counterterms': balance, 'by_status': {status: sorted(k for k, v in balance.items() if v == status)
                                                           for status in sorted(set(balance.values()))},
                    'structurally_matched': sum(v == 'structurally_matched' for v in balance.values())},
        'export': {'directory': args.export, 'manifest_hash': exported['manifest_hash'],
                   'registry_entries': tex.count('% qstore-counterterm-entry '),
                   'guard_notes': tex.count('% qstore-counterterm-note ')},
    }
    out = repo / args.out
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'balance': report['balance']['counterterms'], 'statements': report['statements'],
                      'export': report['export']}, indent=1, ensure_ascii=False))


if __name__ == '__main__':
    main()
