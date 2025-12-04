# Advent of Code 2025

Small personal workspace for solving [Advent of Code](https://adventofcode.com/) puzzles.

This repository contains per-day solution folders and a small CLI in `aoc/` to easily create, run, test, and benchmark each day's solution.

## Setup

1. Install uv: https://docs.astral.sh/uv/getting-started/installation/

## Makefile targets

The Makefile defines a few convenient targets. The Makefile uses a variable `RUN` set to `uv run` by default; if `uv` isn't available on your system you can change `RUN` to `python -m` or `python3 -m`.

- `make run d=<N>`
  - Runs the `solve()` function for the specified day.
  - Example: `make run d=1` will run `day01/solution.py` via the CLI.

- `make test d=<N>`
  - Runs tests for a specific day with pytest
  - Example: `make test d=1`

- `make new d=<N>`
  - Creates a new `dayNN` folder with template `solution.py`, `input.txt`, and `test_solution.py`.
  - Example: `make new d=3` creates `day03/` with starter files.

- `make bench d=<N>`
  - Benchmarks the `solve()` function for a day. The benchmark helper runs the solution multiple times and prints the average runtime.
  - Example: `make bench d=1`
  `