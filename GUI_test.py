import tkinter as tk

def process_data():
    data = []
    for entry in entry_list:
        value = entry.get()
        data.append(value)
    print("Input data:", data)

root = tk.Tk()
root.title("Input Data GUI")

# Create a list to store the Entry widgets
entry_list = []

# Create and pack 8 Entry widgets
for i in range(8):
    entry = tk.Entry(root)
    entry.pack()
    entry_list.append(entry)

# Create and pack the submit button
submit_button = tk.Button(root, text="Submit", command=process_data)
submit_button.pack()

root.mainloop()
