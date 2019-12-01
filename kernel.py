import tkinter as tk
import re
from bisect import bisect_left
from gui import GUI

#  TODO
#  Show/hide auto calculated settings parameters


class Kernel(GUI):
    def __init__(self, master=None):
        super().__init__(master)
        self.prime_list = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
            67, 71, 73, 79, 83, 89, 97
        ]
        self.encrypt_button.configure(command=self.encrypt)

        self.student_number.trace("rw", self.get_prime)
        self.surname.trace("rw", self.insert_a1z26)
        self.a1z26_sum.trace("rw", self.get_q)
        self.p.trace("rw", self.get_n)
        self.q.trace("rw", self.get_n)
        self.n.trace("rw", self.get_phi)
        self.phi.trace("rw", self.get_e)
        self.e.trace("rw", self.get_d)

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

    def get_a1z26(self, char):
        if 7 <= ord(char) - 1071 < 33:
            return (ord(char) - 1070)
        elif ord(char) - 1071 <= 6:
            return (ord(char) - 1071)
        else:
            return 7

    def insert_a1z26(self, *args):
        a1z26_list = []
        if len(self.surname.get()) > 0:
            self.a1z26_field.configure(foreground="black")
            if re.fullmatch(r"[а-яёА-ЯЁ]*", self.surname.get()):
                for letter in self.surname.get().lower():
                    a1z26_list.append(self.get_a1z26(letter))
                self.a1z26.set(a1z26_list)
                self.a1z26_sum.set(sum(a1z26_list))
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

    def get_n(self, *args):
        try:
            self.n.set(self.p.get() * self.q.get())
            self.n_field.configure(foreground="black")
        except tk.TclError:
            self.n_field.configure(foreground="gray70")
            self.n.set("Invalid p or q")

    def get_phi(self, *args):
        try:
            self.phi.set((self.p.get() - 1) * (self.q.get() - 1))
            self.euler_func_field.configure(foreground="black")
        except tk.TclError:
            self.euler_func_field.configure(foreground="gray70")
            self.phi.set("Invalid n")

    def egcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.egcd(b % a, a)
            return g, x - (b // a) * y, y

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            #  TODO
            #  Rewrite to insert exception to field
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def get_e(self, *args):
        try:
            for e in range(2, self.phi.get()):
                if self.egcd(self.phi.get(), e)[0] == 1:
                    self.e_field.configure(foreground="black")
                    self.e.set(e)
                    break
        except tk.TclError:
            self.e_field.configure(foreground="gray70")
            self.e.set("Invalid phi")

    def get_d(self, *args):
        try:
            self.d.set(self.modinv(self.e.get(), self.phi.get()))
            self.d_field.configure(foreground="black")
        except (tk.TclError, Exception):
            self.d_field.configure(foreground="gray70")
            self.d.set("Invalid e")

    def encrypt_block(self, block):
        return pow(block, self.e.get(), self.n.get())

    def encrypt(self):
        for block in self.source_field.get():
            self.encrypted_field.insert(
                0, self.encrypt_block(self.get_a1z26(block)))


if __name__ == "__main__":
    root = tk.Tk()
    kernel = Kernel(master=root)
    kernel.mainloop()
