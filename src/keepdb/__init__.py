from ._version import __version__

from .util.compare import (
	are_dfs_equal,
	are_df_dicts_equal,
)

from .util.convert import pa2pd, pd2pa, canon

from .to_from import pa, pd
from .to_from.pd import (
	to_zip,
	from_zip,
)

__all__ = (
	to_zip,
	from_zip,
	pa2pd,
	pd2pa,
	canon,
	pa,
	pd,
	are_dfs_equal,
	are_df_dicts_equal,
	__version__,
)
