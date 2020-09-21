import yaml

def readFile(fileName, file_desc):
    file= open(fileName, 'r',encoding='utf-8')
    dictToCreate={"type": "object",
                    "description": file_desc,
                    "properties":[]}
    for readLine in file:
        attr = readLine.split(" ")[0].lstrip().rstrip()
        type = readLine.split(" ")[1].lstrip().rstrip()        
        desc = readLine[len(attr)+len(type)+2 : len(readLine)].lstrip().rstrip()
        thisdict = {}
        if type.lower() == "string" or type.lower() == "integer" or type.lower() == "boolean" :
            thisdict[attr] = {
                "type": type,
                "description": desc
            } 
        elif type.lower() == "datetime":  
            thisdict[attr] = {
                "type": "string",
                "format": "date-time",
                "description": desc
            }    
        elif type.lower() == "timeperiod":  
            thisdict[attr] = {
                "$ref": "#/components/schemas/"+type,
                "description": desc
            }                           
        else:
            print("{0} ---> {1}".format(attr, type.lower()))
            type = "array"
            items = {
                "$ref": "#/components/schemas/"+attr
            }
            thisdict[attr] = {
                "type": type,
                "items": items,
                "description": desc
            }  
        dictToCreate["properties"].append(thisdict)
        # dictToCreate["properties"] = dict(thisdict)
        
    return dictToCreate

def writeYaml(fileName, data):
    with open(fileName, 'w') as file:
        yaml.dump(data, file)

def _run():
    fileName = input('Enter the file name for the schema:')
    splitFile = fileName.split("/")
    print("{0}----->{1}".format(splitFile, len(splitFile)))
    p_fileName = splitFile[len(splitFile)-1].replace("txt","yml")
    writeYaml("schemas/"+p_fileName,readFile(fileName,p_fileName.replace(".yml","")))

_run()