from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint

def pdf_to_mp3(file_path='test.pdf',language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix =='pdf':

       print(f'[+] Original file:{Path(file_path).name}')
       print('[+] Processing...')


       with pdfplumber.PDF(open(file=file_path,mode='rb')) as pdf:
           pages = [page.extract_text() for page in pdf.pages]#page.extract извлекаем текст с каждойц страницы
       text = ''.join(pages)
       text.replace('\n',' ')

       my_audio =  gTTS(text=text,lang= language,slow=False)
       file_name = Path(file_path).stem#возвращает последний элемент пути к файлу без расширения
       my_audio.save(f'{file_name}.mp3')

       return f'[+] {file_name}.mp3 saved successfully!\n---Have a good day!---'
    else:
        return 'File not exist'

def main():
    tprint('PDF>>>TO>>>MP3',font='bulbhead')
    file_path = input(("\n Enter a file path: "))
    language = input(("Choose language"))
    print(pdf_to_mp3(file_path=file_path,language=language))

if __name__ == '__main__':
    main()