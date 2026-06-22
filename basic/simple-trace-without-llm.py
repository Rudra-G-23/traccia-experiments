from rich.pretty import pprint
from traccia import init, observe

init(enable_console_exporter=True)


# Trace any function
@observe()
def my_function(x, y):
    return x + y


result = my_function(2, 3)
pprint(result)
