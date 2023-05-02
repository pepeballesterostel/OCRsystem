# OCRsystem
Translate a picture database of a book into the language of prefernce. I use [Tesseract Open Source OCR Engine](https://github.com/tesseract-ocr/tesseract), together with 
the [Google translato API](https://pypi.org/project/googletrans/) to first recognize text from pictures and then translating into a target language. 

## Installation

You'll need to [install](https://tesseract-ocr.github.io/tessdoc/Installation.html)  the **Tesseract** engine in your system. The code assumes that the program will be saved
in the standard directory: "C:\Program Files\Tesseract-OCR\tesseract.exe". If you saved the program in a different directory, just go to line 16 in main.py and change the path
to were the executable file of tesseract is located. 

Create a conda environment and download the requirements.

```
$ conda env create OCRsystem
$ conda activate OCRsystem
$ pip install -r requirements.txt
```

## Usage

Run the main.py python file indicating the path to the folder of book images, the language in which the book is written, and the target language to translate the text (if not 
secified, the text will be generated in the original language). Optionally, you can specify the name of the output word document where the translated text is saved (if
not specified, a word document called "extracted_text.docx" will be created). 

Here is a hint on how to use the system:

```
usage: main.py [-h] [-d DATABASE] [-l LANGUAGE] [-tl TARGET_LANG] [-o OUTPUT]

Extract text from book images

options:
  -h, --help            show this help message and exit
  -d DATABASE, --database DATABASE
                        Path to the book image database
  -l LANGUAGE, --language LANGUAGE
                        Language of the book text (e.g. "deu" for German, "ita" for Italian). Take into account that the data for each language must be downloaded from https://github.com/tesseract-ocr/tessdata
  -tl TARGET_LANG, --target_lang TARGET_LANG
                        Language to translate text to (e.g. "en" for English, "es" for Spanish). If not specified, the text will not be translated.
  -o OUTPUT, --output OUTPUT
                        Path to the output Word document
 ```
 
 ## Example

In this example I use images from the folder Schone to translate a German text into English:
```
python main.py -d Schone -l deu -tl en
```
