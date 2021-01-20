'''
    Requirement:
                pikepdf
                tkinter
'''
import pikepdf, tkinter, os
from tkinter import filedialog
from pathlib import Path
print(' ***** NOTICE: MAKE SURE THAT THIS WINDOW IS ACTIVE BEFORE PRESSING ENTER *****')

input("\n Let's select your PDF file!\n Press Enter :-)")
root = tkinter.Tk()
root.withdraw()
filename = filedialog.askopenfilename(title="Please select the PDF file", filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
dir = Path(filename)
dir = dir.parent

pdf = '.pdf'
if filename.endswith(pdf):

    global destDir
    NewFile = filename.replace(pdf, ' [Unlocked].pdf')
    Password = input('\n Please input the password. In case of open password protected PDF files, press Enter\n')
    print("\n\n Please wait. I'm decrypting your file....\n This might take a few tiny seconds...")
    pdf = pikepdf.open(filename, password=Password)
    pdf.save(NewFile)
    pdf.close()
    NewFile = Path(NewFile)
    destDir = NewFile.parent
    NewFile = NewFile.name
    print('\n\n Yay! I have decrypted "' + filename + '"' + ' successfully ;-)')
    print(f" Your decrypted PDF has been saved as \"{NewFile}\" in the same folder.\n\n See ya later!\n\n Program ended.\n ****************")
else:
    print('\n\n This is not a PDF file :-(\n Program ended.\n ****************')


input('\n\n Press Enter to exit the program and open the folder :-]')
os.startfile(destDir)
