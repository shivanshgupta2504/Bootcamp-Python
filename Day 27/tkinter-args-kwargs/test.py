import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Labels
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


# Buttons
def button_click():
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=input.get())


button = tk.Button(text="Click me", command=button_click)
button.grid(column=1, row=1)

new_button = tk.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = tk.Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()
