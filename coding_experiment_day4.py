filenames = ['1.Reports.txt','2.Presentation.txt','3.RawData.txt']
print(filenames)
for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)