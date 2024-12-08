TAG_LOOKUP = {}


def tag(name):
    global TAG_LOOKUP

    def decorator(fn):
        TAG_LOOKUP[name] = fn
        return fn

    return decorator


def get_tag_handler(name):
    global TAG_LOOKUP
    return TAG_LOOKUP.get(name)
