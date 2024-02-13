# keepdb

Store and retrieve Pandas DataFrames in a `.zip` file of `.parquet` files.


## Install

```
pip install git+https://github.com/ajfriend/keepdb
```

## Quickstart

```python
import keepdb as kd
import seaborn as sns

dfs = {
    'diamonds':    sns.load_dataset('diamonds'),
    'car_crashes': sns.load_dataset('car_crashes'),
}

kd.to_zip('test_file.zip', dfs)
dfs2 = kd.from_zip('test_file.zip')
```

See more details in [notebooks/examples.ipynb](notebooks/examples.ipynb).

## Alternatives

[Cunningham's Law]: https://en.wikipedia.org/wiki/Ward_Cunningham#%22Cunningham's_Law%22

This repo is an attempt to exploit
[Cunningham's Law]: "**The best way to get the right answer on the Internet
is not to ask a question; it's to post the wrong answer.**"

I haven't found a better solution for storing collections of tabular data
(relational databases) in a single file or data structure that:

- works well with or uses Apache Arrow, which seems to be the future of the PyData ecosystem
- isn't just saving a database backup file (e.g, SQLite or DuckDB)

I'd love to hear if anyone has suggestions for a better system!
