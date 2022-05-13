from get_metadata import fetch_metadata # Importing the function from another python module

def dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for r in dict_extract(key, v):
                    yield r
            elif isinstance(v, list):
                for d in v:
                    for r in dict_extract(key, d):
                        yield r


def find_key(key):
    metadata = fetch_metadata()
    return list(dict_extract(key, metadata))


if __name__ == '__main__':
    key = input("What key would you like to find from Instance metadata JSON?\n")
    print(find_key(key))