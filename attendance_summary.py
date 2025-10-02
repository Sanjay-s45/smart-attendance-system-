import pandas as pd

# Load attendance file
file_name = "attendance.csv"

try:
    df = pd.read_csv(file_name)

    # Total attendance count per person
    print("📊 Total Attendance Count:\n")
    total_counts = df['Name'].value_counts()
    print(total_counts)

    print("\n----------------------------")

    # Ask user for date input
    input_date = input("📅 Enter date to filter (YYYY-MM-DD): ")

    # Filter by date
    filtered = df[df['Date'] == input_date]

    if not filtered.empty:
        print(f"\n✅ Records on {input_date}:\n")
        print(filtered)
    else:
        print(f"\n⚠️ No attendance found on {input_date}")

except FileNotFoundError:
    print("❌ 'attendance.csv' not found. Please run attendance.py first.")
