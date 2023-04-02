import json


def extract_json_payload(filename):
    with open(filename, "r") as json_file:
        return json.load(json_file)
