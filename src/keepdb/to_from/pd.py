from ..util.convert import pd2pa, pa2pd
from . import pa


def to_zip(zip_file, dfs):
    """ Store a dict of dataframes as a zip archive containing parquet files for each
    zip_file: str
    dfs: dict[str, pd.DataFrame]
    """
    tables = {
        k: pd2pa(v)
        for k,v in dfs.items()
    }

    pa.to_zip(zip_file, tables)


def from_zip(zip_file):
    tables = pa.from_zip(zip_file)
    dfs = {
        k: pa2pd(v)
        for k,v in tables.items()
    }

    return dfs
