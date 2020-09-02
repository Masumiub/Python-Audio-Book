import pyttsx3
import PyPDF2

book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

dst = pyttsx3.init()
for num in range(7, 8): # till the last; use "pages"
    page = pdfReader.getPage(num)
    text = page.extractText()
    dst.say(text)
    dst.runAndWait()
