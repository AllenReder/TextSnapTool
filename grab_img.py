
import tkinter as tk
from PIL import ImageGrab

root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-alpha", 0.1)

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

rect_start = None
rect_end = None

def on_mouse_down(event):
    global rect_start, rect
    rect_start = (event.x, event.y)
    rect = canvas.create_rectangle(
        rect_start[0], rect_start[1], rect_start[0], rect_start[1], outline="white", fill="white")


def on_mouse_move(event):
    global rect_start, rect
    canvas.coords(rect, rect_start[0], rect_start[1], event.x, event.y)


def on_button_release(event):
    global rect_end
    rect_end = (event.x, event.y)
    root.destroy()


canvas.bind("<ButtonPress-1>", on_mouse_down)
canvas.bind("<B1-Motion>", on_mouse_move)
canvas.bind("<ButtonRelease-1>", on_button_release)

root.mainloop()

grab_box = (rect_start[0], rect_start[1], rect_end[0], rect_end[1])
print(grab_box)
im = ImageGrab.grab(bbox=grab_box)

# 将截图保存为文件
im.save("screenshot.png")