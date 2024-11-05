import sys
import json

debug = False

def logg(message):
    if debug:
            
        print(message, file=sys.stderr)


def read_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        for entity in data.get("@graph") :
            print(entity.get("name"))
            id = entity.get("@id")
            type = entity.get("@type")
            print(f"<{type} rdf:ID=\"{id}\">")
            print(f"</{type}>")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cimtransformer.py <filename>")
    else:
        file_name = sys.argv[1]
        read_json_file(file_name)
