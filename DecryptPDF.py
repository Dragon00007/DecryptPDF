'''
    Requirement:
                pip install pikepdf
'''
import pikepdf

file = input('Please enter the fullPath of the PDF file.\n')
pdf = '.pdf'

if file.endswith(pdf):
    NewFile = file.replace(pdf, ' [Unlocked].pdf')
    Password = input('please input the password.\nIn case of open password protected PDF files press Enter:\n')
    pdf = pikepdf.open(file, password=Password)
    pdf.save(NewFile)
    print('"' + file + '"' + ' has been decrypted successfully.')
else:
    print('This is not a PDF file.')
print("Program ended.\n****************")
