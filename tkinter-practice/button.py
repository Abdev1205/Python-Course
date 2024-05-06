import tkinter as tk


def simulate_flash_with_delay(button, delay=100):
    """Flashes the button for a more controlled duration."""
    if button["bg"] == "lightblue":
        button.configure(bg="red")
    else:
        button.configure(bg="lightblue")
    # Schedule another color change after the delay
    button.after(delay, simulate_flash_with_delay, button)


root = tk.Tk()

# Set window height and width (pixels)
root.geometry("400x250")

# Create the button after defining root
button = tk.Button(root, text="Click Me!", height=2, width=10)
button.configure(bg="lightblue", activebackground="red")  # Set background colors
button.flash()  # Flash the button immediately upon creation

# Option 2: Simulate a flashing effect with a short delay (more control)
# simulate_flash_with_delay(button)

button.pack()
root.mainloop()
