# python-utility
Python utilities for day today work

# Pre-requistie
    - python3

  
# file Generator

This app is used to create file from the given input file

- schemaGenerator.py:
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
How to run:


> python --version               
Python 3.8.6rc1

> python .\schemaGenerator.py
Enter the file name for the schema:file/test.txt
['file', 'test.txt']----->2
 --->
```

------------------------------------------------------------------------

# file Validator

This app is used to valiate files

- YAMLValitor.py:
    - Validates files in the folder is valid YAML or not.
    - output type
        - if the file is of not ".yml" extension
            - Not an yaml file <file name>
        - if the file is invalid yaml file
            - Error on file: <file name> : error: <error info>
        - if it has subfolders
            - -----------is an Folder <folder path>----------

```
How to run:

    > python --version               
    Python 3.8.6rc1

    > python YAMLValidator
    Enter the folder/parent path of the yaml: < enter the path> 

    e.g. output (test output on fileValidator/test.txt)
    Enter the folder/parent path of the yaml files: -----------is an Folder C:\Users\selva\work\code\wow-api-gateway\src/authorizer----------
        Not an yaml file auth-policy.js
        Not an yaml file authorizer.js
        Not an yaml file build-policy.js
        Not an yaml file verify-jwt.js
        -----------is an Folder C:\Users\selva\work\code\wow-api-gateway\src/authorizer----------
        Not an yaml file cloud-formation.json
        Not an yaml file deploy.js
        -----------is an Folder C:\Users\selva\work\code\wow-api-gateway\src/handlers----------
        Not an yaml file get-rest-api.js
        Not an yaml file process-api-gateway-logs.js
        .
        .
        .


```
