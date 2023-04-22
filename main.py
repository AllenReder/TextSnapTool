from cnocr import CnOcr
from grab_img import grabImage


# img = 'C:/Users/Allen/Pictures/test.jpg'
ocr = CnOcr()  # 所有参数都使用默认值


if __name__ == '__main__':
    img = grabImage()
    img.save("screenshot.png")
    out = ocr.ocr(img)
    for thing in out:
        print(thing['text'], end='')
