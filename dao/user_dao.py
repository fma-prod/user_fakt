from dao.lib import execute_sql, build_dict
from port.db.sqlite.setup import conn, create_tables


# create tables if they don't already exist
create_tables()


async def get_all():
    """
    get all users registred in DB
    :return: list of users (dict)
    """
    cursor  = conn.cursor()

    # build sql statements
    sql = """
      SELECT id, name, age FROM users
      """

    # execute sql against targeted DB
    await execute_sql(cursor, sql)

    # properly format results
    names = [d[0] for d in cursor.description]
    things = await build_dict(names, cursor)
    return things


async def get_id(id=None):
    """
    get a user given its technical id
    :param id: technical id of the user to be retrieved
    :return: user (dict)
    """
    cursor = conn.cursor()

    # build sql statements
    sql = """
      SELECT id, name, age FROM users where id= :id
      """

    # execute sql against targeted DB
    await execute_sql(cursor, sql, {'id': id})

    # properly format results
    names = [d[0] for d in cursor.description]
    things = await build_dict(names=names, cursor=cursor)
    return things


async def insert_user(user):
    """
    Insert a new user
    :param user: user dict format
    :return: technical id of user just inserted
    """
    cursor = conn.cursor()

    # build sql statements
    sql = """
      INSERT INTO users(name, age) VALUES(:name, :age)
      """

    # execute sql against targeted DB
    await execute_sql(cursor, sql, user)

    # commit and send back results
    conn.commit()
    return cursor.lastrowid


async def change_user(id=None, values=None):
    """
    set values of the user identified by 'id' technical id
    :param id:  integer
    :param values: dict of fields to be updated
    :return: None
    """
    updation = ', '.join(['{}=:{}'.format(k, k) for k in values.keys()])
    cursor = conn.cursor()

    # build sql statements
    sql = """
      UPDATE users SET {} WHERE id=:id
      """.format(updation)

    # execute sql against targeted DB
    await execute_sql(cursor, sql, params={'id':id, **values})

    # commit and send back results
    conn.commit()



async def delete_user(id):
    """
    delete user identified by id (technical id)
    :param id: technical id
    :return: None
    """
    cursor = conn.cursor()

    # build sql statements
    sql = """
        DELETE from users WHERE id=:id
        """

    # execute sql against targeted DB
    await execute_sql(cursor, sql, params={'id':int(id)})

    # commit and send back results
    conn.commit()
