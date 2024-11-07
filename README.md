# CIM Transformer: JSON to XML Converter

This Python program, `cimtransformer.py`, reads a JSON file and converts its data into an XML format, specifically an RDF (Resource Description Framework) XML. 

The conversion is designed to handle JSON-LD (JSON for Linked Data) files, commonly used for structured, semantic data. 

### Program Overview

The program is structured as follows:

1. **Logging Function (`logg`)**:
    - A simple logging function that prints debug messages to standard error if `debug` is set to `True`.
  
2. **Main Function (`read_json_file`)**:
    - Reads a JSON file and parses it into an RDF-XML format.
    - Assumes the JSON data contains an `@context` for namespaces and an `@graph` with entities.

3. **Command Line Execution**:
    - Expects a file name as a command-line argument.
    - Usage: `python cimtransformer.py <filename>`

### Detailed Explanation

1. **Namespace Extraction**:
    - For each key-value pair in `@context`, the program generates an XML namespace declaration.
    - Ignores `@vocab`, which is not needed as a standalone namespace.

2. **Entity Processing**:
    - For each entity in `@graph`, the program retrieves:
      - `@id`: used as the RDF ID.
      - `@type`: used as the XML element type.
    - The program prints each entity and its properties in XML, following the RDF schema.

3. **Property Conversion**:
    - Processes properties of each entity based on data type:
      - **Dictionary Values**: Checks for `@id` to treat it as a resource link; otherwise, assumes it has `@type` and `@value`.
      - **List Values**: Assumes each item in the list is an RDF resource.
      - **Other Values**: Prints directly within the XML tags for basic data types (e.g., strings).

4. **Output**:
    - Wraps the entire output in `<rdf:RDF>` tags to represent a complete RDF document.

### Example JSON to XML Conversion

Given a JSON file structured as follows:

```json
{
  "@context": {
    "ex": "http://example.com/",
    "@vocab": "http://example.org/"
  },
  "@graph": [
    {
      "@id": "ex:person1",
      "@type": "ex:Person",
      "name": "John Doe",
      "knows": { "@id": "ex:person2" }
    }
  ]
}
```

The program would generate the following XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF
  xmlns:ex="http://example.com/"
>
<ex:Person rdf:ID="ex:person1">
  <name>John Doe</name>
  <knows rdf:resource="ex:person2"/>
</ex:Person>

</rdf:RDF>
```


