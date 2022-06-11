from os.path import exists
from os import remove

while True:
    line = input().split('-')
    if line[0] == 'End':
        break
    command_parts = line
    command, file_name = command_parts[0], command_parts[1]

    if command == 'Create':
        with open(f'./{file_name}', 'w') as file:
            pass
    elif command == 'Add':
        content = command_parts[2]
        with open(f'./{file_name}', 'a') as file:
            file.write(content + '\n')
    elif command == 'Replace':
        if not exists(f'./{file_name}'):
            print('An error occurred.')
            continue
        old_string, new_string = command_parts[2], command_parts[3]
        with open(f'./{file_name}', 'r+') as file:
            file_content = file.read().replace(old_string, new_string)
            file.seek(0)
            # seek() vrushta pointera v nachaloto
            file.truncate()
            # truncate() zachistva faila
            file.write(file_content)

    else:
        if not exists(f'./{file_name}'):
            print('An error occurred.')
            continue
        remove(f'./{file_name}')
    line = input()
