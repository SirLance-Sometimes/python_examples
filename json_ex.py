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
# we can also print out an individual value from the data by putting the name of a key between the brackets. We do this statically below using quotes but this can be access via a variable if the variable contains a valid key.
print(data['name'])

# Another way of getting a value from a dictionary is using <dictionary>.get(<key>)
print(data.get('role')) # The advantage of getting the value this way is that if the key does not exist, it will return None instead of throwing an error. This is useful if you are not sure if the key exists in the dictionary.

# example of dump writing to a file
with open('output.json', 'w') as file:
    json.dump(data, file, indent=3)