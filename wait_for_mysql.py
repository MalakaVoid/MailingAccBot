import asyncio

from wait_db import mysql_connect, wait

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(wait(mysql_connect))
