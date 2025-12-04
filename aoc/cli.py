import argparse
import pytest
from pathlib import Path
from importlib import import_module

from .benchmark import benchmark_day
from .template import create_day


ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE_NAME = "input.txt"


def load(day: int) -> Path:
    day_str = f"day{day:02d}"
    return ROOT / day_str / INPUT_FILE_NAME


def list_days():
    print("\n")
    for d in sorted(ROOT.glob("day*/")):
        print(d.name)


def run_day(day: int):
    day_str = f"day{day:02d}"
    module = import_module(f"{day_str}.solution")
    
    if not hasattr(module, "solve"):
        raise SystemExit("f{day_str}/solution.py must define solve()")

    print(f"\nRunning {day_str}...")
    print("Answer", module.solve())

def test_day(day: int):
    day_str = f"day{day:02d}"

    args = ["--pyargs", day_str]
    exit_code = pytest.main(args)


def main():
    parser = argparse.ArgumentParser(description="Advent of Code runner")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list", help="List days")

    r = sub.add_parser("run", help="Run a specific day")
    r.add_argument("day", type=int)

    r = sub.add_parser("test", help="Test a specific day")
    r.add_argument("day", type=int)

    n = sub.add_parser("new", help="Creatge a new day module")
    n.add_argument("day", type=int)

    b = sub.add_parser("bench", help="Benchmark a day")
    b.add_argument("day", type=int)

    args = parser.parse_args()
    if args.cmd == "list":
        list_days()
    elif args.cmd == "run":
        run_day(args.day)
    elif args.cmd == "test":
        test_day(args.day)
    elif args.cmd == "new":
        create_day(args.day)
    elif args.cmd == "bench":
        benchmark_day(args.day)


if __name__ == "__main__":
    main()
