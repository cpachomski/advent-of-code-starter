from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent

TEMPLATE = """\
from pathlib import Path

def solve() -> int:
    path = Path(__file__).parent / "input.txt"
    # TODO: implement
    return 0

if __name__ == "__main__":
    print(solve())
"""


TEST_TEMPLATE = """\
from day{day:02d}.solution import solve

def test_solve():
    assert solve() == 0
"""


def create_day(day: int):
    folder = ROOT / f"day{day:02d}"
    if folder.exists():
        print(f"{folder} already exists.")
        return

    folder.mkdir()
    (folder / "__init.py__").write_text("")
    (folder / "input.txt").write_text("")
    (folder / "solution.py").write_text(TEMPLATE)
    (folder / "test_solution.py").write_text(TEST_TEMPLATE.format(day=day))

    print(f"Created {folder}")
