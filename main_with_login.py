import tkinter as tk
from tkinter import messagebox
import subprocess

# === Admin credentials (you can change them)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

# === Login function
def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        login_window.destroy()
        subprocess.run(["python", "attendance_gui.py"])
    else:
        messagebox.showerror("Login Failed", "❌ Invalid username or password")

# === Login Window UI
login_window = tk.Tk()
login_window.title("Admin Login")
login_window.geometry("300x200")
login_window.configure(bg="#2c3e50")

tk.Label(login_window, text="Admin Login", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50").pack(pady=10)

tk.Label(login_window, text="Username:", bg="#2c3e50", fg="white").pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password:", bg="#2c3e50", fg="white").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=check_login, bg="#3498db", fg="white", width=20).pack(pady=15)

login_window.mainloop()
