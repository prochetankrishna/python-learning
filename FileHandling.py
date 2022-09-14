# Step 1 : Open a file to read
file_to_be_read = open("some-file.txt")

# Step 2: Create a file in which data needs to be written
file_to_be_written_to = open("file-write.txt", 'w')

# Step 3 : Read from file and Write to another file
for each_line in file_to_be_read:
    file_to_be_written_to.writelines(each_line)

# Step 4 : Close the objects
file_to_be_read.close()
file_to_be_written_to.close()
