import tkinter as tk
from PIL import Image, ImageTk
import time
import os

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Fullscreen Digital Clock")

# Make window fullscreen
root.attributes('-fullscreen', True)

# Dark background
root.config(bg='black')

# Load and display big clock logo image
try:
    img_path = os.path.join(os.path.dirname(__file__), 'clock.png')
    img = Image.open(img_path)
    # Resize to big size, e.g., 300x300
    img = img.resize((300, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)

    logo_label = tk.Label(root, image=photo, bg='black')
    logo_label.image = photo  # keep a reference
    logo_label.pack(pady=30)
except Exception as e:
    print("Clock logo image not found or Pillow not installed:", e)

# Huge clock display label
label = tk.Label(root, font=('Helvetica', 120), bg='black', fg='lime')
label.pack(expand=True, fill='both')

update_time()

# Add ESC key to exit fullscreen and close window
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)
    root.destroy()

root.bind('<Escape>', exit_fullscreen)

root.mainloop()
