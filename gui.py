import tkinter as tk
from tkinter import ttk


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        master.title("RSA Encrypt")

    def create_widgets(self):
        self.source_field = LabeledEntry(master=self.master, label="Source",
                                         width=30, foreground="gray70")
        self.source_field.grid(row=0, columnspan=3)

        self.key_field = LabeledEntry(master=self.master, label="Key",
                                      width=30, foreground="gray70")
        self.key_field.grid(row=1, columnspan=3)

        self.encrypt_button = ttk.Button(master=self.master, text="Encrypt")
        self.encrypt_button.grid(row=2, column=0)

        self.encrypt_button = ttk.Button(master=self.master, text="Decrypt")
        self.encrypt_button.grid(row=2, column=1)

        self.settings_button = ttk.Button(master=self.master, text="Settings",
                                          command=self.settings_menu)
        self.settings_button.grid(row=2, column=2)

        self.encrypted_field = LabeledEntry(master=self.master, label="Result",
                                            width=30, foreground="gray70")
        self.encrypted_field.grid(row=3, columnspan=3)

    def settings_menu(self):
        self.settings_window = tk.Toplevel(master=self.master)
        self.settings_window.title("Settings")

        #  Student number widgets
        self.stundent_number_label = tk.Label(master=self.settings_window,
                                              text="Student number")
        self.stundent_number_label.grid(row=0, column=0, sticky=tk.E)
        self.stundent_number_field = tk.Entry(master=self.settings_window,
                                              width=5)
        self.stundent_number_field.grid(row=0, column=1, sticky=tk.W)

        #  Surname widgets
        self.surname_label = tk.Label(master=self.settings_window,
                                      text="Surname")
        self.surname_label.grid(row=1, column=0, sticky=tk.E)
        self.surname_field = tk.Entry(master=self.settings_window)
        self.surname_field.grid(row=1, column=1)
        self.a1z26_field = tk.Entry(master=self.settings_window,
                                    state="disabled")
        self.a1z26_field.grid(row=1, column=2)
        self.a1z26_sum_field = tk.Entry(master=self.settings_window,
                                        state="disabled")
        self.a1z26_sum_field.grid(row=1, column=3)

        #  p and q widgets
        self.p_label = tk.Label(master=self.settings_window, text="p=")
        self.p_label.grid(row=2, column=0, sticky=tk.W)
        self.p_field = tk.Entry(master=self.settings_window)
        self.p_field.grid(row=2, column=1)
        self.q_label = tk.Label(master=self.settings_window, text="q=")
        self.q_label.grid(row=2, column=2)
        self.q_field = tk.Entry(master=self.settings_window)
        self.q_field.grid(row=2, column=3)

        #  TODO
        #  Focus on main window???

        self.settings_window.grab_set()


class LabeledEntry(tk.Entry):
    def __init__(self, master=None, label=None, **kwargs):
        super().__init__(master, **kwargs)
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
