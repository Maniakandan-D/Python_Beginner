try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

tkinter._test()
