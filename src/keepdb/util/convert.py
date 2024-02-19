import pyarrow as pa


def pd2pa(df):
    df = df.convert_dtypes(dtype_backend='pyarrow')
    return pa.Table.from_pandas(df, preserve_index=False)

def pa2pd(table):
    assert isinstance(table, pa.Table)

    df = table.to_pandas()
    df = df.convert_dtypes(dtype_backend='pyarrow')

    return df

def canon(df):
    table = pd2pa(df)
    return pa2pd(table)
