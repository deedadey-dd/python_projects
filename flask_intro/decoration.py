import time


def delay_dec(function):
    def wrapper_function():
        time.sleep(3)
        function()
        time.sleep(2)
        function()
    return wrapper_function


@delay_dec
def simple_hello():
    print("Hello Dee...")


simple_hello()
