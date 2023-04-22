from cnocr import CnOcr
# img = 'C:/Users/Allen/Pictures/test.jpg'
# ocr = CnOcr()  # 所有参数都使用默认值


if __name__ == '__main__':
    out = ocr.ocr(img)
    for thing in out:
        print(thing['text'], end='')
