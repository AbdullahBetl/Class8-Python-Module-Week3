original_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
                 {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
                 {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_list = sorted(original_list, key=lambda x: x['make'])

print("Sorted List of dictionaries:")
for item in sorted_list:
    print(item)
