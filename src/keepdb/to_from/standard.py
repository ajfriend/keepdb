from ..util.convert import pd2pa, pa2pd
from . import strict


def dfs_to_zip(filename, dfs):
    """ Store a dict of dataframes as a zip archive containing parquet files for each
    filename: str
    dfs: dict[str, pd.DataFrame]
    """
    tables = {
        k: pd2pa(v)
        for k,v in dfs.items()
    }

    strict.dfs_to_zip(filename, tables)


def zip_to_dfs(filename, use_arrow_dtypes=False):
    tables = strict.zip_to_dfs(filename)
    dfs = {
        k: pa2pd(v, use_arrow_dtypes)
        for k,v in tables.items()
    }

    return dfs
