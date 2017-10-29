from async_utils import AsyncIteratorExecutor


async def execute_sql(cursor, sql, params=None):
    """
    """
    if not params:
        params = {}
    cursor.execute(sql, params)


async def build_dict(names, cursor):
    """
    build a dict from a cursor result
    """
    return [dict(zip(names, row)) for row in cursor.fetchall()]


# not used
async def build_dict_ex(names, cursor):
    return [dict(zip(names, row)) async for row in AsyncIteratorExecutor(browse_cursor(cursor))]

# not used
async def browse_cursor(cursor):
    for row in cursor:
        await row