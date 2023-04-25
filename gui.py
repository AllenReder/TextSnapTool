import tkinter as tk
from tkinter import ttk
from grab_img import grabImage
import ocr


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("300x150")  # set the initial size of the window
        self.master.resizable(False, False)  # make the window non-resizable
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create the screenshot button
        self.screenshot_button = tk.Button(self, width=20, height=2)
        self.screenshot_button["text"] = "Take Screenshot"
        self.screenshot_button["command"] = self.take_screenshot
        self.screenshot_button.pack(side="top", pady=10)

        # create the settings button
        self.settings_button = tk.Button(self, width=20, height=2)
        self.settings_button["text"] = "Settings"
        self.settings_button["command"] = self.open_settings
        self.settings_button.pack(side="top", pady=10)

        # create the quit button
        self.quit_button = tk.Button(self, text="Quit", fg="red",
                                     command=self.master.destroy)
        self.quit_button.pack(side="bottom", pady=10)

    def take_screenshot(self):
        self.master.withdraw()  # hide the main window
        img = grabImage()
        print("debug")
        ocr.ocrText(img)
        self.master.deiconify()  # show the main window

    def open_settings(self):
        settings_window = SettingsWindow(self)


class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Settings")
        self.geometry("300x150")  # set the size of the window
        self.resizable(False, False)  # make the window non-resizable

        # create the notebook
        self.notebook = ttk.Notebook(self)

        # create the "General" tab
        self.general_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.general_frame, text="General")

        # create the "Hotkeys" tab
        self.hotkeys_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.hotkeys_frame, text="Hotkeys")

        # add widgets to the "General" tab
        self.general_label = ttk.Label(
            self.general_frame, text="General Settings")
        self.general_label.pack()

        # add widgets to the "Hotkeys" tab
        self.hotkeys_label = ttk.Label(
            self.hotkeys_frame, text="Hotkey Settings")
        self.hotkeys_label.pack()

        self.notebook.pack(pady=10)


# create the main application window
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()
