import keepdb
import seaborn as sns
import tempfile
import pytest

def test_filename_input():
	keys = [
	    'diamonds',
	    'car_crashes',
	]

	dfict = {
	    k: sns.load_dataset(k)
	    for k in keys
	}

	with tempfile.TemporaryFile() as f:
		keepdb.to_from.standard.dfs_to_zip(f, dfict)
		dfict2 = keepdb.to_from.standard.zip_to_dfs(f, use_arrow_dtypes=False)

		keepdb.are_df_dicts_equal(dfict, dfict2)


def test_file_object_input():
	keys = [
	    'diamonds',
	    'car_crashes',
	]

	dfict = {
	    k: sns.load_dataset(k)
	    for k in keys
	}

	with tempfile.NamedTemporaryFile() as f:
		keepdb.to_from.standard.dfs_to_zip(f.name, dfict)
		dfict2 = keepdb.to_from.standard.zip_to_dfs(f.name)

		keepdb.are_df_dicts_equal(dfict, dfict2)
