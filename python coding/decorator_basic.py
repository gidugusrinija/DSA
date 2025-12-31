def log(func):
    def wrapper(*args, **kwargs):
        print(f"calling the function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log
def add(a, b):
    return a+b

print(add(1,8))
