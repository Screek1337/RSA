import tkinter as tk
from tkinter import ttk


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("RSA Encrypt")

        #  Widgets
        self.source_field = None
        self.encrypt_button = None
        self.encrypted_field = None

        self.p_field = None
        self.a1z26_field = None
        self.n_field = None
        self.euler_func_field = None
        self.e_field = None
        self.d_field = None

        self.dropdown_button = None

        #  Icons
        self.rightarrow_icon = tk.PhotoImage(file="right-arrow.gif")
        self.downarrow_icon = tk.PhotoImage(file="down-arrow.gif")

        #  Variables
        self.student_number = tk.IntVar()
        self.student_number.set("")
        self.p = tk.IntVar()
        self.q = tk.IntVar()
        self.n = tk.IntVar()
        self.surname = tk.StringVar()
        self.a1z26 = tk.StringVar()
        self.a1z26_sum = tk.IntVar()
        self.phi = tk.IntVar()
        self.e = tk.IntVar()
        self.d = tk.IntVar()

        self.create_widgets()

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
        x = self.master.winfo_rootx()
        y = self.master.winfo_rooty()
        width = self.master.winfo_width()
        self.settings_window.geometry(f"+{x+width}+{y-21}")

        #  Student number widgets
        self.stundent_number_label = tk.Label(master=self.settings_window,
                                              text="Student number")
        self.stundent_number_label.grid(row=0, column=0, sticky="e")

        self.stundent_number_field = tk.Entry(master=self.settings_window,
                                              width=5)
        self.stundent_number_field.grid(row=0, column=1, sticky="w")

        #  Surname widgets
        self.surname_label = tk.Label(master=self.settings_window,
                                      text="Surname")
        self.surname_label.grid(row=1, column=0, sticky="e")

        self.surname_field = tk.Entry(master=self.settings_window)
        self.surname_field.grid(row=1, column=1)

        #  Dropdown button
        self.hidden = False  # Hide on start
        self.dropdown_button = ttk.Button(
            master=self.settings_window,
            compound=tk.LEFT,
            width=5,
            command=lambda: self.hide_autocalculated(self.hidden))
        self.dropdown_button.grid(row=1, column=2)

        #  a1z26 widgets
        self.a1z26_field = tk.Entry(master=self.settings_window,
                                    state="readonly")
        self.a1z26_field.grid(row=2, column=1)

        self.a1z26_label = tk.Label(master=self.settings_window, text="А1Я33")
        self.a1z26_label.grid(row=2, column=0, sticky="e")

        self.a1z26_sum_field = tk.Entry(master=self.settings_window,
                                        state="readonly",
                                        width=7)
        self.a1z26_sum_field.grid(row=2, column=2)

        #  p widgets
        self.p_label = tk.Label(master=self.settings_window, text="p=")
        self.p_label.grid(row=3, column=0, sticky="e")

        self.p_field = tk.Entry(master=self.settings_window, state="readonly")
        self.p_field.grid(row=3, column=1)

        #  q widgets
        self.q_label = tk.Label(master=self.settings_window, text="q=")
        self.q_label.grid(row=4, column=0, sticky="e")

        self.q_field = tk.Entry(master=self.settings_window, state="readonly")
        self.q_field.grid(row=4, column=1)

        #  p and q widgets
        self.n_label = tk.Label(master=self.settings_window, text="n=")
        self.n_label.grid(row=5, column=0, sticky="e")

        self.n_field = tk.Entry(master=self.settings_window, state="readonly")
        self.n_field.grid(row=5, column=1)

        #  Euler function widgets
        self.euler_func_label = tk.Label(master=self.settings_window,
                                         text="phi(n)=")
        self.euler_func_label.grid(row=6, column=0, sticky="e")

        self.euler_func_field = tk.Entry(master=self.settings_window,
                                         state="readonly")
        self.euler_func_field.grid(row=6, column=1)

        #  e widgets
        self.e_label = tk.Label(master=self.settings_window, text="e=")
        self.e_label.grid(row=7, column=0, sticky="e")

        self.e_field = tk.Entry(master=self.settings_window, state="readonly")
        self.e_field.grid(row=7, column=1)

        #  d widgets
        self.d_label = tk.Label(master=self.settings_window, text="d=")
        self.d_label.grid(row=8, column=0, sticky="e")

        self.d_field = tk.Entry(master=self.settings_window, state="readonly")
        self.d_field.grid(row=8, column=1)

        #  Assigning variables
        self.stundent_number_field.configure(textvariable=self.student_number)
        self.surname_field.configure(textvariable=self.surname)
        self.a1z26_field.configure(textvariable=self.a1z26)
        self.a1z26_sum_field.configure(textvariable=self.a1z26_sum)
        self.p_field.configure(textvariable=self.p)
        self.q_field.configure(textvariable=self.q)
        self.n_field.configure(textvariable=self.n)
        self.euler_func_field.configure(textvariable=self.phi)
        self.e_field.configure(textvariable=self.e)
        self.d_field.configure(textvariable=self.d)

        # Hide autocalculated parameters
        self.hide_autocalculated()

    def hide_autocalculated(self, hidden=False):
        widgets = (self.a1z26_label, self.a1z26_field, self.a1z26_sum_field,
                   self.p_label, self.p_field, self.q_label, self.q_field,
                   self.n_label, self.n_field, self.euler_func_label,
                   self.euler_func_field, self.e_label, self.e_field,
                   self.d_label, self.d_field)
        if not hidden:
            self.dropdown_button.configure(image=self.rightarrow_icon,
                                           text="Show")
            self.hidden = True
            for widget in widgets:
                widget.grid_remove()
        else:
            self.dropdown_button.configure(image=self.downarrow_icon,
                                           text="Hide")
            self.hidden = False
            for widget in widgets:
                widget.grid()


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
