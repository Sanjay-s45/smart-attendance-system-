import pandas as pd

# Read the CSV file
csv_file = "attendance.csv"
excel_file = "attendance_report.xlsx"

try:
    # Read CSV into DataFrame
    df = pd.read_csv(csv_file)

    # Export to Excel
    df.to_excel(excel_file, index=False, engine='openpyxl')

    print(f"[INFO] Exported successfully to '{excel_file}'")
except FileNotFoundError:
    print("[ERROR] 'attendance.csv' file not found. Please run attendance.py first.")
except Exception as e:
    print(f"[ERROR] {str(e)}")
