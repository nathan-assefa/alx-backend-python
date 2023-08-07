import asyncio

async def task_one():
    await asyncio.sleep(5)
    return "Task One Completed"

async def task_two():
    await asyncio.sleep(1)
    return "Task Two Completed"

async def main():
    tasks = await asyncio.gather(task_one(), task_two())
    print(tasks)

asyncio.run(main())
