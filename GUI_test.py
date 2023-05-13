import tkinter as tk

# info = input('enter data: ')
#
# window = tkinter.Tk()
# greeting = tkinter.Label(text="Hello, Ran")
# data = tkinter.Label(text=info, foreground='Blue', background='yellow')
# data.pack()
# greeting.pack()
# exit = tkinter.Button(text='close window')
# exit.pack()
# window.mainloop()

window = tk.Tk()
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=2
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()