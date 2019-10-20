import tkinter as tk
import re
from gui import GUI


class Kernel(GUI):
    def __init__(self, master=None):
        super().__init__(master)
        self.student_number.trace("rw", self.get_prime)
        self.surname.trace("rw", self.get_a1z26)

    def get_prime(self, *args):
        self.prime_list = [
            97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23,
            19, 17, 13, 11, 7, 5, 3, 2
        ]
        try:
            if 0 < self.student_number.get() <= 25:
                self.p_field.configure(foreground="black")
                self.p.set(self.prime_list[self.student_number.get() - 1])
            else:
                self.p_field.configure(foreground="gray70")
                self.p.set("Invalid student number")
        except tk.TclError as exception:
            if str(exception)[-2:] == "\"\"":
                self.p_field.configure(foreground="gray70")
                self.p.set("Enter student number")
            else:
                self.p_field.configure(foreground="gray70")
                self.p.set("Invalid student number")

    def get_a1z26(self, *args):
        self.a1z26_list = []
        if len(self.surname.get()) > 0:
            self.a1z26_field.configure(foreground="black")
            if re.fullmatch(r"[а-яёА-ЯЁ]*", self.surname.get()):
                for letter in self.surname.get().lower():
                    if 7 <= ord(letter) - 1071 < 33:
                        self.a1z26_list.append((ord(letter) - 1070))
                    elif ord(letter) - 1071 <= 6:
                        self.a1z26_list.append((ord(letter) - 1071))
                    else:
                        self.a1z26_list.append((7))
                self.a1z26.set(self.a1z26_list)
                self.a1z26_sum.set(sum(self.a1z26_list))
            else:
                self.a1z26_sum.set("")
                self.a1z26_field.configure(foreground="gray70")
                self.a1z26.set("Invalid surname")

        else:
            self.a1z26_sum.set("")
            self.a1z26_field.configure(foreground="gray70")
            self.a1z26.set("Enter surname")

    def get_q(self, *args):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    kernel = Kernel(master=root)
    kernel.mainloop()
