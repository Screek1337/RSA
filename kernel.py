import tkinter as tk
from gui import GUI


class Kernel(GUI):
    def __init__(self, master=None):
        super().__init__(master)
        self.student_number.trace("rw", self.get_prime)

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
        except tk.TclError:
            self.p_field.configure(foreground="gray70")
            self.p.set("Invalid student number")


if __name__ == "__main__":
    root = tk.Tk()
    kernel = Kernel(master=root)
    kernel.mainloop()
