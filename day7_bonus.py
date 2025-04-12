filenames = ["1.doc","2.report","3.presentation"]
#we want to change the above list to
#filenames = ["1-doc.txt","2-report.txt","3-presentation.txt"]

filenames = [filename.replace(".","-") + '.txt' for filename in filenames]
print(filenames)

#the above is called list comprehension.