import sys
import asyncio
import traceback
from settings import MysqlDSN


async def mysql_connect(config=MysqlDSN, timeout=10):
    '''
    Attempt coonection to mysql, located at `config` host, port, db, etc.

    :param config: module (file) with constants or mocking object
    :param timeout: connection timeout
    :return: aiomysql connection
    '''
    import aiomysql
    print(f'config: {config.host}, {config.port}, {config.db}, {config.user}, {config.password}')
    return await aiomysql.connect(host=config.host, port=config.port,
                                  db=config.db, user=config.user,
                                  password=config.password,
                                  connect_timeout=timeout)


async def wait(connector, retries=10, to_wait=10, **conn_args):
    '''
    Tries one of the above `connectors` `retries` times. Returns to OS:
    0 if connection is sucessful (meaning DB is online), or smth > 0,
    indicating connection error (meaning DB is probably offline).

    :param connector: coroutine function, creates db connection
    :param retries: try to connect that many times
    :param conn_args: arguments for connector coroutine
    '''
    errors = set()
    for i in range(retries):
        try:
            await connector(**conn_args)
            sys.exit(0)
        except Exception as e:
            sys.stderr.write(f'{connector.__name__} failed #{i}\n')
            tb = traceback.format_exc()
            errors.add(tb)
            if isinstance(e, ImportError):
                break  # driver not installed, no point to wait
            await asyncio.sleep(to_wait)

    for error in errors:
        print(error)
    sys.exit(128)
