import zipfile
import io
import pandas as pd


def dfs_to_zip(filename, dfs):
    """ Store a dict of dataframes as a zip archive containing parquet files for each
    filename: str
    dfs: dict[str, pd.DataFrame]
    """
    # note: not sure the zip compression does much on top of the parquet compression. maybe drop?
    with zipfile.ZipFile(filename, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for df_name, df in dfs.items():
            b = df.to_parquet(compression='brotli', index=False, engine='pyarrow')
            z.writestr(f'{df_name}.parquet', b)

def zip_to_dfs(filename):
    out = {}
    with zipfile.ZipFile(filename, 'r') as zf:
        for name in zf.namelist():
            data = zf.read(name)
            data = io.BytesIO(data)
            df = pd.read_parquet(data, dtype_backend='numpy_nullable')
            assert name.endswith('.parquet')
            name = name[:-8]
            out[name] = df
    return out


def are_dfs_equal(
    left,
    right,
    check_dtype = False
):
    """
    Use `check_dytpe = False` because we sometimes get pandas.Float64Dtype instead of float64
    """

    # Raises informative exception if not equal
    pd.testing.assert_frame_equal(
        left,
        right,
        check_dtype = check_dtype
    )

    return True


def are_df_dicts_equal(
    left,
    right,
    check_dtype = False
):
    """
    Use `check_dytpe = False` because we sometimes get pandas.Float64Dtype instead of float64
    """

    assert left.keys() == right.keys()

    keys = left.keys()
    for k in keys:
        assert are_dfs_equal(left[k], right[k], check_dtype=check_dtype)

    return True








