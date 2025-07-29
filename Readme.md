# Python :
- Dynamic 
- object-oriented programming as well as functional programming .
- case sensitive language 
- portable
- Python name inspired by british comedy group "Monty Python".
- 0-based indexing

### [Working of python](./images/1000221207.jpg)
[![](https://mermaid.ink/img/pako:eNp1UU1PwzAM_StWzlHVrZu05oZACCQKExUTh16yxmsDbTK5rlA17b-TUpVxYDnFfh928k6i9AaFEh--J4dD4SActtwgPNiOPQ3gD7AduPZuAjss2XoHj47Jm75EA_sBdjfP8PqS52_ZxAJYpJtUrZWc63tLHcMOqRvVizRdqGRGZ8_tUPMIRvGsyvRRwsE2jCThSbdGg1opCZcp6Uol0fqK0zJ6n5m3vj0S1ujG-Z2EStNeVwilb5pJpNbRn31zy2D8lwtbwv_mycV8Gceb8FiQQooWqdXWhE89jXAhuMYWC6HC1Wj6LEThzoGne_b54EqhmHqUgnxf1UIddNOFqj8azXhndUW6_e2isSGTbMrsJ7rzN9ssilY?type=png)](https://mermaid.live/edit#pako:eNp1UU1PwzAM_StWzlHVrZu05oZACCQKExUTh16yxmsDbTK5rlA17b-TUpVxYDnFfh928k6i9AaFEh--J4dD4SActtwgPNiOPQ3gD7AduPZuAjss2XoHj47Jm75EA_sBdjfP8PqS52_ZxAJYpJtUrZWc63tLHcMOqRvVizRdqGRGZ8_tUPMIRvGsyvRRwsE2jCThSbdGg1opCZcp6Uol0fqK0zJ6n5m3vj0S1ujG-Z2EStNeVwilb5pJpNbRn31zy2D8lwtbwv_mycV8Gceb8FiQQooWqdXWhE89jXAhuMYWC6HC1Wj6LEThzoGne_b54EqhmHqUgnxf1UIddNOFqj8azXhndUW6_e2isSGTbMrsJ7rzN9ssilY)

## Virtual Environments : 
A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts.

```python
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment (Linux/macOS)
source myenv/bin/activate

# Activate the virtual environment (Windows)
source myenv/Scripts/activate

# Deactivate the virtual environment
deactivate

# use the kernel set up
ipython kernel install /-/-user /-/-name=projectname
```
## Requirement.txt File : 
This file consists of packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment.
```python
# Output the list of installed packages and their versions to a file
pip freeze > requirements.txt

# Install the packages listed in the requirements.txt file
pip install -r requirements.txt
```
### Some imp. Points 
- Single Line Comments by  # 
- Multi Line comments by triple quotes either  ''' ''' or """ """ 
- Single and double quotes are used for single line strings whereas triple quotes are used for multi line strings .
- To print apostrophe we have to use different quote to complete the string or use escape sequence character ' \ ' .

## Inendation in Python : 
- Python uses indentation (spaces or tabs) to define blocks of code.
- Python is sensitive to whitespace. 
- Ensure consistent indentation to avoid errors. Ideally, use 4 spaces for indentation
```python
if 5>2 :
    print("True")
# Spaces before print are called indentation
```

- ### [Variables and Data Types in Python](variable.ipynb)

## Taking user Input : 
- The  input()  function allows you to take user input from the keyboard.
- By default,  input()  returns a string. You can convert it to other data types as
needed. e.g. : [main](main.ipynb)
- separator sep and end in print function 

## Escape Sequence Characters : 
- Escape sequences are used to include special characters in strings.
- Common escape sequences:
1. \n : Newline
2. \t : Tab
3. \\\ : Backslash
4. \\" : Double quote
5. \\' : Single quote

## \_\_pychache__ file :
When a Python module is imported, Python compiles its source code (.py file) into bytecode. This bytecode is a lower-level, platform-independent representation of the code that can be executed more efficiently by the Python interpreter. Storing this compiled bytecode in \_\_pycache__ avoids the need to recompile the module every time it's imported, leading to faster program execution, especially in larger projects.
- In working .pyc file 

# Introspection of class : 
```python 
print(dir(e))
# e : object of class 
```

## [Operators in python](operators.ipynb)
## [Conditional Statements](conditional.ipynb)
## [Loops in python](Loops.ipynb)
## [Strings in Python](strings.ipynb)
## [Functions in Python](functions.ipynb)
## [Modules & pip in Python](modules.ipynb)
## [Lists in Python](List.ipynb)
## [Tuples in Python](Tuples.ipynb)
## [Sets in Python](Sets.ipynb)
## [Dictionaries in Python](Dictionaries.ipynb)
## [OOPS in Python](./OOPS)


