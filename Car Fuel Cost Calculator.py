import tkinter as tk
from tkinter import messagebox

def calculate_fuel_cost():
    try:
        distance = float(distance_entry.get())
        fuel_efficiency = float(fuel_efficiency_entry.get())
        fuel_price = float(fuel_price_entry.get())
        
        fuel_needed = distance / fuel_efficiency  # Calculate fuel required
        total_cost = fuel_needed * fuel_price  # Calculate total cost
        
        result_label.config(text=f"Total fuel cost: ₹{total_cost:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

        #def convert_units():
        #try:
     #   miles = float(distance_entry.get())
      #  km = miles * 1.60934  # Convert miles to kilometers
       # distance_entry.delete(0, tk.END)
        #distance_entry.insert(0, f"{km:.2f}")
       #except ValueError:
       #   messagebox.showerror("Conversion Error", "Please enter a valid number in miles.")

# Create GUI window
root = tk.Tk()
root.title("Car Fuel Cost Calculator")

tk.Label(root, text="Distance (km):").grid(row=0, column=0)
distance_entry = tk.Entry(root)
distance_entry.grid(row=0, column=1)

tk.Label(root, text="Fuel Efficiency (km per liter):").grid(row=1, column=0)
fuel_efficiency_entry = tk.Entry(root)
fuel_efficiency_entry.grid(row=1, column=1)

tk.Label(root, text="Fuel Price per Liter (₹):").grid(row=2, column=0)
fuel_price_entry = tk.Entry(root)
fuel_price_entry.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate_fuel_cost)
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
