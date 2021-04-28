import asyncio
from functools import partial

async def wrap_async(func, *args, **kwargs):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, partial(func, *args, **kwargs))
    
    response = await future
    return response
