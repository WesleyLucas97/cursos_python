names = ['luiz', 'miranda', 'helena', 'joana', 'felipe']
new_names = [name[::-1].title()[::-1] for name in names]
new_names_2 = [f'{name[:-1].lower()}{name[-1].upper()}' for name in names]

print(new_names)
print(new_names_2)