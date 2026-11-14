"""Traegt CT-001 und CT-002 in das Gegenterm-Register (Schema v7) ein und prueft Guard-Weitergabe und Blindheit fuer H102.

Reproduzierbar: legt eine eigene Datenbank an (Standard: build/ct_register_2026_11_14.sqlite3 relativ zum Repo),
registriert
  CT-001  Phaseneinheit des Lepton-Flusses (kappa*s, diskrete Auswahl unter drei Messweisen, Scan mit 154 Versuchen),
  CT-002  Kopplung des Flusses an eine Horizont-Punktierung (Zahl der Querungen, Auswahl unter vier Dauern),
die Aussage H102 (Vorab-Notiz) mit depends-on-counterterm-Kanten, den Uebergang CT-001 -> partially_constrained
(Schritte 1-3) und schreibt einen JSON-Bericht.
Aufruf (aus dem Repo-Wurzelordner):
  python notes/research/counterterms/register_ct001_ct002_2026_11_14.py [--db PFAD] [--out PFAD]
"""
import argparse
import hashlib
import json
from pathlib import Path

from qam.store.counterterms import (check_blindness, read_lifecycle, register_scheme, register_transition,
                                    resolve_dependencies)
from qam.store.registry import register, register_link
from qam.tools.store_db import initialize

FRAME = 'matter-frame-M'
HERE = Path('notes/research/counterterms')
DRAFT = HERE / 'CT-001_gamma_halbe_einheit_entwurf.md'
STEP1 = Path('notes/research/ct001_shrink_2026_11_14_out.txt')
SCAN = Path('notes/research/op3_flux_two_thirds_2026_11_13.md')
STEP2 = Path('notes/research/ct001_sector_reading_2026_11_14_out.txt')
I1 = Path('notes/research/op3_i1_string_bridge_2026_11_14.md')
H102 = Path('notes/research/predictions/Vorab_Notiz_H102_Tau_Masse_aus_gamma.md')

PDG = [
    {'label': 'm_e', 'source': 'PDG', 'version': '2024', 'value': '0.51099895 MeV'},
    {'label': 'm_mu', 'source': 'PDG', 'version': '2024', 'value': '105.6583755 MeV'},
    {'label': 'm_tau', 'source': 'PDG', 'version': '2024', 'value': '1776.93 +- 0.09 MeV'},
]
DOMAIN = {'variable': 'j', 'interval': ['1/2', '3/2'], 'samples': ['1/2', '1', '3/2'],
          'description': 'Spin der Punktierung; die Sektorlesart ist fuer alle j gleich'}


def provenance(repo, path, locator):
    data = (repo / path).read_bytes()
    return {'path': path.as_posix(), 'sha256': hashlib.sha256(data).hexdigest(),
            'revision': '2026-11-14', 'locator': locator}


