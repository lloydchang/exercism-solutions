def hello():
    foo = 'Hello, '
    bar = 'World!'
    if not foo or not bar:
        raise Exception("foo or bar wasn't created")
    return foo + bar