#

[Cunningham's Law]: https://en.wikipedia.org/wiki/Ward_Cunningham#%22Cunningham's_Law%22

I'm sharing this repo in the spirit of [Cunningham's Law]: "The best way to get the right answer on the Internet is not to ask a question; it's to post the wrong answer." I have a problem and can't find a great answer, so I'm posting my attempt in the hope that someone will come along and point me to something better.


## Goals

- build a modern (uses `pyproject.toml` instead of `setup.py`), well-organized, python project
	- try out latest patterns for use in other projects
	- provide examples
	- run coverage on tests also!
	- use ruff, but only with single quotes for chrissake

## Alternatives

- save as a SQLite database?
- save as duckdb database?
- HDF5?


## TODO

- better project name?
- github install instructions
- pypi package
- how best to separate:
	- minimum viable code to install package
	- test package
	- develop, with helper stuff like jupyter lab
	- make an "aggressive version" that just uses pyarrow!


## notes

- df comparison code that requries someone set an idex is putting too much onto the comparison code
	- instead, just compare the DFs for exact equality (at least, up to floating point differences)
	- expect the consumer to sort/order them in a way that makes them comparable.
