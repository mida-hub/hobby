import time
import asyncio

def is_prime(n):
    return not any(n%i==0 for i in range(2, n//2))

async def highest_prime(x):
    print(f'{x}未満の数で最も大きな素数')
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print(f'{x}未満の素数で最も大きな素数は{y}')
            return y
        # time.sleep(0.02)
        await asyncio.sleep(0.02)
    return None

async def main():
    t0 = time.time()
    await asyncio.wait([
        highest_prime(10000),
        highest_prime(1000),
        highest_prime(100)
    ])
    t1 = time.time()
    print(f'経過時間: {(t1-t0) * 1000} ms')

# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())