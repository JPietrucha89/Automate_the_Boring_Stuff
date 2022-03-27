#Say you have a list value like this:
#spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space,
#  with and inserted before the last item. For example, passing the previous spam list to the function would return
#  'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.

def string_comma(listParameter):
    string=""
    for i in range(len(listParameter)-1):
        string=string+listParameter[i]+', '
    
    string=string+"and "+listParameter[-1]
    return string

#main
spam = ['apples', 'bananas', 'tofu', 'cats', 'kapcie']
print(string_comma(spam))