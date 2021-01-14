# Async-Response-Wrapper
Simple function for wrapping synchronous (blocking) functions in asyncio. Useful to allow multi-threading in Python for modules such as requests.

## Example usage
```py
from asyncio-wrapper import wrap_async
import requests # optional, for this example

async def fetch_google():
    response = await wrap_async(requests.get, 'https://google.com', *args, **kwargs)
    ...
```
