import os
from dataclasses import dataclass

HOST = str(os.getenv('MYSQL_HOST', default="127.0.0.1"))
PORT = int(os.getenv('MYSQL_PORT', default=3306))
USER = str(os.getenv('MYSQL_USER', default='test_user'))
PASSWORD = str(os.getenv('MYSQL_PASSWORD', default='secret'))
DB = str(os.getenv('MYSQL_DATABASE', default='test'))
POOL_SIZE_INIT = int(os.getenv('MYSQL_POOLSIZE_INIT', default=16))
DSN_CHARSET = str(os.getenv('MYSQL_DSN_CHARSET', default='utf8mb4'))
POOL_SIZE = int(os.getenv('MYSQL_POOL', default=32))
AUTOCOMMIT = bool(os.getenv('MYSQL_AUTOCOMMIT', default=1))
MYSQL_STATSD_REPORT = bool(os.getenv('MYSQL_STATSD_REPORT', default=False))
MYSQL_STATSD_PERIODIC_REPORTS_DELAY = int(os.getenv('MYSQL_STATSD_PERIODIC_REPORTS_DELAY', default=5))
DSN = str(os.getenv('MYSQL_DSN', default=f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}?charset={DSN_CHARSET}'))
MYSQL_DEBUG_OUTPUT = bool(os.getenv('MYSQL_DEBUG_OUTPUT', default=0))
MYSQL_NEW_CONNPOOL = bool(os.getenv('MYSQL_NEW_CONNPOOL', default=0))
WSREP_SYNC_WAIT = int(os.getenv('MYSQL_WSREP_SYNC_WAIT', default=0))
TRANSACTION_ISOLATION_LEVEL = str(os.getenv('MYSQL_TRANSACTION_ISOLATION_LEVEL', default='READ COMMITTED'))


@dataclass
class MysqlDSN:
    user: str = USER
    password: str = PASSWORD
    host: str = HOST
    port: str = PORT
    db: str = DB
    pool_size_init: int = POOL_SIZE_INIT
    pool_size: int = POOL_SIZE
    dsn_charset: str = DSN_CHARSET
    autocommit: bool = AUTOCOMMIT
    mysql_debug_output: bool = MYSQL_DEBUG_OUTPUT
    mysql_new_connpool: bool = MYSQL_NEW_CONNPOOL
    dsn: str = DSN
    wsrep_sync_wait: int = WSREP_SYNC_WAIT
    transaction_isolation_level: str = TRANSACTION_ISOLATION_LEVEL
    mysql_statsd_report: bool = MYSQL_STATSD_REPORT
    mysql_statsd_periodic_reports_delay: int = MYSQL_STATSD_PERIODIC_REPORTS_DELAY