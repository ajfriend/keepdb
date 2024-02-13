import pandas as pd


def set_dtype(df):
    return df.convert_dtypes(dtype_backend='numpy_nullable')

def are_dfs_equal(
    left,
    right,
):
    """
    Use `check_dytpe = False` because we sometimes get pandas.Float64Dtype instead of float64
    """

    left = set_dtype(left)
    right = set_dtype(right)

    # Raises informative exception if not equal
    pd.testing.assert_frame_equal(left, right)

    return True


def are_df_dicts_equal(
    left,
    right,
):
    """
    Use `check_dytpe = False` because we sometimes get pandas.Float64Dtype instead of float64
    """

    assert left.keys() == right.keys()

    keys = left.keys()
    for k in keys:
        assert are_dfs_equal(left[k], right[k])

    return True
