#Write a python code to copy content of one file to another file.?
with open("file1.txt", 'r') as source:
        with open("destination_file", 'w') as destination:
            for line in source:
                destination.write(line)