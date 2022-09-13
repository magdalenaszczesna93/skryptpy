with open("names.txt", 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)

new_name = "Luke\n"
with open("names.txt", 'a') as write_file:
    write_file.write(new_name)

new_name = "Luke"
with open("new_names.txt", 'w') as write_file:
    write_file.write(new_name)