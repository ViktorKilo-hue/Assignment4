#Write and Append Data to a File

#Prompt user to enter text and write it to the file 

try:
    textInput = input("Enter text to write to the file: ")
except Exception as e:
    print("An error occured while trying to write data!")
else:
    f = open("output.txt","w")
    f.write(textInput)
    f.close()
    print("Data successfully written to output.txt")


#Prompt user to append any text to the file
while True:
    choice = input("Do you want to add more data to the file?(Y/N): ").strip().lower()
    if choice == 'n':
        break
    elif choice == 'y':
        addInfo = input("Enter additional text to append: ").strip()
        f1 = open("output.txt","a")
        f1.write("\n"+addInfo)
        f1.close()
        print("Data successfully appended.")
    else:
        break

#Read the contents of the file
try:
    f2 = open("output.txt","r")
    print("Final content of output.txt")
    print(f2.read())
    f2.close()
except Exception as e:
    print("An Error occured while reading the file.")