def ct001(repo):
    return {'object_id': 'CT-001', 'frame': FRAME, 'status': 'conditional',
            'source': provenance(repo, SCAN, 'Scan-Treffer Delta Phi = gamma_BI/2, Nachtrag Holonomie-Fluss-Paarung'),
            'payload': {
                'title': 'CT-001 Phaseneinheit des Lepton-Flusses Delta Phi = kappa s gamma_M',
                'target_sector': 'Lepton-Fluss (Koide-Phase), Qubit-Oktant zu geladenen Leptonen',
                'operator_basis': {'kind': 'readout', 'frame': FRAME,
                                   'expression': 'Delta Phi = pi/4 - 3 theta_e (Fluss vom Qubit-Oktanten zu den geladenen Leptonen)'},
                'compensation_function': {
                    'symbolic': r'\delta_1 = \kappa s \cdot \gamma_M, \quad \kappa s = u',
                    'parameters': {'u': {'role': 'discrete_choice',
                                         'options': ['A/r^2 (Sektor relativ zum eigenen Kreis) = 1/2',
                                                     'A/(8 pi G hbar) mit sqrt(j(j+1)) = sqrt3/2',
                                                     'A/(G hbar) mit sqrt(j(j+1)) (r10) = 4 pi sqrt3'],
                                         'value': 'A/r^2 (Sektor relativ zum eigenen Kreis) = 1/2'}},
                    'form': None,
                },
                'reference_scale': 'Frame M, Zaehlregel gamma_M = 0.237533 (alle Spins, Gewicht 2)',
                'matching_condition': 'pi/4 - 3 theta_e = u gamma_M mit theta_e aus m_e, m_mu, m_tau',
                'rg_flow': None,
                'validity_domain': DOMAIN,
                'magnitude_convention': 'signed',
                'replacement_tolerance': '1/10000',
                'open_guards': [
                    {'title': 'GUARD-CT001-SEKTORNORM',
                     'obligation': 'Phase = normierte Sektorflaeche A/r^2 ist Lesart (wie Omega = A/R^2), nicht hergeleitet'},
                    {'title': 'GUARD-CT001-KONVENTION-R10',
                     'obligation': 'r10 misst dieselbe Flaeche in G hbar (43,5-fach); welche Messweise wofuer gilt, ist offen'},
                    {'title': 'GUARD-CT001-NACHTRAEGLICH',
                     'obligation': 'Scan-Treffer mit bekanntem m_tau (154 Versuche, 0,34 zufaellig erwartet)'},
                ],
                'assumptions': ['Delta Phi ist ein aeusserer Fluss (Qubit-Tripel selbst gibt Omega/2 = pi/4 bis 1e-5)',
                                'gamma_M aus der Zaehlregel des Materie-Frames (r09/r10)'],
                'scope': 'Lokal, effektiv, Lesart; keine Herleitung; OP3/OP4 offen',
                'fitted_on': {'method': 'Scan ueber Kandidatenausdruecke fuer Delta Phi', 'parameters': ['u'],
                              'data': PDG, 'uncertainty': {},
                              'scan': {'trials': 154, 'hits': 1, 'chance_expectation': '17/50'}},
                'known_tensions': [
                    {'description': 'Eigene Flaechenkonvention von r10 gibt das 43,5-fache',
                     'convention': 'r10: A = 8 pi gamma sqrt(j(j+1)) l_P^2, Einheit G hbar',
                     'delta': '85/2 * gamma_M/2', 'source': DRAFT.as_posix()},
                    {'description': 'Daten verlangen u = 0,49982 +- 0,00008 (2,3 sigma neben 1/2, wie H102)',
                     'convention': 'Massen PDG 2024', 'delta': '-0.00018', 'source': STEP1.as_posix()},
                ],
            }}


