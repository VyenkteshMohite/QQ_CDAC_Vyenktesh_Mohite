import PyPDF2
from googletrans import Translator
import csv

def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extractText()
        return text

def translate_text(text):
    translator = Translator()
    translated_text = translator.translate(text, src='mr', dest='en')
    return translated_text.text

def save_to_csv(translated_text, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in translated_text:
            csv_writer.writerow(row)

def main():
    pdf_file = '3963 - गहाणखत.pdf'
    output_file = 'translated_text.csv'
    extracted_text = extract_text_from_pdf(pdf_file)
    lines = extracted_text.split('\n')
    rows_to_translate = [lines[3], lines[6], lines[7]]  # Rows 4, 7, and 8
    translated_text = []
    for row in rows_to_translate:
        translated_row = translate_text(row)
        translated_text.append([translated_row])
    save_to_csv(translated_text, output_file)
    print("Translation complete. Saved as", output_file)

if __name__ == "_main_":
    main()