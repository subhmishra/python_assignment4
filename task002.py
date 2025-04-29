                              # Task 2: Write and Append Data to a File
#writing
file = open("output.txt", "w")
user_value1 = input("enter text to  write to the file: ")
file.write(user_value1 +"\n")
print("data succesfully written to output .txt \n")
file.close()

#appending
file = open("output.txt", "a")
user_value2 = input(" enter additional text to appened: ")
file.write(user_value2)
print("data succesfully appended \n")
file.close()

# final reading the file
file = open("output.txt", "r")
file1 = file.read()
print("final content of output.txt :\n",file1)


#output
# #enter text to  write to the file: hello, shubham
# data succesfully written to output .txt
#
#  enter additional text to appened: welcome to the world of python
# data succesfully appended
#
# final content of output.txt :
#  hello, shubham
# welcome to the world of python