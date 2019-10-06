import tkinter as tk
from tkinter import ttk


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        master.title("RSA Encrypt")

    def create_widgets(self):
        self.source_field = LabeledEntry(master=self.master,
                                         width=50, label="Source")
        self.source_field.pack()

        self.key_field = LabeledEntry(master=self.master,
                                      width=50, label="Key")
        self.key_field.pack()

        self.encrypt_button = ttk.Button(master=self.master,
                                         text="Encrypt")
        self.encrypt_button.pack()

        self.encrypted_field = LabeledEntry(master=self.master,
                                            width=50, label="Result")
        self.encrypted_field.pack()


class LabeledEntry(tk.Entry):
    def __init__(self, master=None, label=None, **kwargs):
        tk.Entry.__init__(self, master, **kwargs)
        self.label = label
        self.on_exit()
        self.bind('<FocusIn>', self.on_entry)
        self.bind('<FocusOut>', self.on_exit)

    def on_entry(self, event=None):
        if self.get() == self.label:
            self.delete(0, tk.END)

    def on_exit(self, event=None):
        if not self.get():
            self.insert(0, self.label)


root = tk.Tk()
app = GUI(master=root)
app.mainloop()
