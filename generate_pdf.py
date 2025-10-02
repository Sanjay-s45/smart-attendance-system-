import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf():
    try:
        df = pd.read_csv("attendance.csv")

        # File setup
        c = canvas.Canvas("attendance_report.pdf", pagesize=A4)
        width, height = A4
        c.setFont("Helvetica-Bold", 16)
        c.drawString(180, height - 50, "Attendance Report")

        c.setFont("Helvetica", 12)
        y = height - 100

        # Column Headers
        c.drawString(50, y, "Name")
        c.drawString(200, y, "Date")
        c.drawString(350, y, "Time")
        y -= 20
        c.line(50, y, 550, y)
        y -= 20

        # Data Rows
        for index, row in df.iterrows():
            if y < 80:
                c.showPage()
                y = height - 80
            c.drawString(50, y, str(row["Name"]))
            c.drawString(200, y, str(row["Date"]))
            c.drawString(350, y, str(row["Time"]))
            y -= 20

        c.save()
        print("✅ PDF Report generated as 'attendance_report.pdf'.")

    except FileNotFoundError:
        print("❌ Error: attendance.csv not found.")
    except Exception as e:
        print("❌ Error:", str(e))

# Run the function
generate_pdf()
