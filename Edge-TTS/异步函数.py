import asyncio

async def foo():
    print("Start foo")
    await asyncio.sleep(1)
    print("End foo")

async def bar():
    print("Start bar")
    await asyncio.sleep(2)
    print("End bar")

async def main():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(bar())

    await task1
    await task2

# 运行输出
asyncio.run(main())
