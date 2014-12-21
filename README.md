# technicolor

logging in colour

# introduction

technicolor provides logging in colour and logging of function usage by means of a simple decorator.

# quick start

In the main code of the program could be a technicolor logging setup such as the following:

```Python
global log
log = logging.getLogger(__name__)
logging.root.addHandler(technicolor.ColorisingStreamHandler())
if self.verbose:
    logging.root.setLevel(logging.DEBUG)
else:
    logging.root.setLevel(logging.INFO)
```

Then, in modules imported, there could be a logging setup such as the following:

```Python
log = logging.getLogger(__name__)
```

The function logging of technicolor logs the name of the function called, the caller of the function and the arguments of the function used. This functionality can be engaged by using a decorator in a way such as the following:

```Python
@technicolor.log
def function1(
    a,
    b,
    c = 4,
    d = 5,
    e = 6
    ):
    return(a + b + c + d + e)
```
