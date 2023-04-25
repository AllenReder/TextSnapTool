from cnocr import CnOcr
import pyperclip

ocr = CnOcr()  # 所有参数都使用默认值

def ocrText(img):
    out = ocr.ocr(img)
    text = ''
    for thing in out:
        print(thing['text'])
        text = text + '\n' + thing['text']
    pyperclip.copy(text)
    return text