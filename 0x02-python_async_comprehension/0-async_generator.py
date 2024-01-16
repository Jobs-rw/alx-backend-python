#!/usr/bin/env python3
"""
The coroutine will loop 10 times, each time asynchronously waiting for 1 second.
"""
import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

# Example usage:
async def main():
    async for number in async_generator():
        print(f"Generated random number: {number}")

# Run the event loop to test the coroutine
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
