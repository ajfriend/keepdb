import keepdb
import seaborn as sns
import tempfile
import pytest


def _get_dfs():
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
	dfs = _get_dfs()

	with tempfile.TemporaryFile() as f:
		keepdb.to_zip(f, dfs)
		dfs2 = keepdb.from_zip(f)

	assert keepdb.are_df_dicts_equal(dfs, dfs2)


def test_file_object_input():
	dfs = _get_dfs()

	with tempfile.NamedTemporaryFile() as f:
		keepdb.to_zip(f.name, dfs)
		dfs2 = keepdb.from_zip(f.name)

	assert keepdb.are_df_dicts_equal(dfs, dfs2)
