import json

# reading data from a file with load
with open('example.json', 'r') as file:
    data = json.load(file)

# reading data from a string with loads
with open('example.json', 'r') as file:
    string_data = file.read()
    data2 = json.loads(string_data)

# example of dumps showing string output
print(json.dumps(data, indent=3))
print(json.dumps(data2, indent=3))

# example of dump writing to a file
with open('output.json', 'w') as file:
    json.dump(data, file, indent=3)