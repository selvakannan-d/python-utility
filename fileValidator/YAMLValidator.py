import yaml
import sys
import os 

def validateYAML(__yaml_path):
    with open(__yaml_path, 'r') as stream:
        try:
            yaml.load(stream, Loader=yaml.FullLoader)
            print('Valid YAML {0}'.format(__yaml_path))
            return True
        except yaml.YAMLError as exception:
            print('Error on file: {0} : error: {1}'.format(__yaml_path,exception))
            # raise exception
                
def readFilenames(dir):
    my_files = os.listdir(dir)
    for x in my_files :
        if x.endswith('.yml') or x.endswith('.yaml'):
            validateYAML(dir+'/'+x)
        else:
            if x.find(".") < 0 :
                print('-----------is an Folder {0}----------'.format(dir+'/'+x))
                readFilenames(dir+'/'+x)
                print('-----------is an Folder {0}----------'.format(dir+'/'+x))
            else:
                print('Not an yaml file {0}'.format(x))
    

def _run():
    path = input('Enter the folder/parent path of the yaml files: ')
    readFilenames(path)

_run()

# __load_doc("C:/Users/selva/work/code/python-utility/fileGenerator/schemas/test.yml")
# yaml.load("C:/Users/selva/work/code/python-utility/fileGenerator/schemas/test.yml", Loader=yaml.FullLoader)