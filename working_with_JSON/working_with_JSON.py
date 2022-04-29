# Python’s json module handles all the details of translating between a string with JSON data and Python values for the json.loads() and json.dumps() functions. JSON can’t store every kind of Python value. It can contain values of only the following data types: strings, integers, floats, Booleans, lists, dictionaries, and NoneType. JSON cannot represent Python-specific objects, such as File objects, CSV reader or writer objects, Regex objects, or Selenium WebElement objects.

import json
# After you import the json module, you can call loads() and pass it a string of JSON data. Note that JSON strings always use double quotes. It will return that data as a Python dictionary. Python dictionaries are not ordered, so the key-value pairs may appear in a different order when you print jsonDataAsPythonValue.


# Reading JSON with the loads() Function
# To translate a string containing JSON data into a Python value, pass it to the json.loads() function. (The name means “load string,” not “loads.”)
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
# {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
print('JSON as Python values:')
print(jsonDataAsPythonValue)

print()
# Writing JSON with the dumps() Function
# The json.dumps() function(which means “dump string, ” not “dumps”) will translate a Python value into a string of JSON-formatted data. Enter the following into the interactive shell:
pythonValue = {'isCat': True, 'miceCaught': 0,
               'name': 'Zophie', 'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
# '{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'
print('JSON as string:')
print(stringOfJsonData)
