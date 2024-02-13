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
