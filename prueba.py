import pytesseract
from PIL import Image

imageName = 'dni.jpg'
imagePath = 'public/' + imageName
text = pytesseract.image_to_string(Image.open(imagePath))
textArr = text.split("\n")

print(textArr)

toCompare = 'IDESP'
equals = True
dniNumberLine = ""

for line in textArr:
    equals = True
    for i in range(5):
        if len(line) < 4 or line[i] != toCompare[i]:
            equals = False
            break

    if equals == True:
        dniNumberLine = line
        break;

i = 0
while dniNumberLine[::-1][i] == '<':
    i += 1

spaces = i
reversedDniNumber = ''
dniNumber = ''

while i-spaces < 9:
    reversedDniNumber += dniNumberLine[::-1][i]
    i += 1

for i in range(len(reversedDniNumber)):
    dniNumber += reversedDniNumber[::-1][i]

print(dniNumber)

f = open('public/dni.txt', 'w')
f.write(dniNumber)
f.close()