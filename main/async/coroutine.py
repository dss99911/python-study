import time

import asyncio


# https://docs.python.org/3/library/asyncio-task.html
# awaitable objects: coroutines, Tasks, and Futures.


async def use_coroutine():
    """use coroutine"""

    print("hello")
    coro = _say_after(1, 'start coroutine before sleep')
    await asyncio.sleep(2)
    print("after sleep")
    await coro
    print('world')


async def _say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def use_task():
    """able to run concurrently"""
    # task is get started when create_task

    # task is added to loop
    task2 = asyncio.create_task(
        _say_blocking_after(2, 'task2'))

    # as it's sleep, run the task above on the next in the loop
    await asyncio.sleep(1)

    # this is called after task2 is completed. because task2 is blocked 2secs
    print("task2 is already started without await")
    await task2


async def _say_blocking_after(delay, what):
    time.sleep(delay)
    print(what)


async def use_gather():
    """Schedule three calls *concurrently*:"""
    await asyncio.gather(
        _factorial("A", 2),
        _factorial("B", 3),
        _factorial("C", 4),
    )


async def _factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


async def run_in_thread():
    """
    running in threads
    used for executing IO-bound functions/methods
    """
    await asyncio.gather(
        asyncio.to_thread(_blocking_io),
        asyncio.sleep(1))


def _blocking_io():
    time.sleep(1)


async def run_coroutine_in_thread():
    """
    running coroutine in threads
    """
    await asyncio.gather(
        asyncio.run_coroutine_threadsafe(_factorial("a", 1)),
        asyncio.sleep(1))


async def use_cancel():
    # Create a "cancel_me" Task
    task = asyncio.create_task(_cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")


async def _cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


if __name__ == '__main__':
    asyncio.run(use_task())
    # asyncio.run(use_coroutine())
    # asyncio.run(use_gather())
    print("main")
