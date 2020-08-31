import json
from pprint import pprint
from jinja2 import Environment, FileSystemLoader
def config_file():
    ENV = Environment(loader=FileSystemLoader('.') )
    i_file=input("Enter the name for info file (file to upload): ")
    c_file=input("Enter the name for configuration file ( file_name.txt) (this file will be created) : ")

    inf_file=i_file+".txt"
    conf_file=c_file+".txt"

    with open(inf_file, 'r') as g:
       prac=json.load(g)
       interfaces = prac
      

    template = ENV.get_template("template.j2")
    output = template.render(devices=interfaces)
    print (output)

    with open(conf_file, 'w') as f:
        f.writelines(output)
    print("File successfuly created "'\n'
            "---------------------------"'\n')