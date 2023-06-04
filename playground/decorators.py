def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


CREATE TABLE inventory (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL,
    shares NUMERIC NOT NULL,
    buy_price NUMERIC NOT NULL,
    buy_time TIMESTAMP NOT NULL,
    FOREIGN KEY (id) REFERENCES users (id)
);

CREATE TABLE main_table (
    id serial PRIMARY KEY,
    nested_data inventory
);