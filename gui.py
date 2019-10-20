import tkinter as tk
from tkinter import ttk


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        master.title("RSA Encrypt")

        #  Widgets
        self.p_field = None
        self.a1z26_field = None

        #  Variables
        self.student_number = tk.IntVar()
        self.student_number.set("")
        self.p = tk.IntVar()
        self.surname = tk.StringVar()
        self.a1z26 = tk.StringVar()
        self.a1z26_sum = tk.IntVar()

    def create_widgets(self):
        #  Source widgets
        self.source_field = LabeledEntry(master=self.master,
                                         label="Source",
                                         width=30,
                                         foreground="gray70")
        self.source_field.grid(row=0, columnspan=3)

        #  Key widgets
        self.key_field = LabeledEntry(master=self.master,
                                      label="Key",
                                      width=30,
                                      foreground="gray70")
        self.key_field.grid(row=1, columnspan=3)

        #  Encrypt widgets
        self.encrypt_button = ttk.Button(master=self.master, text="Encrypt")
        self.encrypt_button.grid(row=2, column=0)

        #  Decrypt widgets
        self.decrypt_button = ttk.Button(master=self.master, text="Decrypt")
        self.decrypt_button.grid(row=2, column=1)

        #  Settings widgets
        self.settings_button = ttk.Button(master=self.master,
                                          text="Settings",
                                          command=self.settings_menu)
        self.settings_button.grid(row=2, column=2)

        #  Result widgets
        self.encrypted_field = LabeledEntry(master=self.master,
                                            label="Result",
                                            width=30,
                                            foreground="gray70")
        self.encrypted_field.grid(row=3, columnspan=3)

    def settings_menu(self):
        self.settings_window = tk.Toplevel(master=self.master)
        self.settings_window.title("Settings")

        #  p and q widgets
        self.p_label = tk.Label(master=self.settings_window, text="p=")
        self.p_label.grid(row=3, column=0, sticky="e")

        self.p_field = tk.Entry(master=self.settings_window,
                                textvariable=self.p,
                                state="readonly")
        self.p_field.grid(row=3, column=1)

        self.q_label = tk.Label(master=self.settings_window, text="q=")
        self.q_label.grid(row=4, column=0, sticky="e")

        self.q_field = tk.Entry(master=self.settings_window)
        self.q_field.grid(row=4, column=1)

        self.p_and_q_label = tk.Label(master=self.settings_window, text="p*q=")
        self.p_and_q_label.grid(row=5, column=0, sticky="e")

        self.p_and_q_field = tk.Entry(master=self.settings_window)
        self.p_and_q_field.grid(row=5, column=1)

        #  Student number widgets
        self.stundent_number_label = tk.Label(master=self.settings_window,
                                              text="Student number")
        self.stundent_number_label.grid(row=0, column=0, sticky="e")

        self.stundent_number_field = tk.Entry(master=self.settings_window,
                                              textvariable=self.student_number,
                                              width=5)
        self.stundent_number_field.grid(row=0, column=1, sticky="w")

        #  Surname widgets
        self.a1z26_field = tk.Entry(master=self.settings_window,
                                    textvariable=self.a1z26,
                                    state="readonly")
        self.a1z26_field.grid(row=2, column=1)

        self.surname_label = tk.Label(master=self.settings_window,
                                      text="Surname")
        self.surname_label.grid(row=1, column=0, sticky="e")

        self.surname_field = tk.Entry(master=self.settings_window,
                                      textvariable=self.surname)
        self.surname_field.grid(row=1, column=1)

        self.a1z26_label = tk.Label(master=self.settings_window, text="А1Я33")
        self.a1z26_label.grid(row=2, column=0, sticky="e")

        self.a1z26_sum_field = tk.Entry(master=self.settings_window,
                                        textvariable=self.a1z26_sum,
                                        state="readonly",
                                        width=7)
        self.a1z26_sum_field.grid(row=2, column=3)

        #  Euler function widgets
        self.euler_func_label = tk.Label(master=self.settings_window,
                                         text="phi(n)=")
        self.euler_func_label.grid(row=6, column=0, sticky="e")

        self.euler_func_field = tk.Entry(master=self.settings_window)
        self.euler_func_field.grid(row=6, column=1)


class LabeledEntry(tk.Entry):
    def __init__(self, master=None, label=None, **kwargs):
        super().__init__(master, **kwargs)
        self.label = label
        self.on_focus_out()
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

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
