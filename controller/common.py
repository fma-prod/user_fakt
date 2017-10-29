"""
End points controller implementation
"""
from aiohttp import web
import version


async def ping(request):
    return web.json_response({'Server Status': 'Ok',
                              'API version': version.version,
                              'API name': version.name})
