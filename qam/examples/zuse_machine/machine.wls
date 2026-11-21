(* Binary tape with zero-based addresses and a fixed left boundary. *)
ClearAll[ZuseStep, ZuseTrace, ZuseRunExamples];

ZuseStep[program_, configuration_, grow_: False] := Module[
  {tape = configuration["tape"], head = configuration["head"],
   state = configuration["state"], rule, nextHead, nextState},
  If[configuration["status"] =!= "running", Return[configuration]];
  rule = SelectFirst[program["rules"],
    #["state"] === state && #["read"] === tape[[head + 1]] &];
  If[MissingQ[rule], Return[Join[configuration, <|"status" -> "stuck"|>]]];
  nextHead = head + rule["move"];
  If[nextHead < 0 || (nextHead >= Length[tape] && !TrueQ[grow]),
    Return[Join[configuration, <|"status" -> "boundary"|>]]];
  tape[[head + 1]] = rule["write"];
  If[nextHead == Length[tape], tape = Append[tape, 0]];
  nextState = rule["next"];
  <|"tape" -> tape, "head" -> nextHead, "state" -> nextState,
    "status" -> If[nextState === program["halt"], "halted", "running"]|>
];

ZuseTrace[program_, example_, grow_: False] := Module[
  {current, trace, steps},
  current = Join[KeyTake[example, {"tape", "head", "state"}],
    <|"status" -> If[example["state"] === program["halt"], "halted", "running"]|>];
  (* Reap after recording the initial configuration and each executed step. *)
  trace = Reap[
    Sow[current];
    Do[
      If[current["status"] =!= "running", Break[]];
      current = ZuseStep[program, current, grow];
      Sow[current],
      {steps, example["steps"]}
    ]
  ][[2, 1]];
  trace
];

ZuseRunExamples[program_] := Do[
  Print[ExportString[
    <|"example" -> example["name"], "mode" -> If[grow, "grow", "fixed"],
      "trace" -> ZuseTrace[program, example, grow]|>,
    "RawJSON", "Compact" -> True]],
  {grow, {False, True}}, {example, program["examples"]}
];

If[ListQ[$ScriptCommandLine] && Length[$ScriptCommandLine] > 0 &&
    FileNameTake[First[$ScriptCommandLine]] === "machine.wls",
  ZuseRunExamples[Import[
    If[Length[$ScriptCommandLine] > 1, $ScriptCommandLine[[2]],
      FileNameJoin[{DirectoryName[$InputFileName], "machine.json"}]],
    "RawJSON"]]
];
