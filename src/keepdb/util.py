# convert to arrow
# return as arrow
# helper functions to test that files are exactlyt he same. or dbs.

def foo():
    print('heeeeeey')

# def dfs_to_zip(filename, dfs):
#     """ Store a dict of dataframes as a zip archive containing parquet files for each
#     filename: str
#     dfs: dict[str, pd.DataFrame]
#     """
#     # note: not sure the zip compression does much on top of the parquet compression. maybe drop?
#     with zipfile.ZipFile(filename, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
#         for df_name, df in dfs.items():
#             b = df.to_parquet(compression='brotli', index=False, engine='pyarrow')
#             z.writestr(f'{df_name}.parquet', b)

# def zip_to_dfs(filename):
#     out = {}
#     with zipfile.ZipFile(filename, 'r') as zf:
#         for name in zf.namelist():
#             data = zf.read(name)
#             data = io.BytesIO(data)
#             df = pd.read_parquet(data, dtype_backend='pyarrow', engine='pyarrow')
#             assert name.endswith('.parquet')
#             name = name[:-8]
#             out[name] = df
#     return out