"""Contracts for declared macro and bibliography resources."""

import re


def validate_resource(payload):
    resource_type = payload.get('resource_type')
    latex = payload['latex']
    if resource_type == 'macro':
        name = payload['name']
        if not isinstance(name, str) or not re.fullmatch(r'[A-Za-z]+', name):
            raise ValueError('Macro name must consist of ASCII letters without backslash')
        pattern = r'\\newcommand\{\\' + re.escape(name) + r'\}(?:\[[0-9]\])?\{'
        head = re.match(pattern, latex)
        if head is None:
            raise ValueError('Macro must be a newcommand declaration matching its registered name')
        # Verify one complete declaration, respecting escaped braces and comments.
        depth = 1
        index = head.end()
        while index < len(latex) and depth:
            char = latex[index]
            if char == '\\':
                index += 2
                continue
            if char == '%':
                newline = latex.find('\n', index)
                if newline < 0:
                    raise ValueError('Unclosed macro body')
                index = newline + 1
                continue
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
            index += 1
        if depth or latex[index:].strip():
            raise ValueError('Macro resource must contain exactly one balanced declaration')
    elif resource_type == 'bibliography':
        key = payload['key']
        if not isinstance(key, str) or not re.fullmatch(r'[A-Za-z0-9:._-]+', key):
            raise ValueError('Invalid bibliography key')
        if not latex.startswith(r'\bibitem{' + key + '}') or latex.count(r'\bibitem') != 1:
            raise ValueError('Bibliography resource must contain one matching bibitem')
    else:
        raise ValueError('Supported resource types: macro, bibliography')


def resource_groups(objects):
    packages = set()
    macros = {}
    references = {}
    for obj in objects:
        if obj['kind'] != 'latex-resource':
            continue
        payload = obj['payload']
        if 'package' in payload:
            if payload['package'] not in {'amsthm', 'amssymb', 'array'}:
                raise ValueError('Unsupported package resource')
            packages.add(payload['package'])
            continue
        validate_resource(payload)
        if payload['resource_type'] == 'macro':
            target, name = macros, payload['name']
        else:
            target, name = references, payload['key']
        if name in target and target[name]['version_hash'] != obj['version_hash']:
            raise ValueError(f'Conflicting resource versions for {name}')
        target[name] = obj
    return packages, list(macros.values()), list(references.values())
