from tkcalendar import DateEntry
from datetime import datetime

import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess
import pandas as pd
from PIL import Image, ImageTk

# === Functions ===

def start_attendance():
    try:
        subprocess.run(["python", "attendance.py"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def view_summary():
    try:
        df = pd.read_csv("attendance.csv")
        summary = df['Name'].value_counts().to_string()
        messagebox.showinfo("📊 Attendance Summary", summary)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def export_excel():
    try:
        df = pd.read_csv("attendance.csv")
        df.to_excel("attendance_report.xlsx", index=False, engine='openpyxl')
        messagebox.showinfo("✅ Exported", "Saved as attendance_report.xlsx")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def view_chart():
    try:
        subprocess.run(["python", "attendance_chart.py"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def generate_pdf():
    try:
        subprocess.run(["python", "generate_pdf.py"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_new_person():
    try:
        name = simpledialog.askstring("Add New Person", "Enter name of the person:")
        if name:
            subprocess.run(["python", "capture_faces.py", name])
            subprocess.run(["python", "train_model.py"])
            messagebox.showinfo("Success", f"✅ '{name}' added and model retrained!")
        else:
            messagebox.showwarning("Cancelled", "No name entered.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def filter_attendance_by_date():
    filter_win = tk.Toplevel(window)
    filter_win.title("Filter Attendance by Date")
    filter_win.geometry("300x280")
    filter_win.configure(bg="#1e1e2f")

    tk.Label(filter_win, text="From Date", fg="white", bg="#1e1e2f").pack(pady=5)
    from_date = DateEntry(filter_win, width=18, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
    from_date.pack(pady=5)

    tk.Label(filter_win, text="To Date", fg="white", bg="#1e1e2f").pack(pady=5)
    to_date = DateEntry(filter_win, width=18, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
    to_date.pack(pady=5)

    def apply_filter_and_export():
        try:
            df = pd.read_csv("attendance.csv")
            df['Date'] = pd.to_datetime(df['Date'])
            start = pd.to_datetime(from_date.get())
            end = pd.to_datetime(to_date.get())
            filtered = df[(df['Date'] >= start) & (df['Date'] <= end)]

            if filtered.empty:
                messagebox.showinfo("No Records", "No attendance found in this range.")
                return

            # === PDF Export ===
            from reportlab.lib.pagesizes import A4
            from reportlab.pdfgen import canvas

            c = canvas.Canvas("filtered_attendance.pdf", pagesize=A4)
            width, height = A4
            c.setFont("Helvetica-Bold", 14)
            c.drawString(150, height - 40, f"Filtered Attendance Report")

            c.setFont("Helvetica", 10)
            y = height - 80
            c.drawString(50, y, "Name")
            c.drawString(200, y, "Date")
            c.drawString(350, y, "Time")
            y -= 20
            c.line(50, y, 550, y)
            y -= 20

            for index, row in filtered.iterrows():
                if y < 80:
                    c.showPage()
                    y = height - 80
                c.drawString(50, y, str(row["Name"]))
                c.drawString(200, y, row["Date"].strftime("%Y-%m-%d"))
                c.drawString(350, y, str(row["Time"]))
                y -= 20

            c.save()
            messagebox.showinfo("Success", "🧾 PDF saved as 'filtered_attendance.pdf'.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(filter_win, text="📄 Export as PDF", command=apply_filter_and_export, bg="#ff9800", fg="white", width=20).pack(pady=20)


def close_app():
    window.destroy()

# === GUI Setup ===
window = tk.Tk()
window.title("🧠 Smart Attendance System")
window.geometry("480x600")
window.configure(bg="#1e1e2f")  # Background color

# === Title ===
title_label = tk.Label(window, text="Smart Attendance System", font=("Arial Rounded MT Bold", 18), fg="white", bg="#1e1e2f")
title_label.pack(pady=25)

# === Button Function ===
def create_button(text, command, bg, emoji, y_offset):
    return tk.Button(
        window,
        text=f"{emoji}  {text}",
        command=command,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=bg,
        fg="white",
        bd=0,
        activebackground="#444",
        relief="flat",
        cursor="hand2"
    ).place(relx=0.5, y=y_offset, anchor="center")

# === Buttons ===
create_button("Start Attendance", start_attendance, "#4caf50", "▶", 100)
create_button("View Summary", view_summary, "#2196f3", "📊", 160)
create_button("Export to Excel", export_excel, "#ff9800", "📁", 220)
create_button("Generate PDF Report", generate_pdf, "#795548", "📄", 280)
create_button("📊 View Chart", view_chart, "#607d8b", "📈", 340)
create_button("📅 Filter Attendance by Date", filter_attendance_by_date, "#03a9f4", "📆", 400)
create_button("➕ Add New Person", add_new_person, "#9c27b0", "🧑", 460)
create_button("Exit", close_app, "#f44336", "❌", 520)


# === Run App ===
window.mainloop()

