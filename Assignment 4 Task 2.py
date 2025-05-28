#write and append data to a file
user = input("Enter text to write to the file: ")
file = open("output.txt","w")
writing_file = file.write(user)
print("Data successfully written to output.txt.")
file.close()

file = open("output.txt","a")
append_file = file.write("\nLearning file handling in python.")
print("Data successfully appended.")
file.close()

file = open("output.txt","r")
content = file.read()
print("Final content of output.txt:\n"+content)
file.close()