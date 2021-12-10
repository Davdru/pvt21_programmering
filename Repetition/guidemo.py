import tkinter


root = tkinter.Tk()

button = tkinter.Button(root, text="Min knapp", command=lambda :print("Hello there"))
button.pack()

root.mainloop()