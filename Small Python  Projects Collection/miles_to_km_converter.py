import tkinter as tk


window = tk.Tk() # create a GUI window
window.title("Mile to Km Converter") # add title to the program window

def converter():
	"""Convert Miles to Kms"""
	kilometers = float(miles_input.get()) * 1.60934
	result_label["text"] = f"{kilometers:.2f}"


# takes input from user in miles
miles_input = tk.Entry(width=10)
miles_input.grid(column=1, row=0, padx=10, pady=10)

# informative label
miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0, padx=10, pady=10)

# informative label
equal = tk.Label(text="is equal to", font=("Arial", 10, "normal"))
equal.grid(column=0, row=1, padx=10, pady=10)

# label to show converted result in 
result_label = tk.Label(text="0", font=("Arial", 10, "bold"))
result_label.grid(column=1, row=1, padx=10, pady=10)

# informative label
km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1, padx=10, pady=10)

# calculation button to convert the miles to km 
calculate_button = tk.Button(text="Calculate", command=converter, width=15) 
calculate_button.grid(column=1, row=2, padx=10, pady=15)

window.mainloop() # keep the window opened