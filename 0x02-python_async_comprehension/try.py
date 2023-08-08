import asyncio

# Regular List
def generate_list():
    result = []
    for i in range(1000000):
        result.append(i)
    return result

# Asynchronous Generator
async def async_generate():
    for i in range(1000000):
        await asyncio.sleep(0.001)  # Simulate asynchronous operation
        yield i

async def main():
    # Regular List
    regular_list = generate_list()
    print("Memory used by regular list:", regular_list.__sizeof__())
    
    # Asynchronous Generator
    async_gen = async_generate()
    print("Memory used by async generator:", async_gen.__sizeof__())

    async for _ in async_gen:
        pass

asyncio.run(main())
