# Absolute file path
# Relative file path = ./talk.ppt = current file we are in

# with open("my_file.txt") as file: # no need to close the files
#   contents =  file.read()
#   print(contents)

# with open("my_file_w.txt", mode="a") as file: # no need to close the files
#   file.write("New text")
  
with open("/Users/thandekazulu/Desktop/my_file.txt") as file: # a = append
  contents = file.read()
  print(contents)