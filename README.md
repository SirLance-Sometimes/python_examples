# python_examples

## app1 and app2
These two go together to demonstrate two concepts, first the `if __name__ == "__main__":` code.  The second concept these files demonstrate is `import <module>` and the impacts import has on `__name__`.

Look over app1 first and run the file with `python app1.py` and note the results.

Then look over app2 and run the file with `python app2.py` and note the differences.

## var_scope
This file demonstrates the difference between variable scopes global and local.

Review the code and commends, then run the code with `python var_scope.py` and note how the print output changes for var1 depending on if it is called in the function vs outside the function.

## jason_ex
This example show examples of the differences between dump and dumps as well as load and loads.
This example takes data in from the provided example json file and will create a new json file.

## Extra tips
If you want to interact with these modules after they have run use the command `python -i <modulename.py>` this will run the code and leave you at an open shell so that you can run new commands in the shell. I suggest checking `dir()` to see all the variables in the global scope that are left over from the code you have run.  Anything you see as the output of `dir()` can be typed in with out the single quote which will show you the value associated with that variable name.

If you add a variable with say `x = 5` and then run `dir()` you should see x in the global list. Typing in `x` by its self after or `print(x)` will then show you the value.