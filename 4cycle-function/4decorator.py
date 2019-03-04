def document_it(func):
    def new_func(*args, **kwargs):
        print("- Running function:", func.__name__)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return new_func

def add_ints(a, b):
    return a + b

print("Origin function:", add_ints(1, 1))

decorated = document_it(add_ints) # Мануальное присваивание
decorated(2, 2)


@document_it # Альтернатива мануальному присваиванию
def add_str(a, b):
    return a + " " + b

add_str("str1", "str2")