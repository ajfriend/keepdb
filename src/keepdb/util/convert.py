import pandas as pd
import pyarrow as pa


def pd2pa(x):
    if isinstance(x, pa.Table):
        return x
    else:
        return pa.Table.from_pandas(x, preserve_index=False)

def pa2pd(x):
    if isinstance(x, pd.DataFrame):
        return x
    elif isinstance(x, pa.Table):
        return x.to_pandas()
    else:
        raise ValueError(f'Unrecognized type: {type(x)}')
