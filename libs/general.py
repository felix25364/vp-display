import asyncio


async def multitask(*args):
    return await asyncio.gather(*args)