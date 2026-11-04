import QSFormal.QamFile

/-! `qamcheck FILE.qam` — check a QAM record exported by `qam.sty` with the verified checker
`QSFormal.QamFile.step`.  Exit code 0: all lines accepted; 1: a line was rejected or unreadable. -/

open QSFormal.QamFile

def main (args : List String) : IO UInt32 := do
  match args with
  | [path] =>
    let txt ← IO.FS.readFile path
    let mut st : State := {}
    let mut n := 0
    let mut count := 0
    for raw in splitChar '\n' txt.toList do
      n := n + 1
      match parseLine raw with
      | .error e =>
        IO.eprintln s!"{path}:{n}: cannot read line: {e}"
        return 1
      | .ok none => pure ()
      | .ok (some line) =>
        match step st line with
        | some st' =>
          st := st'
          count := count + 1
        | none =>
          IO.eprintln s!"{path}:{n}: rejected: {toS (trimC raw)}"
          IO.eprintln s!"  reason: {reason st line}"
          return 1
    IO.println s!"{path}: {count} lines checked, all rules hold"
    return 0
  | _ =>
    IO.eprintln "usage: qamcheck FILE.qam"
    return 2
