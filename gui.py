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
        self.source_field = LabeledEntry(master=self.master, label="Source",
                                         width=50, foreground="gray70")
        self.source_field.pack()

        self.key_field = LabeledEntry(master=self.master, label="Key",
                                      width=50, foreground="gray70")
        self.key_field.pack()

        self.encrypt_button = ttk.Button(master=self.master, text="Encrypt")
        self.encrypt_button.pack()

        self.encrypted_field = LabeledEntry(master=self.master, label="Result",
                                            width=50, foreground="gray70")
        self.encrypted_field.pack()


class LabeledEntry(tk.Entry):
    def __init__(self, master=None, label=None, **kwargs):
        tk.Entry.__init__(self, master, **kwargs)
        self.label = label
        self.on_focus_out()
        self.bind('<FocusIn>', self.on_focus_in)
        self.bind('<FocusOut>', self.on_focus_out)

    def on_focus_in(self, event=None):
        if self.get() == self.label:
            self.delete(0, tk.END)
            self.configure(foreground="black")

    def on_focus_out(self, event=None):
        if not self.get():
            self.configure(foreground="gray70")
            self.insert(0, self.label)


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(master=root)
    app.mainloop()
