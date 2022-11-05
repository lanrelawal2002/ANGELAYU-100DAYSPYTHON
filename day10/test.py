
"""For user functions you can rename and use the new variable as a
python expression"""
def combine(name1, name2):
    return f"Please vote {name1} {name2}"

function_name = combine
function_rename = function_name

print(function_rename("Joyce", "Myer"))


"""For built-in functions you can't rename and use new variable as
a python expression"""
# len("matter")
# new_length = len
# value = new_length
# print(value)