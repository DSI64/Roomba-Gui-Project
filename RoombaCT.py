import tkinter as tk

def power_color(color):
    power.config(bg=color)

def update_digits(event):
    # Track digits entered
    if event.char.isdigit():
        current_text = [digit1.cget("text"), digit2.cget("text"), digit3.cget("text"), digit4.cget("text")]
        
        # Replace "-" placeholders with first digit entries
        if "-" in current_text:
            next_index = current_text.index("-")
            current_text[next_index] = event.char
        else:
            # Reset to dashes after 4 digits
            current_text = ["-", "-", "-", "-"]
            current_text[0] = event.char  # Start with new digit

        # Update each LED label
        digit1.config(text=current_text[0])
        digit2.config(text=current_text[1])
        digit3.config(text=current_text[2])
        digit4.config(text=current_text[3])

window = tk.Tk()
window.title("Roomba Controller")
window.geometry("900x600")
window.config(bg="gray")

# Power Button
power = tk.Button(window, text="Power", bg="white", width=5, height=2)
power.place(x=295, y=545)

# Start Button
Boot = tk.Button(window, text="Boot", bg="white", width=5, height=2)
Boot.place(x=295, y=500)

# Color Buttons
red_button = tk.Button(window, bg="red", width=5, height=2, command=lambda: power_color("red"))
red_button.place(x=140, y=370)

orange_button = tk.Button(window, bg="orange", width=5, height=2, command=lambda: power_color("orange"))
orange_button.place(x=95, y=420)

yellow_button = tk.Button(window, bg="yellow", width=5, height=2, command=lambda: power_color("yellow"))
yellow_button.place(x=140, y=470)

green_button = tk.Button(window, bg="green", width=5, height=2, command=lambda: power_color("green"))
green_button.place(x=185, y=420)

# Play a Tune Button
tune = tk.Button(window, bg="white", text="Play A Tune", width=40, height=5)
tune.place(x=530, y=60)

# Load and Display Roomba Image
roomba_image = r"C:\Users\kobeg\Desktop\Coding Projects\Roomba Resized Image.png"
photo5 = tk.PhotoImage(file=roomba_image)
roomba_label = tk.Label(window, image=photo5, bg="white")
roomba_label.place(x=420, y=240)

# Digit LEDs
digit1 = tk.Label(window, text="-", font=("Helvetica", 24), width=2, bg="black", fg="green")
digit1.place(x=200, y=200)

digit2 = tk.Label(window, text="-", font=("Helvetica", 24), width=2, bg="black", fg="green")
digit2.place(x=250, y=200)

digit3 = tk.Label(window, text="-", font=("Helvetica", 24), width=2, bg="black", fg="green")
digit3.place(x=300, y=200)

digit4 = tk.Label(window, text="-", font=("Helvetica", 24), width=2, bg="black", fg="green")
digit4.place(x=350, y=200)

# Bind KeyPress event to update digits directly from keyboard input
window.bind("<KeyPress>", update_digits)

# Load and Display Arrow Image
right_image = r"C:\Users\kobeg\Desktop\Coding Projects\rightarrow resized.png"
photo1 = tk.PhotoImage(file = right_image)
right_arrow = tk.Button(window, image=photo1)
right_arrow.place(x=750, y=440)

up_image = r"C:\Users\kobeg\Desktop\Coding Projects\up arrow resized.png"
photo2 = tk.PhotoImage(file = up_image)
up_arrow = tk.Button(window, image = photo2)
up_arrow.place(x = 700, y = 370)

down_image = r"C:\Users\kobeg\Desktop\Coding Projects\down arrow resized.png"
photo3 = tk.PhotoImage(file = down_image)
down_arrow = tk.Button(window, image = photo3)
down_arrow.place(x = 700, y = 470)


left_image = r"C:\Users\kobeg\Desktop\Coding Projects\left_arrow.png"
photo4 = tk.PhotoImage(file = left_image)
down_arrow = tk.Button(window, image = photo4)
down_arrow.place(x = 605, y = 440)

window.mainloop()