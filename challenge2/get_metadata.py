import json
import requests # requests module allows you to send HTTP requests using Python.

IMDS_URL = 'http://169.254.169.254/latest/'  # AWS Instance metadata service


def expand_urls(url, array):
    output = {}
    for items in array:
        full_url = url + items
        r = requests.get(full_url)
        text = r.text

        if items[-1] == "/":
            values = r.text.splitlines()
            output[items[:-1]] = expand_urls(full_url, values)

        elif is_json(text):
            output[items] = json.loads(text)

        else:
            output[items] = text

    return output


def fetch_metadata():
    path = ["meta-data/"]
    total = expand_urls(IMDS_URL, path)
    return total


def fetch_metadata_json():
    metadata = fetch_metadata()
    metadata_json = json.dumps(metadata, indent=1)
    return metadata_json


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print(fetch_metadata_json())