import pandas as pd


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
