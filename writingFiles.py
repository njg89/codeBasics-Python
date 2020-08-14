# There are two methods for saving data to a file: Write and Append
# Write will overwrite original contents
# Append will add new data to the previous data

writeMe = 'Example text to save to a file.....we shall see if this appends"

saveFile = open('python-writeFileSample.txt','a')
saveFile.write(writeMe)
saveFile.close()