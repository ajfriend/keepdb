import keepdb

def test_version():
	assert keepdb.__version__ == '0.0.42'

def test_foo():

	assert keepdb.foo() == 'hi'