import sys
import json

debug = False

def logg(message):
    if debug:
            
        print(message, file=sys.stderr)


def read_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)

        print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        print(f"<rdf:RDF")

        for key, value in data.get("@context").items():
            if key != "@vocab":
                print(f"  xmlns:{key}=\"{value}\"")
        print(">")
                
        for entity in data.get("@graph") :
            id = entity.get("@id")
            entity_type = entity.get("@type")
            print(f"<{entity_type} rdf:ID=\"{id}\">")
            for key, value in entity.items():
                if key != "@id" and key != "@type": 
                    if type(value) is dict:
                        if value.get("@id") is not None:
                            print(f"  <{key} rdf:resource=\"{value.get("@id")}\"/>")
                        else:
                            print(f"  <{key} rdf:type=\"{value.get("@type")}\">{value.get("@value")}</{key}>")
                    elif type(value) is list:
                        for v in value:
                            print(f"  <{key} rdf:resource=\"{v.get("@id")}\"/>")
                    else:
                        print(f"  <{key}>{value}</{key}>")
            print(f"</{entity_type}>\n")
            
        print("</rdf:RDF>")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cimtransformer.py <filename>")
    else:
        file_name = sys.argv[1]
        read_json_file(file_name)
