import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the analyzed data
csv_file = "photo_metadata.csv"

try:
    # Read the data
    df = pd.read_csv(csv_file)

    # Ensure timestamps are parsed
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y:%m:%d %H:%M:%S', errors='coerce')
    df = df.dropna(subset=['Timestamp'])

    # Extract columns if they don’t exist
    if 'Hour' not in df.columns:
        df['Hour'] = df['Timestamp'].dt.hour
    if 'Day' not in df.columns:
        df['Day'] = df['Timestamp'].dt.day_name()
    if 'Month' not in df.columns:
        df['Month'] = df['Timestamp'].dt.month_name()
    if 'Year' not in df.columns:
        df['Year'] = df['Timestamp'].dt.year

    ### 1. Hour of the Day vs Number of Photos (Line Graph)
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Hour', y='Hour', data=df, estimator='count', ci=None, marker='o', color='b')
    plt.title('Photo Counts by Hour (Line Graph)')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Photos')
    plt.savefig('photos_by_hour_line.png')
    plt.show()

    ### 2. Day of the Week vs Number of Photos (Pie Chart)
    day_counts = df['Day'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(day_counts, labels=day_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Photo Distribution by Day of the Week')
    plt.savefig('photos_by_day_pie.png')
    plt.show()

    ### 3. Month vs Number of Photos (Horizontal Bar Chart)
    plt.figure(figsize=(10, 6))
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sns.countplot(y='Month', data=df, order=month_order, palette='viridis')
    plt.title('Photo Counts by Month')
    plt.xlabel('Number of Photos')
    plt.ylabel('Month')
    plt.savefig('photos_by_month_barh.png')
    plt.show()

    ### 4. Year vs Number of Photos (Area Chart)
    year_counts = df['Year'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    plt.fill_between(year_counts.index, year_counts.values, color="skyblue", alpha=0.4)
    plt.plot(year_counts.index, year_counts.values, marker="o", linestyle="-", color="Slateblue")
    plt.title('Photo Counts by Year (Area Chart)')
    plt.xlabel('Year')
    plt.ylabel('Number of Photos')
    plt.savefig('photos_by_year_area.png')
    plt.show()

except FileNotFoundError:
    print(f"Error: {csv_file} not found. Please run gfotos.py to generate the file.")
except Exception as e:
    print(f"An error occurred: {e}")

# 5. Heatmap: Hour vs Day of the Week
heatmap_data = df.pivot_table(index='Day', columns='Hour', aggfunc='size', fill_value=0)
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlGnBu")
plt.title('Photo Distribution by Hour and Day of the Week')
plt.xlabel('Hour of the Day')
plt.ylabel('Day of the Week')
plt.savefig('photos_heatmap_hour_day.png')
plt.show()
# End of visualize_photos.py