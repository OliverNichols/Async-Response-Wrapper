# Async-Response-Wrapper
Simple function for wrapping synchronous (blocking) functions in asyncio. Useful to allow multi-threading in Python for modules such as requests.

## Example usage
```py
import asyncio_wrapper, requests

async def fetch_google():
    response = await asyncio_wrapper(requests.get, 'https://google.com', *args, **kwargs)
    ...
```
