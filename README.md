# Spanish DNI number reader

## Index
1. [Español](#español)
    1. [Descripcion](#descripcion)
    2. [Requerimientos](#requerimientos)
    3. [Uso](#uso)
2. [English](#english)
    1. [Description](#description)
    2. [Requeriments](#requeriments)
    3. [Usage](#usage)

---

## **Español**

### Descripcion

Este programa analiza una imagen del reverso de un DNI español y extrae el number del DNI.  

La forma en la que lo hace es extrayendo todo el texto de la imagen, busca la linea que empieza por IDESP, ya que esta es la linea que contiene el numero del DNI y siempre empieza por IDESP, y lee desde el final, saltandose los '<' los 9 primeros caracteres. Después les da la vuelta a estos 9 caracteres para imprimirlos en el orden correcto y ese sería el DNI.


### Requerimientos

- Tesseract: [Como installar Tesseract en Windows](https://parzibyte.me/blog/2019/05/11/instalar-tesseract-ocr-windows-10/#Descargar_Tesseract_OCR)
- Librerias de Python: (En linea de comandos)
    - PIL: `pip3 install pillow`
    - pytesseract: `pip3 install pytesseract`


### Uso

1. Pon la imagen del reverso del DNI dentro de la carpeta "public" con el nombre dni.jpg
2. Abre la terminal en la carpeta Dni-Reader.
3. Ejecuta el siguiente comando: `python3 main.py`
4. El programa devolverá el numbero del DNI por consola, asi como en un fichero llamado dni.txt dentro de la carpeta public para que luego pueda ser usado por otros programas.

---

## **English**

### Description

This program analyzes an image of the reverse of a spanish DNI and extract the DNI number from it.  

It works by extracting all the text from the image, look for the line that starts with IDESP, because this is the line that contains the ID number and always starts with IDESP, and read from the end, escaping the '<', the first 9 caracters. Then it flip this nine caracters to print them in the correct order and thats the DNI.


### Requeriments

- Tesseract: [How to install in Windows](https://parzibyte.me/blog/2019/05/11/instalar-tesseract-ocr-windows-10/#Descargar_Tesseract_OCR)
- Python libraries: (In Command Line)
    - PIL: `pip3 install pillow`
    - pytesseract: `pip3 install pytesseract`


### Usage

1. Put the dni's reverse's image inside the "public" directory with the name dni.jpg.
2. Open a terminal in the Dni-Reader directory.
3. Run this command: `python3 main.py`
4. The program will output the DNI number in console as well as in a the file call dni.txt so it can letter be used by other programs