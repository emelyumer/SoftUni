def tags(expected_tag):
    def decorator(func):
        def wrapper(*args):
            return f"<{expected_tag}>{func(*args)}</{expected_tag}>"

        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))




