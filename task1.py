#Read a File and Handle Errors 

#Try opening the file in read mode
try:
    f = open("sample.txt")
#Raise File Not Found Error if the file is not found    
except FileNotFoundError:
    print("Error: The file sample.txt was not found.")
#Read File content and close the file
else:
    print("Reading file content: ")
    # Strip to remove extra newline
    print("Line 1:", f.readline().strip())  
    print("Line 2:", f.readline().strip())
    f.close()
