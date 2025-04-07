import tkinter as tk
from tkinter import ttk

def convert():
    try:
        value = float(entry_value.get())
        unit_from = combo_from.get()
        unit_to = combo_to.get()

        result = ""
        if unit_from == "Celsius" and unit_to == "Fahrenheit":
            result = (value * 9/5) + 32
        elif unit_from == "Fahrenheit" and unit_to == "Celsius":
            result = (value - 32) * 5/9
        elif unit_from == "Kilometers" and unit_to == "Miles":
            result = value * 0.621371
        elif unit_from == "Miles" and unit_to == "Kilometers":
            result = value / 0.621371
        elif unit_from == "Kilograms" and unit_to == "Pounds":
            result = value * 2.20462
        elif unit_from == "Pounds" and unit_to == "Kilograms":
            result = value / 2.20462
        else:
            result = "Invalid conversion"

        label_result.config(text=f"Result: {result:.2f}")
    except ValueError:
        label_result.config(text="Enter a valid number")

# GUI setup
app = tk.Tk()
app.title("Unit Converter")

tk.Label(app, text="Enter Value:").grid(row=0, column=0, padx=10, pady=10)
entry_value = tk.Entry(app)
entry_value.grid(row=0, column=1, padx=10, pady=10)

units = ["Celsius", "Fahrenheit", "Kilometers", "Miles", "Kilograms", "Pounds"]

combo_from = ttk.Combobox(app, values=units)
combo_from.grid(row=1, column=0, padx=10)
combo_from.set("Celsius")

combo_to = ttk.Combobox(app, values=units)
combo_to.grid(row=1, column=1, padx=10)
combo_to.set("Fahrenheit")

tk.Button(app, text="Convert", command=convert).grid(row=2, column=0, columnspan=2, pady=10)
label_result = tk.Label(app, text="Result:")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

app.mainloop()
