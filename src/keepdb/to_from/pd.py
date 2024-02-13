from ..util.convert import pd2pa, pa2pd
from . import pa


def to_zip(filename, dfs):
    """ Store a dict of dataframes as a zip archive containing parquet files for each
    filename: str
    dfs: dict[str, pd.DataFrame]
    """
    tables = {
        k: pd2pa(v)
        for k,v in dfs.items()
    }

    pa.dfs_to_zip(filename, tables)


def from_zip(filename):
    tables = pa.zip_to_dfs(filename)
    dfs = {
        k: pa2pd(v)
        for k,v in tables.items()
    }

    return dfs