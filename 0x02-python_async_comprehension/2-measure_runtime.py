#!/usr/bin/env python3
"""executing async_comprehension four times in paralle"""
import asyncio
from previous_file import async_comprehension

async def measure_runtime():
    start_time = time.time()

    # Use asyncio.gather to execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime

# Run the event loop and print the result
if __name__ == "__main__":
    import time
    asyncio.run(measure_runtime())

