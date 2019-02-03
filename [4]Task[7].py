import os

def sed(pattern, replacement, file1, file2):
    # Open File1
    file1_content = open(file1)

    # Write Contents to File2
    file2_content = open(file2, 'w')

    # Search and replace string
    for line in file1_content:
        if pattern in line:
            print('pattern exist')
            replaced = line.replace(pattern, replacement)
            file2_content.write(replaced)
        else:
            file2_content.write(line)

print(os.getcwd())
pattern = 'I'
replacement = 'Me'
file1 = ''
file2 = ''
sed(pattern, replacement, file1, file2)
