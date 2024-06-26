# Q.1
import time

def time_dec(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran for {end-start} time")
        return result
    return wrapper

@time_dec
def timer(n):
    time.sleep(n)
    
# timer(3)

# Q.2

def debug(func):
    def wrapper(*args, **kwargs):
        arg_value = ', '.join(str(arg) for arg in args)
        kwarg_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"args: {arg_value}")
        print(f"kwargs: {kwarg_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting):
    print(f"{greeting}, {name}")
    
greet("Mitva", greeting="Hello")

# Q.3

def cache(func):
    cache_values = {}
    def wrapper(*args, **kwargs):
        if args in cache_values:
            return cache_values[args]
        result = func(*args, **kwargs)
        cache_values[args] = result
        return result
    return wrapper

@cache
def some_api_call(a, b):
    time.sleep(3)
    return a + b

print(some_api_call(2, 3))
print(some_api_call(2, 3))
print(some_api_call(5, 6))
print(some_api_call(5, 6))

