"""Traegt CT-003 (Ladungsachse e8 auf den Sedenionen) samt abhaengigen Aussagen ein und erzeugt die Platzhalter-Bilanz.

Baut eine neue Datenbank mit dem vollen Stand: CT-001, CT-002 und H102 wie in register_ct001_ct002_2026_11_14.py,
dazu
  CT-003  Ladungsachse der farbneutralen Leptonen auf C(x)S: e8 statt e7 (Q|_O = Q8 aufgegeben),
  S-N     neutrales Qubit N = ker Q_* mit psi = diag(1, omega)        (depends-on-counterterm CT-003),
  S-2T    Hurwitz-Einheiten wirken auf N als 2T                       (requires S-N),
  S-GEN   C(x)S traegt unter Q_* zwei vollstaendige Generationen      (depends-on-counterterm CT-003).
Danach Aufloesung (geerbte Guards), ein LaTeX-Export der Auswahl {H102, S-2T, S-GEN} mit Registeranhang und eine Bilanz.
Aufruf (aus dem Repo-Wurzelordner, mit PYTHONPATH=.):
  python notes/research/counterterms/register_ct003_2026_11_14.py [--db PFAD] [--out PFAD] [--export ORDNER]
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
spec = importlib.util.spec_from_file_location('ct12', HERE / 'register_ct001_ct002_2026_11_14.py')
ct12 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ct12)

FRAME_S = 'sedenion-frame'
CHARGE = Path('notes/research/op3_sedenion_charge_2026_11_13.md')
HURWITZ = Path('notes/research/op3_hurwitz_2t_neutral_qubit_2026_11_14.md')
GENERATIONS = Path('notes/research/op3_sedenion_generations_estar_2026_11_14.md')


def ct003(repo):
    return {'object_id': 'CT-003', 'frame': FRAME_S, 'status': 'conditional',
            'source': ct12.provenance(repo, CHARGE, 'Suchrichtung N1-N3, Ergebnis 1-3'),
            'payload': {
                'title': 'CT-003 Ladungsachse der farbneutralen Leptonen auf den Sedenionen (e8 statt e7)',
                'target_sector': 'Ladung auf C(x)S, farbneutraler Block span(1, e7, e8, e15)',
                'operator_basis': {'kind': 'readout', 'frame': FRAME_S,
                                   'expression': 'Q_* = P_0 (1/2 - (i/2) X) P_0 + 2/3 P_3 + 1/3 P_3bar mit X = L_e8'},
                'compensation_function': {
                    'symbolic': r'Q_\ast\vert_{\rm farbneutral} = \tfrac12 - \tfrac{i}{2} X',
                    'parameters': {'X': {'role': 'discrete_choice',
                                         'options': ['L_e7/R_e7 (Fortsetzung von Q8; nicht psi-vertraeglich)',
                                                     'L_e8 (psi-fest)', 'R_e8 (psi-fest)'],
                                         'value': 'L_e8 (psi-fest)'}},
                    'form': None,
                },
                'reference_scale': 'Sedenionen S = O + O e8 (Cayley-Dickson, r04), Farbe = Stab(e7) in g2',
                'matching_condition': '[Q, psi] = 0, [Q, su(3)_c] = 0, conj(Q) = 1 - Q, Spektrum {0, 1/3, 2/3, 1}',
                'rg_flow': None,
                'validity_domain': {'variable': 'k', 'interval': ['0', '2'], 'samples': ['0', '1', '2'],
                                    'description': 'Potenz psi^k des Generationszyklus'},
                'magnitude_convention': 'signed',
                'replacement_tolerance': '0',
                'open_guards': [
                    {'title': 'GUARD-CT003-Q8-AUFGEGEBEN',
                     'obligation': 'Q_* stimmt auf O nicht mit der Companion-Ladung Q8 ueberein; O ist nicht Q_*-invariant'},
                    {'title': 'GUARD-CT003-ZWEI-GENERATIONEN',
                     'obligation': 'Weg A traegt nur zwei Generationen (K28); psi ist kein Generationsschritt'},
                    {'title': 'GUARD-CT003-EPSILON-C',
                     'obligation': 'epsilon wirkt auf den Leptonen als Ladungskonjugation; S3 bricht zu Z3'},
                ],
                'assumptions': ['Ladung auf S im Companion nicht definiert; Fortsetzung ist eine Wahl',
                                'Rueckwaertssuche N1-N3 ohne Q|_O = Q8 (op3_sedenion_charge_2026_11_13.md)'],
                'scope': 'Lesart auf dem Sedenionen-Weg; keine Herleitung; OP3/OP4 offen',
                'fitted_on': None,
                'known_tensions': [
                    {'description': 'Q_* ungleich Q8 auf span(1, e7)', 'convention': 'Companion-Ladung k85',
                     'delta': 'neutrale Linie 1 + i e8 statt 1 + i e7', 'source': CHARGE.as_posix()},
                    {'description': 'nur zwei Neutrino-Flavours', 'convention': 'K28 Weg A',
                     'delta': 'dritte Generation fehlt', 'source': GENERATIONS.as_posix()},
                ],
            }}


def statement(db, repo, object_id, path, latex, title, locator):
    return register(db, repo, {
        'object_id': object_id, 'kind': 'claim', 'frame': FRAME_S, 'status': 'conditional',
        'source': ct12.provenance(repo, path, locator),
        'payload': {'title': title, 'latex': latex, 'assumptions': ['CT-003'], 'dependencies': []}})['version_hash']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', default='.')
    parser.add_argument('--db', default='build/ct_register_full_2026_11_14.sqlite3')
    parser.add_argument('--out', default=str(ct12.HERE / 'register_ct003_2026_11_14_report.json'))
    parser.add_argument('--export', default='build/ct_register_export_2026_11_14')
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    db = (repo / args.db).resolve()
    if db.exists() or (repo / args.export).exists():
        raise SystemExit('Datenbank oder Exportordner existiert schon; bitte neue Pfade waehlen')
    db.parent.mkdir(parents=True, exist_ok=True)
    initialize(db)
    # Voller Stand: CT-001, CT-002, H102 wie im ersten Skript.
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
    # CT-003 und abhaengige Aussagen.
    s3 = register_scheme(db, repo, ct003(repo))
    n = statement(db, repo, 'S-N', CHARGE, 'ψ wirkt auf N als diag(1, ω)',
                  'Neutrales Qubit N = ker Q_* mit psi = diag(1, omega)', 'Ergebnis 4')
    t2 = statement(db, repo, 'S-2T', HURWITZ, 'Das ist die binäre Tetraedergruppe 2T',
                   'Hurwitz-Einheiten von H_n wirken auf N als 2T', 'Ergebnis 1')
    gen = statement(db, repo, 'S-GEN', GENERATIONS, 'genau **zwei vollständige Generationen**',
                    'C(x)S traegt unter Q_* zwei vollstaendige Generationen', 'Ergebnis 1')
    for source, why in ((n, 'N ist der Kern von Q_*'), (gen, 'Generationszaehlung unter Q_*')):
        register_link(db, {'source': source, 'target': s3['version_hash'], 'kind': 'depends-on-counterterm',
                           'status': 'declared', 'description': why})
    register_link(db, {'source': t2, 'target': n, 'kind': 'requires', 'status': 'declared',
                       'description': '2T wirkt auf das neutrale Qubit N'})
    resolved = {name: resolve_dependencies(db, key) for name, key in
                (('H102', h102), ('S-N', n), ('S-2T', t2), ('S-GEN', gen))}
    snapshot = create_snapshot(db, 'ct-register-full-2026-11-14')['snapshot_hash']
    selection = select_versions(db, snapshot, [h102, t2, gen])
    exported = export_selection(selection, repo / args.export)
    tex = (Path(exported['directory']) / 'paper.tex').read_text(encoding='utf-8')
    schemes = {'CT-001': s1, 'CT-002': s2, 'CT-003': s3['version_hash']}
    balance = {name: read_lifecycle(db, key)['status'] for name, key in schemes.items()}
    report = {
        'database': args.db, 'snapshot': snapshot, 'selection_hash': selection['selection_hash'],
        'CT-003': {'version_hash': s3['version_hash'], 'guards': s3['guards'], 'lifecycle': balance['CT-003']},
        'statements': {name: {'version_hash': item['version'], 'inherited_guards': len(item['inherited_guards']),
                              'counterterms': sorted(c['status'] for c in item['counterterms'])}
                       for name, item in resolved.items()},
        'balance': {'counterterms': balance, 'by_status': {status: sorted(k for k, v in balance.items() if v == status)
                                                           for status in sorted(set(balance.values()))},
                    'structurally_matched': sum(v == 'structurally_matched' for v in balance.values()),
                    'note': 'Elektron-Abstand pi/12 - theta_e = Delta Phi / 3 haengt an CT-001/CT-002, kein eigener Eintrag'},
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
