import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import xlwt

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 500, bg = 'lightsteelblue3', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue3')
label1.config(font=('helvetica', 25))
canvas1.create_window(150, 60, window=label1)

label2 = tk.Label(root, text='FROM EXCEL TO CSV', bg = 'lightsteelblue3')
label2.config(font=('helvetica', 15))
canvas1.create_window(150, 90, window=label2)

def getExcel ():
    global read_file
    global fileText

    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_excel(import_file_path)
    
    fileText = tk.Label(root, text='File opened, now you can start a program', bg = 'lightsteelblue3')
    fileText.config(font=('helvetica', 10))
    canvas1.create_window(150, 450, window=fileText)

browseButtonCsv = tk.Button(text="      Import Excel File     ", command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButtonCsv)

def convertToCsv ():
    global read_file
    global fileText

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv (export_file_path, index = None)

    fileText.destroy()
    fileText = tk.Label(root, text=('File saved'), bg = 'lightsteelblue3')
    fileText.config(font=('helvetica', 15))
    canvas1.create_window(150, 450, window=fileText)

saveAsButtonCsv = tk.Button(text='Convert Excel to CSV', command=convertToCsv, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButtonCsv)

label3 = tk.Label(root, text='FROM CSV TO EXCEL', bg = 'lightsteelblue3')
label3.config(font=('helvetica', 15))
canvas1.create_window(150, 230, window=label3)

def getCsv ():
    global read_file
    global fileText

    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_csv(import_file_path)
    
    fileText = tk.Label(root, text='File opened, now you can start a program', bg = 'lightsteelblue3')
    fileText.config(font=('helvetica', 10))
    canvas1.create_window(150, 450, window=fileOpened)


browseButtonCsv = tk.Button(text="      Import CSV File     ", command=getCsv, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 270, window=browseButtonCsv)


def convertToExcel ():
    global read_file
    global fileText

    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    read_file.to_excel (export_file_path, index = None)
    
    fileText.destroy()
    fileText = tk.Label(root, text=('File saved'), bg = 'lightsteelblue3')
    fileText.config(font=('helvetica', 15))
    canvas1.create_window(150, 450, window=fileText)

saveAsButtonExcel = tk.Button(text='Convert CSV to Excel', command=convertToExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 320, window=saveAsButtonExcel)


def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 400, window=exitButton)

root.mainloop()