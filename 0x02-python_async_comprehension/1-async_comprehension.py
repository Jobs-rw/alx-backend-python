#!/usr/bin/env python3

import asyncio
from typing import List

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

async def async_comprehension() -> List[int]:
    random_numbers = [number async for number in async_generator()]
    return random_numbers

# Example usage:
async def main():
    result = await async_comprehension()
    print(f"Collected random numbers: {result}")

# Run the event loop to test the coroutine
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

