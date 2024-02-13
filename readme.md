# keepdb

Store and retrieve Pandas DataFrames in a `.zip` file of `.parquet` files.


## Install

```
pip install git+https://github.com/ajfriend/keepdb
```

## Quickstart

Assume you have Pandas DataFrames like `df_diamonds` and `df_car_crashes`:

```python
# using seaborn to provide example DataFrames
import seaborn as sns
df_diamonds = sns.load_dataset('diamonds')
df_car_crashes = sns.load_dataset('car_crashes')
```

You can use `keepdb` to save both DataFrames to `test_file.zip`
and read them back like:

```python
import keepdb as kd

dfs = {'diamonds': df_diamonds, 'car_crashes': df_car_crashes}

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
