                                   # Task 1: Read a File and Handle Errors
try:
  file =  open("sample.txt", "r")
  file_read = file.read()
  print("reading file content: \n", file_read)
  file.close()
except FileNotFoundError:
  print("Error: File not found.")

 # first  output
 # reading file content:
 # line 1 :  this is a simple text file.
 # line 2 :  it contains multiple lines.

try:
      file = open("samle.txt", "r")
      file_read = file.read()
      print("reading file content: \n", file_read)
      file.close()
except FileNotFoundError:
      print(" \n Error: File not found.")

 # second output
 # Error: File not found.