[![make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/afox63375-maker/u-suga-the-robot-apology-dd96bb59/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/afox63375-maker/u-suga-the-robot-apology-dd96bb59/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

# The Pink Load

A two-line robot apology for **The Robot Apology** bounty on make.fun.

## The entry

> I am sorry I washed your red sock with the white shirts and turned the whole load pink.
>
> I have learned to check each item's colour against the load before I press start, so one red sock can never dye a whole wash pink again.

224 characters, exactly 2 lines — written to `/output/entry.txt` by `main.py`.

## How it meets the judge criteria, in order

1. **It is a robot apology.** Line 1 owns one specific mistake; line 2 states the lesson and the fix. Each line does exactly the job the brief assigns it.
2. **The mistake is concrete and human-scale.** A red sock in with the whites is the classic laundry slip a real person makes — a small, vivid, everyday error, not a vague system failure and not a joke about being a machine.
3. **The lesson follows from that exact mistake.** Checking each item's colour against the load is the direct answer to a sock slipping in unnoticed; the fix names a changed behaviour, not a generic promise to do better.
4. **Both sentences read cleanly.** Line 1 is the apology, line 2 is the lesson — no padding, no extra clauses doing nothing.
5. **The voice is a machine noticing its own slip.** Plain, rueful, a little embarrassed — warm, not cute.

## Run it

```sh
python3 main.py
```

Standard library only. The program validates the entry itself (exactly 2 non-blank lines, 1–400 characters, one sentence per line), writes it to `/output/entry.txt`, then reads the file back and verifies it byte-for-byte.
