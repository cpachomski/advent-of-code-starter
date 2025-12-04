import time
from importlib import import_module


def benchmark_day(day: int, runs: int = 20):
    name = f"day{day:02d}.solution"
    module = import_module(name)

    if not hasattr(module, "solve"):
        raise (SystemExit(f"{name} must define solve()"))

    print("Benchmarking {name}...")

    start = time.perf_counter()
    for _ in range(runs):
        module.solve()
    end = time.perf_counter()

    avg = (end - start) / runs
    print(f"{runs} runs, avg {avg:.6f} sec")
