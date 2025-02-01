from tkinter import Tk, Frame, Text, Entry, Button, END
import requests
from ui import AppUI
from utils import fetch_server_data

class App:
    def __init__(self, root):
        self.root = root
        self.ui = AppUI(root)
        self.ui.submit_button.config(command=self.get_server_data)
        self.ui.clear_button.config(command=self.clear_console)

    def get_server_data(self):
        cfx_code = self.ui.input_area.get()
        if cfx_code:
            response = fetch_server_data(cfx_code)
            self.ui.output_box.config(state='normal')
            self.ui.output_box.delete(1.0, END)
            self.ui.output_box.insert(END, response)
            self.ui.output_box.config(state='disabled')

    def clear_console(self):
        self.ui.output_box.config(state='normal')
        self.ui.output_box.delete(1.0, END)
        self.ui.output_box.config(state='disabled')

if __name__ == "__main__":
    root = Tk()
    root.title("FiveM Resolver")
    root.geometry("600x400")
    root.configure(bg='#2e2e2e')
    app = App(root)
    root.mainloop()