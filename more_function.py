try:
    import tkinter
except ImportError:  # using python 2
    import tkinter as tkinter


def parabola(x):
    y = x * x
    return y

mainwindow = tkinter.Tk()

mainwindow.title("parabola")
mainwindow.geometry("640*480")

canvas = tkinter.canvas(mainwindow, width=640, height=480)
canvas.grid(row=0, column=0)

for x in range(-100, 100):
    y = parabola(x)
    print(y)
mainwindow.mainloop()
