.PHONY: run test
RUN = uv run 


list:
	$(RUN) -m aoc.cli list

run:
	$(RUN) -m aoc.cli run $(d)

test:
	$(RUN) -m aoc.cli test $(d)

new:
	$(RUN) -m aoc.cli new $(d)

bench:
	$(RUN) -m aoc.cli bench $(d)