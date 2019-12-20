import yaml

with open('my-yaml.yaml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

print(data)