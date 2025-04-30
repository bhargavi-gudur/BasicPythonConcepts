f = open('output.txt', 'w')
f.write('Hello, World!\n')
f.write('This is a test file.\n')
f.write('Goodbye!\n')
f.close()
f = open('output.txt', 'r')
print(f.read())
f.close()
f = open('text.txt', 'a')
f.write('This is an appended line.\n')
f.close()
f = open('text.txt', 'r')
print(f.read())
f.close()
# To copy a file in Python
readfile= open("output.txt","r")
writefile =open("copy.txt","w")
for lines in readfile:
    writefile.write(lines)
readfile.close()
writefile.close()

# To check if the file is copied successfully
check_read = open("copy.txt","r")
check_read = open("copy.txt", "a+")

check_read.write("This is a new line added to the copied file.\n")
print(check_read.read()) 
check_read.close()    