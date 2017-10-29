"""
Set of user controllers.
classical CRUD operations
"""

from aiohttp import web

from dao.user_dao import get_id, get_all, insert_user, change_user, delete_user

async def get_user_by_id(request):
    """
    user retriever, based on technical id
    :param request: aiohttp request
    :return: json format of the user data retrieved or json description of the error
    """
    # get id set by the user into the request
    id = int(request.match_info['id'])

    # execute dao statement
    try:
        res = await get_id(id=int(id))
    except Exception as e:
        print(e)
        return web.json_response({'error': str(e)}, status=500)

    # nothing has been found
    if not res:
        return web.json_response({'error': "User {} not found".format(id)}, status=404)

    # success response
    return web.json_response(res)


async def get_all_users(request):
    """
    retrieve all users registered
    :param request: aioihttp request
    :return: json format of the list of users retrieved or json description of the error
    """

    # execute dao statement
    try:
        res = await get_all()
    except Exception as e:
        print(e)
        return web.json_response({'error': str(e)}, status=500)

    # success response
    return web.json_response(res)


async def create_user(request):
    """
    crate a new user
    :param request: aioihttp request
    :return: json format of the new user id or json description of the error
    """
    # data describing of the user to be created
    data = await request.json()

    # check of the data, we ensure required data are present, name
    name = data.get('name', '__missing__')
    if name == '__missing__':
        return web.json_response({'error': '"name" is a required field'})

    # check of the data type, we ensure required data type are correct present, name
    if not isinstance(name, str) or not len(name):
        return web.json_response({'error': '"name" must be a string with at least one character'})

    # check of the data type, if not age or age is zero we raise an error
    data['age'] = int(data.get('age', 0))
    if not data['age']:
        return web.json_response({'error': '"age" must be a present and greater than 0'})

    # execute dao statement
    try:
        new_id = await insert_user(data)
    except Exception as e:
        print(e)
        return web.json_response({'error': str(e)}, status=500)

    # success response
    return web.json_response({'id': new_id})


async def update_user(request):
    # data describing of the updation to be done, get back the id
    data = await request.json()

    # get id from the url
    user_id = int(request.match_info['id'])

    # check of the data type, we ensure required data type are correct present, name and age
    if not any([data.get('name', None), data.get('age', None)]):
        return web.json_response({'error': '"name" or "age" has to be provided.'})

    # execute dao statement
    try:
        await change_user(user_id, values={k:data[k] for k in ('name','age') if k in data.keys()})
    except Exception as e:
        print(e)
        return web.json_response({'error': str(e)}, status=500)

    # success response
    return web.json_response({'id': user_id})


async def remove_user(request):
    # get id from the url
    user_id = int(request.match_info['id'])

    # execute dao statement
    try:
        await delete_user(user_id)
    except Exception as e:
        print(e)
        return web.json_response({'error': str(e)}, status=500)

    # success response
    return web.json_response({'id': user_id})