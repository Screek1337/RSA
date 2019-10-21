import tkinter as tk
import re
from bisect import bisect_left
from gui import GUI


class Kernel(GUI):
    def __init__(self, master=None):
        super().__init__(master)
        self.prime_list = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
            67, 71, 73, 79, 83, 89, 97
        ]
        self.student_number.trace("rw", self.get_prime)
        self.surname.trace("rw", self.get_a1z26)
        self.a1z26_sum.trace("rw", self.get_q)

    def get_prime(self, *args):
        try:
            if 0 < self.student_number.get() <= 25:
                self.p_field.configure(foreground="black")
                self.p.set(self.prime_list[-self.student_number.get()])
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

    def find_closest(self, number):
        pos = bisect_left(self.prime_list, number)
        if pos == 0:
            return self.prime_list[0]
        if pos == len(self.prime_list):
            return self.prime_list[-1]
        before = self.prime_list[pos - 1]
        after = self.prime_list[pos]
        if after - number < number - before:
            return after
        else:
            return before

    def get_q(self, *args):
        try:
            while self.a1z26_sum.get() > 100:
                self.a1z26_sum.set(self.a1z26_sum.get() - 100)
            self.q_field.configure(foreground="black")
            self.q.set(self.find_closest(self.a1z26_sum.get()))
        except tk.TclError:
            if len(self.surname.get()) > 0:
                self.q_field.configure(foreground="gray70")
                self.q.set("Invalid surname")
            else:
                self.q_field.configure(foreground="gray70")
                self.q.set("Enter surname")


if __name__ == "__main__":
    root = tk.Tk()
    kernel = Kernel(master=root)
    kernel.mainloop()
