import tkinter as tk
from PIL import ImageGrab


def grabImage():
    # 截图矩形的起始坐标
    rect_start = None
    rect_end = None
    rect = None

    root = tk.Tk()
    root.attributes("-fullscreen", True) # 全屏
    root.attributes("-alpha", 0.2) # 透明度
    root.attributes("-topmost", True) # 窗口置顶

    canvas = tk.Canvas(root, bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # 按下
    def on_mouse_down(event):
        nonlocal rect_start, rect
        rect_start = (event.x, event.y)
        # 创建矩形
        rect = canvas.create_rectangle(rect_start[0], rect_start[1], rect_start[0], rect_start[1], outline="white", fill="white")

    # 移动
    def on_mouse_move(event):
        nonlocal rect_start, rect
        canvas.coords(rect, rect_start[0], rect_start[1], event.x, event.y)

    # 松开
    def on_button_release(event):
        nonlocal rect_end
        rect_end = (event.x, event.y)
        root.destroy()

    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_move)
    canvas.bind("<ButtonRelease-1>", on_button_release)

    root.mainloop()

    grab_box = (rect_start[0], rect_start[1], rect_end[0], rect_end[1])
    # print(grab_box)
    im = ImageGrab.grab(bbox=grab_box)

    return im


# img = grabImage()
# img.save("screenshot.png")
