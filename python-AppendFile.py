appendMe = '\nMore sample text to APPEND to an existing file.'

saveFile = open('python-writeFileSample.txt','a')
saveFile.write(appendMe)
saveFile.close()