import tkinter as tk
from tkinter import ttk

# Main window
window = tk.Tk()
window.title("Physics Calculator")
window.geometry("500x400")

# Tabs (Kinematics and Energies)
notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)  # Kinematics
tab2 = ttk.Frame(notebook)  # Energies

notebook.add(tab1, text="Kinematics")
notebook.add(tab2, text="Energies")
notebook.pack(expand=True, fill="both")

# ======== Kinematics Section ========
def calculate_kinematics():
    try:
        distance = float(entry_distance.get())
        time = float(entry_time.get())
        speed = distance / time
        label_result_kinematics.config(text=f"Speed: {speed:.2f} m/s")
    except ValueError:
        label_result_kinematics.config(text="Please enter valid distance and time!")

# Distance and time input
label_distance = tk.Label(tab1, text="Distance (m):")
label_distance.pack()
entry_distance = tk.Entry(tab1)
entry_distance.pack()

label_time = tk.Label(tab1, text="Time (s):")
label_time.pack()
entry_time = tk.Entry(tab1)
entry_time.pack()

# Calculate button
button_calculate_kinematics = tk.Button(tab1, text="Calculate", command=calculate_kinematics)
button_calculate_kinematics.pack(pady=10)

# Result display
label_result_kinematics = tk.Label(tab1, text="", font=("Arial", 12))
label_result_kinematics.pack()

# ======== Energies Section ========
def calculate_energy():
    try:
        mass = float(entry_mass.get())
        velocity = float(entry_velocity.get())
        height = float(entry_height.get())
        # Kinetic energy
        kinetic_energy = 0.5 * mass * velocity**2
        # Potential energy
        potential_energy = mass * 9.8 * height
        label_result_energy.config(text=f"Kinetic E: {kinetic_energy:.2f} J\nPotential E: {potential_energy:.2f} J")
    except ValueError:
        label_result_energy.config(text="Please enter valid mass, velocity, and height!")

# Mass, velocity, and height input
label_mass = tk.Label(tab2, text="Mass (kg):")
label_mass.pack()
entry_mass = tk.Entry(tab2)
entry_mass.pack()

label_velocity = tk.Label(tab2, text="Velocity (m/s):")
label_velocity.pack()
entry_velocity = tk.Entry(tab2)
entry_velocity.pack()

label_height = tk.Label(tab2, text="Height (m):")
label_height.pack()
entry_height = tk.Entry(tab2)
entry_height.pack()

# Calculate button
button_calculate_energy = tk.Button(tab2, text="Calculate", command=calculate_energy)
button_calculate_energy.pack(pady=10)

# Result display
label_result_energy = tk.Label(tab2, text="", font=("Arial", 12))
label_result_energy.pack()

# Run the main window
window.mainloop()
