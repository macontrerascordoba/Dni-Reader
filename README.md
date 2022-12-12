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

- Si quieres ejecutar desde el .exe necesitas:
    - Tesseract: [Como installar Tesseract en Windows](https://parzibyte.me/blog/2019/05/11/instalar-tesseract-ocr-windows-10/#Descargar_Tesseract_OCR)
  
- Si quieres ejecutar el archivo .py además de Tesseract necesitarias los siguientes modulos de python:
    - PIL: `pip3 install pillow`
    - pytesseract: `pip3 install pytesseract`
    - Tkinter: `pip3 install tk`


### Uso


1. Descarga y ejecuta el archivo "DniReader.exe o clona el repositorio y ejecuta el codigo con `python3 DniReader.py`.
2. Busca y selecciona la image del DNI.
3. Selecciona donde quieres guardar el resultado y el nombre del fichero.
4. El programa guardará el DNI en el fichero indicado.

---

## **English**

### Description

This program analyzes an image of the reverse of a spanish DNI and extract the DNI number from it.  

It works by extracting all the text from the image, look for the line that starts with IDESP, because this is the line that contains the ID number and always starts with IDESP, and read from the end, escaping the '<', the first 9 caracters. Then it flip this nine caracters to print them in the correct order and thats the DNI.


### Requeriments

- If you want to execute form the .exe you will need:
    - Tesseract: [How to install in Windows](https://linuxhint.com/install-tesseract-windows/)

- If you want to execute from the .py file, you will also need the following python modules:
    - PIL: `pip3 install pillow`
    - pytesseract: `pip3 install pytesseract`
    - Tkinter: `pip3 install tk`


### Usage

1. Download and execute the file "DniReader.exe" or clone the repository and execute the code with `python3 DniReader.py`.
2. Search and select the DNI image.
3. Select where do you want to save the result and the file name.
4. The program will save the DNI on the especified file.