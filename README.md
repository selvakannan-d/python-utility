# python-utility
Python utilities for day today work

# Pre-requistie
    - python3
    
# file Generator

This app is used to create file from the given input file

- schemaGenerator:
    - This process creates schema file from the given input text file.
    - Input text file should be space delimited file.
    - Splits and considers first 2 spaces
        - First attr: attribute name on the schema file
        - second attr: type for the attribute
        - rest: description for the attribute
        - e.g. data, for best practice create your input file under "file" folder
         ```
         name string this field holds name for the string
         ref Attachment this field holds attachment object
         ```
         - e.g. output, out put are generated on "schema/"
         ```
description: test
properties:
- name:
    description: this field holds name for the string
    type: string
- ref:
    description: this field holds attachment object
    items:
      $ref: '#/components/schemas/ref'
    type: array
type: object

         ```

# How to run

```
> python --version               Python 3.8.6rc1

> python .\schemaGenerator.py
Enter the file name for the schema:file/test.txt
['file', 'test.txt']----->2
 --->
```


