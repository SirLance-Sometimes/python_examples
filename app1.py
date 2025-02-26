'''
Try running this app with the command: python app1.py
Then go and try running app2.py with the command: python app2.py
'''

# This is a function, by itself it does nothing. It is just a function definition.
def hello():
    print("Hello from app1!")

# This condition checks if the program is being run directly or imported as a module.
# If it is run directly, it will execute the hello function.
# If it is imported, it will not execute the hello function.
if __name__ == "__main__":
    print("I, app1, was run and not imported")
    hello()