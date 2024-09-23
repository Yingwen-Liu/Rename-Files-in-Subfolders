import os
import json


def replace(directory, string, replace_string):
    # Walk through all subdirectories and files
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if string in filename:
                new_filename = filename.replace(string, replace_string)
                
                # Get the full path of the current and new file
                old_file = os.path.join(foldername, filename)
                new_file = os.path.join(foldername, new_filename)
                
                # Rename the file
                os.rename(old_file, new_file)
                print(f'Renamed: {old_file} -> {new_file}')


def add(directory, string, pos):
    # Check if pos is an integer
    try:
        int(pos)
    except ValueError:
        print(f'Error: Position "{pos}" is not an integer.')
        return
    
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            # Ensure pos is within the bounds of the filename
            if pos > len(filename):
                print(f'Error: Position {pos} is out of bounds for filename "{filename}".')
                continue
                        
            new_filename = filename[:pos] + string + filename[pos:]
                
            # Rename the file
            old_file = os.path.join(foldername, filename)
            new_file = os.path.join(foldername, new_filename)
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} -> {new_file}')


def main():
    # Load config
    with open('config.json', 'r') as file:
        config = json.load(file)
    
    mode = config['mode'].strip().lower()
    
    if mode in ['replace', 'r']:
        # Replace: replace the string in the filename with a given string
        replace(config['root_directory'], config['string'], config['replace_string'])
    elif mode in ['add', 'a']:
        # Add: insert the string in the filename at a given position
        add(config['root_directory'], config['string'], config['position'])
    else:
        raise Exception('The given mode does not exist.')
    
    print('>>> All Done! <<<')


if __name__ == '__main__':
    main()