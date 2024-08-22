from tkinter import Tk, Button, StringVar, Entry

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value.replace('x', '*'))
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

root = Tk()
calculator = Calculator(root)

Button(width=11, height=4, text="(", command=lambda: calculator.show('(')).place(x=0, y=50)
Button(width=11, height=4, text=")", command=lambda: calculator.show(')')).place(x=90, y=50)
Button(width=11, height=4, text="%", command=lambda: calculator.show('%')).place(x=180, y=50)
Button(width=11, height=4, text="/", command=lambda: calculator.show('/')).place(x=270, y=50)

Button(width=11, height=4, text="7", command=lambda: calculator.show(7)).place(x=0, y=125)
Button(width=11, height=4, text="8", command=lambda: calculator.show(8)).place(x=90, y=125)
Button(width=11, height=4, text="9", command=lambda: calculator.show(9)).place(x=180, y=125)
Button(width=11, height=4, text="x", command=lambda: calculator.show('x')).place(x=270, y=125)

Button(width=11, height=4, text="4", command=lambda: calculator.show(4)).place(x=0, y=200)
Button(width=11, height=4, text="5", command=lambda: calculator.show(5)).place(x=90, y=200)
Button(width=11, height=4, text="6", command=lambda: calculator.show(6)).place(x=180, y=200)
Button(width=11, height=4, text="-", command=lambda: calculator.show('-')).place(x=270, y=200)

Button(width=11, height=4, text="1", command=lambda: calculator.show(1)).place(x=0, y=275)
Button(width=11, height=4, text="2", command=lambda: calculator.show(2)).place(x=90, y=275)
Button(width=11, height=4, text="3", command=lambda: calculator.show(3)).place(x=180, y=275)
Button(width=11, height=4, text="+", command=lambda: calculator.show('+')).place(x=270, y=275)

Button(width=11, height=4, text="0", command=lambda: calculator.show(0)).place(x=90, y=350)
Button(width=11, height=4, text=".", command=lambda: calculator.show('.')).place(x=0, y=350)
Button(width=11, height=4, text="=", command=calculator.solve).place(x=180, y=350)
Button(width=11, height=4, text="C", command=calculator.clear).place(x=270, y=350)

root.mainloop()
