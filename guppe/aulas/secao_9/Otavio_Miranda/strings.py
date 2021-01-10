string = 'Wesley Lucas'
new_string =[
    string[index: index + 2] 
    for index in range(0, len(string), 2)]
print(new_string)
