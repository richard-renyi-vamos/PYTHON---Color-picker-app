import tkinter as tk
from tkinter import colorchooser

def pick_color():
    # Open color chooser and get the selected color
    color_code = colorchooser.askcolor(title="Choose a color")[1]
    if color_code:
        color_display.config(bg=color_code)
        color_label.config(text=f"Selected Color: {color_code}", fg=color_code)

# Create the main application window
root = tk.Tk()
root.title("Color Picker App")
root.geometry("300x200")

# Add a button to trigger the color chooser
pick_color_button = tk.Button(root, text="Pick a Color", command=pick_color, font=("Arial", 14))
pick_color_button.pack(pady=20)

# Add a label to display the selected color's hex code
color_label = tk.Label(root, text="Selected Color: None", font=("Arial", 12))
color_label.pack(pady=10)

# Add a frame to preview the selected color
color_display = tk.Frame(root, bg="white", width=150, height=50, relief="solid", borderwidth=1)
color_display.pack(pady=10)

# Run the application
root.mainloop()
