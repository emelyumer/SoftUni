def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


data = {'name': 'Georgi', 'town': 'Sofia', 'age': '33'}
result = get_info(**data)
print(result)