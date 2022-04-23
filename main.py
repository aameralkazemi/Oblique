import tkinter as tk

class ExampleView(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

if __name__=='__main__':
    root = tk.Tk()
    view = ExampleView(tk.Tk())
    root.mainloop()