def ct002(repo):
    return {'object_id': 'CT-002', 'frame': FRAME, 'status': 'conditional',
            'source': provenance(repo, I1, 'Ergebnis 1-3, Tabelle der vier Dauern'),
            'payload': {
                'title': 'CT-002 Kopplung des Lepton-Flusses an eine Horizont-Punktierung (Zahl der Querungen)',
                'target_sector': 'Kopplung Lepton-Sektor zu Horizont-Punktierung (I1, String-Bruecke)',
                'operator_basis': {'kind': 'readout', 'frame': FRAME,
                                   'expression': 'normierte Weltflaeche A_ws/l^2 = phi/2 eines am Horizont endenden Strings'},
                'compensation_function': {
                    'symbolic': r'\delta_2 = \varphi/2, \quad \varphi = n',
                    'parameters': {'n': {'role': 'discrete_choice',
                                         'options': ['halbe Querung phi = 1/2', 'eine Lichtquerung phi = 1',
                                                     'hin und zurueck phi = 2', 'thermischer Umlauf phi = 2 pi'],
                                         'value': 'eine Lichtquerung phi = 1'}},
                    'form': None,
                },
                'reference_scale': 'euklidisches Unruh-Bild r10.1, Horizont im Zentrum',
                'matching_condition': 'Delta Phi = gamma_M * A_ws/l^2',
                'rg_flow': None,
                'validity_domain': DOMAIN,
                'magnitude_convention': 'signed',
                'replacement_tolerance': '1/10000',
                'open_guards': [
                    {'title': 'GUARD-CT002-EINE-QUERUNG', 'obligation': 'Warum genau eine Querung, nicht hergeleitet'},
                    {'title': 'GUARD-CT002-FRAME-M', 'obligation': 'Warum endet der String an einer Punktierung des Frames M'},
                    {'title': 'GUARD-CT002-EUKLIDISCH', 'obligation': 'Fortsetzung euklidischer Winkel zu Rapiditaet, Phase gegen Gewicht'},
                    {'title': 'GUARD-CT002-STRINGDYNAMIK', 'obligation': 'Gerader ruhender String nur angenommen'},
                ],
                'assumptions': ['Zurueckgestellte Idee I1 (String als Bruecke), Ausloeser 4'],
                'scope': 'Lesart; keine Herleitung; OP3/OP4 offen',
                'fitted_on': {'method': 'Auswahl unter vier vorab gelisteten Dauern', 'parameters': ['n'],
                              'data': PDG, 'uncertainty': {},
                              'scan': {'trials': 4, 'hits': 1, 'chance_expectation': '1/4'}},
                'known_tensions': [
                    {'description': 'Daten verlangen phi = 0,99964 +- 0,00016 (2,3 sigma neben 1)',
                     'convention': 'Massen PDG 2024', 'delta': '-0.00036', 'source': I1.as_posix()},
                ],
            }}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', default='.')
    parser.add_argument('--db', default='build/ct_register_2026_11_14.sqlite3')
    parser.add_argument('--out', default=str(HERE / 'register_2026_11_14_report.json'))
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    db = (repo / args.db).resolve()
    if db.exists():
        raise SystemExit(f'Datenbank existiert schon, bitte neuen Pfad waehlen: {args.db}')
    db.parent.mkdir(parents=True, exist_ok=True)
    initialize(db)
    s1 = register_scheme(db, repo, ct001(repo))
    s2 = register_scheme(db, repo, ct002(repo))
    claim = register(db, repo, {
        'object_id': 'H102', 'kind': 'claim', 'frame': FRAME, 'status': 'conditional',
        'source': provenance(repo, H102, 'Vorhersage, Entscheidungskriterium'),
        'payload': {'title': 'H102 Tau-Masse aus dem Fluss pi/4 - gamma_M/2',
                    'latex': 'Φ_e = 3θ_e = π/4 − γ_M/2',
                    'assumptions': ['CT-001', 'CT-002'], 'dependencies': []}})['version_hash']
    for scheme, why in ((s1['version_hash'], 'H102 benutzt die Einheit u = 1/2 (CT-001)'),
                        (s2['version_hash'], 'H102 benutzt die Kopplung eine Querung (CT-002)')):
        register_link(db, {'source': claim, 'target': scheme, 'kind': 'depends-on-counterterm',
                           'status': 'declared', 'description': why})
    step = register_transition(db, repo, {
        'scheme': s1['version_hash'], 'previous': None, 'status': 'partially_constrained',
        'reviewer': 'Claude Opus 5.5 auf Autorenauftrag „Ja, eintragen“',
        'reason': 'Schritte 1-3: aeusserer Fluss; 1/2 als normierte Sektorflaeche fuer alle j; gamma_M als Winkel '
                  'aus Zaehlregel und Unruh-Bild. Kein Residuenbeleg (Optionen nicht rational), daher nicht structurally_matched.',
        'evidence': provenance(repo, STEP2, 'Sektorlesart, Abgleich mit der Konventionstabelle'), 'replacement': None, 'receipt': None})
    resolved = resolve_dependencies(db, claim)
    blind_old = check_blindness(db, {'statement': claim, 'tested_against': [
        {'label': 'm_tau', 'source': 'PDG', 'version': '2024'}]})
    blind_new = check_blindness(db, {'statement': claim, 'tested_against': [
        {'label': 'm_tau', 'source': 'PDG', 'version': 'naechste Ausgabe nach 2026-11-13'}]})
    report = {
        'database': args.db, 'frame': FRAME,
        'CT-001': {'version_hash': s1['version_hash'], 'guards': s1['guards'],
                   'lifecycle': read_lifecycle(db, s1['version_hash'])['status'],
                   'transition': step['transition_hash'], 'reaudit': step['reaudit']},
        'CT-002': {'version_hash': s2['version_hash'], 'guards': s2['guards'],
                   'lifecycle': read_lifecycle(db, s2['version_hash'])['status']},
        'H102': {'version_hash': claim, 'inherited_guards': resolved['inherited_guards'],
                 'counterterms': [{'status': c['status'], 'scheme': c.get('scheme', c.get('version_hash'))}
                                  for c in resolved['counterterms']]},
        'blindness_PDG_2024': {'result': blind_old['result'], 'verdict': blind_old['verdict'],
                               'findings': blind_old.get('findings')},
        'blindness_next_PDG': {'result': blind_new['result'], 'verdict': blind_new['verdict'],
                               'findings': blind_new.get('findings')},
    }
    out = repo / args.out
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items()
                                                             if kk in ('lifecycle', 'verdict', 'result')})
                      for k, v in report.items()}, indent=1, ensure_ascii=False))
    print(f'H102 erbt {len(resolved["inherited_guards"])} offene Guards; Bericht: {args.out}')


if __name__ == '__main__':
    main()
