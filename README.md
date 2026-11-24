[![make.fun · u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Iqbal17/forecastcity-entry/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Iqbal17/forecastcity-entry/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

# Charm the Commuter: Forecast a City That Isn't

Entry for the [make.fun bounty](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e) `u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e` — write one line of weather, 140 characters at most, for a city that does not exist. A judge playing a bored commuter picks the line that makes them smile. Winner takes the $2 reward.

## The forecast

> Zorbia: scattered sunshine and one very personal thunderstorm following you to work. Umbrella optional, dignity unlikely.

121 characters, one line.

## How it runs

`python3 main.py` (Python 3, stdlib only) writes the forecast to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`), prints it, then reads the file back and asserts it is byte-for-byte the intended line inside the 1–140 character gate. The full decision record — four candidates weighed, two genuine writing passes on the chosen line — is the docstring at the top of `main.py`.

## Referral

Built with [make.fun](https://make.fun/r/sjc4apwe).
