"""Charm the Commuter: Forecast a City That Isn't — make.fun entry.

Decision record (24 Nov 2026):

The gate is one line of weather, 1-140 characters, for a city that does not
exist. The judge is a bored commuter reading the forecast on a phone at a
rainy bus stop, weighing in order: (1) reads as a one-line forecast for a
named invented city, weather the whole point; (2) makes the commuter smile
on one reading; (3) keeps the register of a real broadcast forecast, bent
rather than dropped; (4) one concrete detail of the city's weather or life;
(5) every word earning its place. Quirkiness for its own sake does not count.

Candidates weighed:

A. Zorbia (CHOSEN): "Zorbia: scattered sunshine and one very personal
   thunderstorm following you to work. Umbrella optional, dignity unlikely."
   (121 chars) The weather is the whole point — a thunderstorm, only a
   personal one, so criterion 1 holds while the joke lands. "Scattered
   sunshine" and "Umbrella optional" keep the broadcast register; the storm
   following you to work is the commuter's-eye detail; "dignity unlikely"
   is the punch, in the last two words. Every clause does work.

B. Drizzleford: "Drizzleford: overnight rain, morning fog, then a 9 a.m.
   hail of unread emails. Buses on time, spirits delayed." (110 chars)
   The strongest broadcast rhythm of the four — "overnight rain, morning
   fog" reads straight off the radio — and "spirits delayed" is a sweet
   punch. It loses because the weather stops being weather halfway through:
   a hail of emails is an office joke wearing a forecast's coat, so it
   falls at criterion 1, the first and most important.

C. Wobbleton: "Wobbleton: heavy rain, and a strong chance your umbrella
   will betray you before the 8:15 bus. Pack patience." (114 chars)
   A real commuter grievance and a clear punch ("betray you"), but the
   joke is familiar — umbrellas failing is the first joke every forecast
   reaches for — so it loses on surprise at criterion 2, and "Pack
   patience" is advice, not a turn of phrase.

D. Mizzlewick: "Mizzlewick: 100% chance of rain, 0% chance the bus
   shelter fits everyone. Queue early, get wet together." (104 chars)
   The bus-shelter detail is the most commuter-true image of the four,
   but the ending is warm rather than funny; it smiles politely where
   Zorbia's "dignity unlikely" actually makes the commuter laugh, and it
   spends its last words on logistics instead of a punch.

Writing passes on the chosen line:

Pass 1: "Zorbia: scattered sunshine, with one thunderstorm following you
to work. Umbrella optional, dignity unlikely." The skeleton was right —
forecast opening, storm, commuter, punch — but "one thunderstorm" was
flat: any city can have a thunderstorm, and nothing made it Zorbia's.

Pass 2: replaced "with one thunderstorm" with "and one very personal
thunderstorm". "Very personal" makes the storm single the commuter out,
which is the whole joke: the weather is not bad in general, it is out to
get you specifically. The comma splice went with it, so the line now
reads in one broadcast breath: forecast, storm, commute, punch.

Final line (121 characters, one line, inside the 1-140 gate):

    Zorbia: scattered sunshine and one very personal thunderstorm
    following you to work. Umbrella optional, dignity unlikely.
"""

import os

LINE = (
    "Zorbia: scattered sunshine and one very personal thunderstorm "
    "following you to work. Umbrella optional, dignity unlikely."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    # Read-back verification: the file must hold exactly the intended line.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    assert written == LINE, f"entry.txt mismatch: {written!r} != {LINE!r}"
    assert 1 <= len(written) <= 140, f"gate failed: {len(written)} chars"
    print(f"chars: {len(written)}")


if __name__ == "__main__":
    main()
