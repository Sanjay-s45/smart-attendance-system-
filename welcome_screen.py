import tkinter as tk
import threading
import subprocess
from PIL import Image, ImageTk

# === Main Window
welcome = tk.Tk()
welcome.title("Welcome")
welcome.geometry("600x500")
welcome.config(bg="#1e1e2f")

# === Load and Show Logo+
logo_image = Image.open("logo.png")
logo_image = logo_image.resize((120, 120))  # Resize if needed
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(welcome,  image=logo_photo, bg="#1e1e2f")
logo_label.pack(pady=30)

# === Animated Text
welcome_label = tk.Label(welcome, text="", font=("Arial Rounded MT Bold", 22), fg="white", bg="#1e1e2f")
welcome_label.pack()

text_to_type = "Welcome to Smart Attendance System"
.
def type_text(index=0):
    if index < len(text_to_type):
        current = welcome_label.cget("text")
        welcome_label.config(text=current + text_to_type[index])
        welcome.after(100, type_text, index + 1)
    else:
        welcome.after(2500, open_main_gui)

def open_main_gui():
    welcome.destroy()
    subprocess.run(["python", "main_with_login.py"])  # or "attendance_gui.py" if no login

threading.Thread(target=type_text).start()
welcome.mainloop()
