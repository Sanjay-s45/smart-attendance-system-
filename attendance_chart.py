import pandas as pd
import matplotlib.pyplot as plt

# Load attendance data
try:
    df = pd.read_csv("attendance.csv")

    # Count attendance per person
    counts = df['Name'].value_counts()

    # Plot the bar chart
    plt.figure(figsize=(8, 5))
    counts.plot(kind='bar', color='skyblue')
    plt.title("Attendance Count per Person")
    plt.xlabel("Name")
    plt.ylabel("Days Present")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

except FileNotFoundError:
    print("❌ Error: attendance.csv not found.")
