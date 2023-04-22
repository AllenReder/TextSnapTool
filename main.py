from cnocr import CnOcr
from grab_img import grabImage
import pyperclip


# img = 'C:/Users/Allen/Pictures/test.jpg'
ocr = CnOcr()  # 所有参数都使用默认值


if __name__ == '__main__':
    img = grabImage()
    img.save("screenshot.png")
    out = ocr.ocr(img)
    text = ''
    for thing in out:
        print(thing['text'])
        text = text + '\n' + thing['text']
    pyperclip.copy(text)
