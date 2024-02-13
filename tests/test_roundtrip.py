import keepdb
import seaborn as sns
import tempfile
import pytest


def get_dfs():
	keys = [
	    'diamonds',
	    'car_crashes',
	]

	dfs = {
	    k: sns.load_dataset(k)
	    for k in keys
	}

	return dfs


def test_filename_input():
	dfs = get_dfs()

	with tempfile.TemporaryFile() as f:
		keepdb.to_from.standard.dfs_to_zip(f, dfs)
		dfs2 = keepdb.to_from.standard.zip_to_dfs(f, use_arrow_dtypes=False)

	keepdb.are_df_dicts_equal(dfs, dfs2)


def test_file_object_input():
	dfs = get_dfs()

	with tempfile.NamedTemporaryFile() as f:
		keepdb.to_from.standard.dfs_to_zip(f.name, dfs)
		dfs2 = keepdb.to_from.standard.zip_to_dfs(f.name)

	keepdb.are_df_dicts_equal(dfs, dfs2)


def test_filename_input_arrow():
	dfs = get_dfs()

	with tempfile.TemporaryFile() as f:
		keepdb.to_from.standard.dfs_to_zip(f, dfs)
		dfs2 = keepdb.to_from.standard.zip_to_dfs(f, use_arrow_dtypes=True)

	with pytest.raises(KeyError, match='DictionaryType'):
		# this should work but currently doesn't. i think i'm waiting on https://github.com/pandas-dev/pandas/issues/57395
		keepdb.are_df_dicts_equal(dfs, dfs2)
