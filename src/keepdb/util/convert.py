import pandas as pd
import pyarrow as pa


def pd2pa(x):
    #  todo: add check that indices are not allowed
    return pa.Table.from_pandas(x, preserve_index=False)

def pa2pd(x, use_arrow_dtypes=False):
    assert isinstance(x, pa.Table)

    if use_arrow_dtypes:
        return x.to_pandas(types_mapper=pd.ArrowDtype)
    else:
        return x.to_pandas()
