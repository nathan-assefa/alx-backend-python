import asyncio

async def async_count_up_to(limit):
    for i in range(limit):
        await asyncio.sleep(1)  # Simulating some asynchronous operation
        yield i

async def main():
    print(async_count_up_to(3))
    async for num in async_count_up_to(3):
        print(num)

asyncio.run(main())
