# Importing required modules
import PyPDF2
from unidecode import unidecode

# Creating a pdf file object
pdfFileObj = open(
    '/Volumes/MobileDev/learning/python/Naushad Nizar Ali.pdf', 'rb')

# Creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Getting number of pages in pdf file
pages = len(pdfReader.pages)

# Loop for reading all the Pages
for i in range(pages):

    # Creating a page object
    pageObj = pdfReader.pages[i]

    # Printing Page Number
    print("Page No: ", i)

    # Extracting text from page
    # And splitting it into chunks of lines
    text = pageObj.extract_text().split("  ")

    # Finally the lines are stored into list
    # For iterating over list a loop is used
    for i in range(len(text)):

        # Printing the line
        # Lines are seprated using "\n"
        plain_text = unidecode(text[i])

        print(plain_text, end="\n")

    # For Seprating the Pages
    print()

# closing the pdf file object
pdfFileObj.close()
