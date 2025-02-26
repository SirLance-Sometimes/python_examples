'''
This is what I thought they were trying to explain in the slides. You can see below that var1 was created outside 
of the function, and it is a global variable. Inside the function, we created a new variable var1 that is local to the function.
The global variable var1 is still accessible inside the function using the globals() function.
When var1 is accessed in the function without the globals() function, it will refer to the local variable.
The global variable var1 is not affected by the local variable var1.

You can run this with the command python var_scope.py

'''

# This is a global variable
var1 = "a value"

def func1():
    var1 = "a different value"
    print("func1 var1 local: " + var1)  # This will print "a different value" because of the local scope
    print("func1 var1 global: " + globals()["var1"])  # This will print "a value" because of the global scope
    globals()["var2"] = "a new value"  # This will create a new global variable var2

if __name__ == "__main__":
    print("before the function var1: " + var1)  # This will print "a value" because of the global scope
    func1()
    print("after the function var1: " + var1)  # This will still print "a value" because the global variable is unchanged
    print("after the function var2: " + var2)  # This will print a new value because var2 was created in the function using the globals() function. Note this is uncommon and even my IDE is trying to tell me this variable is undefined despite the code working. I never do this.