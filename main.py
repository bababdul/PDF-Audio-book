#By: Abdulganiyu Babatunde, bababdulg@gmail.com, 6474505223
#Date created: 1/27/2024
#Date last modified: 1/27/2024

import pyttsx3 #imports python text to speech
import PyPDF2   #imports pdf reader
from tkinter.filedialog import * 

pdfname = askopenfilename() # Opens filedirectory and prompts user to select a pdf file, otherwise an error occurs
with open(pdfname, 'rb') as pdfname: # Opens the file in binary
    pdfreader = PyPDF2.PdfReader(pdfname) # Variable assigned to reading the pdf
    pagenum = len(pdfreader.pages) 

    for i in range(0, pagenum):
        text = pdfreader.pages[i].extract_text() # Extracts the text from the selected page
        print("Text from the page:\n", text)
        reader = pyttsx3.init() 
        reader.say(text) # Says the text on selected page
        reader.say("Next page")
        reader.runAndWait()
        
