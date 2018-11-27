def hello():
    # return "Hello, World!"
    foo = "Hello, "
    bar = "World!"
    if not foo or not bar:
        raise Exception("Meaningful message indicating the source of the error")
    return foo + bar