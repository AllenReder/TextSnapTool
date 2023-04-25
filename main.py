from cnocr import CnOcr
import tkinter as tk
from gui import Application


# img = 'C:/Users/Allen/Pictures/test.jpg'


if __name__ == '__main__':

    # 创建 gui 窗口
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
