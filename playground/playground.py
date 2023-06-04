import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down



CREATE TABLE 'inventory' (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
user_id INTEGER NOT NULL,
symbol TEXT NOT NULL,
shares INTEGER DEFAULT 0,
buy_price NUMERIC,
buy_time TIMESTAMP,
sell_price NUMERIC,
sell_time TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES users (id)
);



pk_6cc83872fd334e7d88fb9862dfe7ba58