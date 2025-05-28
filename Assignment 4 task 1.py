# Read a file and Handle Errors
try:
    file2 = open("sample.txt", "r")
    reading_file = file2.read()
    print(reading_file)
    file2.close()
except FileNotFoundError:
    print("The file 'sample.txt' was not found")