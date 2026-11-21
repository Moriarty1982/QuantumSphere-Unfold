"""Bounded execution of a declared binary tape machine."""

from scripts.qsc_audit import tensor_grammar_check as tensor


def bounded_integer(value, lower, upper, label):
    if type(value) is not int or not lower <= value <= upper:
        raise tensor.InputError(f"{label} must be an integer in [{lower}, {upper}]")


def run(program, initial, args):
    tensor._keys(program, {"states", "halt", "rules"})
    tensor._strings(program["states"])
    states = set(program["states"])
    halt = program["halt"]
    tensor._text(halt)
    if halt not in states or len(states) > 64:
        raise tensor.InputError("Expected at most 64 declared states including the halt state")
    if not isinstance(program["rules"], list) or len(program["rules"]) > 128:
        raise tensor.InputError("Expected a list of at most 128 tape rules")
    rules = {}
    for rule in program["rules"]:
        tensor._keys(rule, {"state", "read", "write", "move", "next"})
        for field in ("state", "next"):
            tensor._text(rule[field])
            if rule[field] not in states:
                raise tensor.InputError(f"Undeclared state in rule field {field}")
        bounded_integer(rule["read"], 0, 1, "Read bit")
        bounded_integer(rule["write"], 0, 1, "Write bit")
        bounded_integer(rule["move"], -1, 1, "Head movement")
        key = rule["state"], rule["read"]
        if key in rules or rule["state"] == halt:
            raise tensor.InputError("Duplicate rule or outgoing rule from the halt state")
        rules[key] = rule

    bounded_integer(args["max_steps"], 0, 1024, "max_steps")
    bounded_integer(args["max_cells"], 1, 1024, "max_cells")
    if args["mode"] not in ("fixed", "grow") or type(args["trace"]) is not bool:
        raise tensor.InputError("Expected mode fixed/grow and a Boolean trace flag")
    tensor._keys(initial, {"tape", "head", "state"})
    tape, head, state = initial["tape"], initial["head"], initial["state"]
    if (not isinstance(tape, list) or not 1 <= len(tape) <= args["max_cells"]
            or any(type(bit) is not int or bit not in (0, 1) for bit in tape)):
        raise tensor.InputError("Expected a nonempty binary tape within max_cells")
    bounded_integer(head, 0, len(tape) - 1, "Initial head address")
    tensor._text(state)
    if state not in states:
        raise tensor.InputError("Initial state must be declared in the program")
    tape = tape.copy()

    def snapshot(status):
        return {"tape": tape.copy(), "head": head, "state": state, "status": status}

    status = "halted" if state == halt else "running"
    trace = [snapshot(status)] if args["trace"] else None
    stop = status
    steps = 0
    while status == "running" and steps < args["max_steps"]:
        rule = rules.get((state, tape[head]))
        if rule is None:
            status = "stuck"
        else:
            target = head + rule["move"]
            if target < 0 or (target == len(tape) and args["mode"] == "fixed"):
                status = "boundary"
            elif target == args["max_cells"]:
                stop = "cell_limit"
                break
            else:
                tape[head] = rule["write"]
                if target == len(tape):
                    tape.append(0)
                head, state = target, rule["next"]
                status = "halted" if state == halt else "running"
        steps += 1
        if trace is not None:
            trace.append(snapshot(status))
        stop = status

    result = {
        "mode": args["mode"], "steps": steps,
        "stop": "step_limit" if stop == "running" else stop,
        "final": snapshot(status),
    }
    if trace is not None:
        result["trace"] = trace
    return result
