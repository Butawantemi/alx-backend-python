#!/usr/bin/env python3
"""an program to measure the runtime of async function"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure the async function execution time

    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    runtime = (time.perf_counter() - start) / n
    return runtime
