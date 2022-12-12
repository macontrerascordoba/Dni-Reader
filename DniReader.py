import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Initialize Tkinter
root = tk.Tk()
root.withdraw()

# Ask user for the image
imagePath = filedialog.askopenfilename(title='Choose the DNI Image', filetype=[('JPG', '*.jpg'), ('PNG', '*.png')])

# Extract the text from image using Tesseract and saves it in an array line by line 
text = pytesseract.image_to_string(Image.open(imagePath))
textArr = text.split("\n")

toCompare = 'IDESP'
equals = True
dniNumberLine = ""

# Looks in the array for the line that stars with IDESP
for line in textArr:
    equals = True
    for i in range(5):
        if len(line) < 4 or line[i] != toCompare[i]:
            equals = False
            break

    if equals == True:
        dniNumberLine = line
        break;

# Goes to the end of the Dni by reading the line from the end and skiping the '<'
i = 0
while dniNumberLine[::-1][i] == '<':
    i += 1

spaces = i
reversedDniNumber = ''
dniNumber = ''

# Read the DNI but from end to start
while i-spaces < 9:
    reversedDniNumber += dniNumberLine[::-1][i]
    i += 1

# Reverses the readed DNI to save it in the correct orientation
for i in range(len(reversedDniNumber)):
    dniNumber += reversedDniNumber[::-1][i]

# Ask the user where to save the file and saves it
savePath = filedialog.asksaveasfilename(title='Choose where you want to save the DNI number', initialdir='.', initialfile='dni.txt', filetypes=[('txt', '*.txt')],defaultextension='.txt')
f = open(savePath, 'w')
f.write(dniNumber)
f.close()