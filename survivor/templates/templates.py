from jinja2 import FileSystemLoader, Environment

keys   = []
values = []
with open('./.env', 'r') as in_file:  # read environment variable files
    config = in_file.read().splitlines()
    for line in config:  # for each line append the config key to the keys list and the value to the values list
        config = line.split('=')
        keys.append(config[0])
        values.append(str(config[1]))

file_loader = FileSystemLoader('./')  # load the current directory
env = Environment(loader=file_loader)

template = env.get_template('secrets.yml.j2')  # get the secrets.yml.j2 as the template for creating the kubernetes secrets manifest
output   = template.render(keys=keys, values=values, length=len(keys))  # render the template and store the rendered file as variable


with open('/tmp/out/kubernetes-secrets.yml', 'w+') as out_file:  # write the output to a file
    out_file.write(output)
