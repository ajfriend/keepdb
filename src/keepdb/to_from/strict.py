import zipfile
import io
import pyarrow.parquet as pq

"""
this should be just pyarrow to pyarrow. pytable to pytable. super strict.
use this as the tool to save the less-strict case.
"""

def table_to_parquet_bytes(table):
    b = io.BytesIO()
    pq.write_table(table, b, compression='brotli')
    return b.getvalue()

def parquet_bytes_to_table(b):
    b = io.BytesIO(b)
    return pq.read_table(b)

def without_suffix(name, suffix='.parquet'):
    assert name.endswith(suffix)
    n = len(suffix)
    return name[:-n]


def dfs_to_zip(zip_file, tables):
    """ Store a dict of dataframes as a zip archive containing parquet files for each
    zip_file: str
    tables: dict[str, pa.Table]
    """
    with zipfile.ZipFile(zip_file, 'w') as z:
        for table_name, table in tables.items():
            z.writestr(
                f'{table_name}.parquet',
                table_to_parquet_bytes(table),
            )

def zip_to_dfs(zip_file):
    tables = {}
    with zipfile.ZipFile(zip_file, 'r') as z:
        for file_name in z.namelist():
            b = z.read(file_name)
            table = parquet_bytes_to_table(b)
            table_name = without_suffix(file_name, '.parquet')
            tables[table_name] = table

    return tables
