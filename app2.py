# This is an import statement. It imports the app1 module which makes the functions defined in app one available in this module.
import app1

# This condition checks if the program is being run directly or imported as a module.
# If it is run directly, it will execute the code below, which include the hello function from app1.
# If it is imported, it will not do anything.
if __name__ == "__main__":
    print("I, app2, was run and not imported")
    app1.hello()
    print("Hello from app2!")
    print("app2 __name__:", __name__)
    print("app1 __name__:", app1.__name__)