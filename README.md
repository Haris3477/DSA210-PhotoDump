## **PhotoDump: Google Photos Analysis**

### **Description**

The aim of this project is to analyze photo metadata from my Google Photos account to determine when I typically take photos during the day. Using the timestamps embedded in photo metadata (EXIF data), I will uncover patterns in my photo-taking habits, such as the time of day when I am most active with photography.

---

### **Motivation**

While analyzing Snapchat usage previously, I realized that photos taken throughout the day could also reveal interesting insights about my daily activity. This project is motivated by the desire to understand when I am most likely to capture moments and whether there are noticeable patterns in my photo-taking behavior over time.

---

### **Tools to Be Used**

- **Programming Language:** Python  
- **Libraries:**
  - **Pandas:** For data extraction, cleaning, and analysis.
  - **Matplotlib & Seaborn:** For creating visualizations such as histograms and heatmaps.
  - **NumPy:** For numerical computations.
  - **Pillow:** To extract EXIF metadata (timestamps) from photos.
  - **OS Module:** To navigate and process files in directories.
  - **Google Photos API:** For programmatically fetching photo metadata.
  - **Jupyter Notebook:** For documenting and presenting the analysis.

---

### **Data Source**

The data for this project will be sourced from my Google Photos account. Photos will either be:

1. **Manually downloaded** for local processing, or  
2. **Fetched using the Google Photos API** to retrieve metadata programmatically.  

The primary information used will be timestamps embedded in the EXIF data of the photos.

---

### **Data Processing**

1. **Raw Data:** Extract timestamps and other metadata from the photos using EXIF data.  
2. **Preprocessing:**  
   - Convert timestamps to readable formats (example: hour of the day).  
   - Filter out photos without valid metadata.  
3. **Exploratory Data Analysis (EDA):**  
   - Group and analyze photos by time of day, day of the week, and other possible patterns.  
4. **Final Dataset:** A clean and structured dataset ready for visualization and deeper analysis.

---

### **Data Visualizations**

- **Time-Based Activity:**  
  - Create histograms to show the frequency of photos taken at different times of the day.
- **Daily Trends:**  
  - Analyze photo activity across days of the week to identify any patterns.
- **Heatmaps:**  
  - Generate heatmaps to display photo-taking density by hour and day.

---


## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Haris3477/DSA210-PhotoDump.git
   cd DSA210-PhotoDump
   ```

2. Install required dependencies:
   ```bash
   pip install pandas matplotlib seaborn numpy pillow
   ```

3. Add your photos:
   - Place your photos in the `photos` directory within the project folder
   - Supported formats: .jpg, .jpeg, .png

4. Run the analysis scripts:

   For Python 3.x:
   ```bash
   python3 gfotos.py
   python3 analyze_photos.py
   python3 visualize_photos.py
   ```

   For Python 2.x:
   ```bash
   python gfotos.py
   python analyze_photos.py
   python visualize_photos.py
   ```

## Script Descriptions
- `gfotos.py`: Extracts EXIF metadata from photos
- `analyze_photos.py`: Performs statistical analysis on the extracted data
- `visualize_photos.py`: Generates visualizations and plots

## Output
The scripts will generate:
- CSV files with extracted metadata
- Statistical analysis results
- Visualization plots in the `graphs` directory

## Requirements
- Python 3.x (recommended) or Python 2.x
- Required Python packages listed in dependencies
- Sufficient disk space for photo processing

## Troubleshooting
If you encounter permission issues when running the scripts, try:
```bash
chmod +x gfotos.py analyze_photos.py visualize_photos.py
```

### **Hypothesis**

- **Hypothesis (H₁):**  
  I took most photos at **8 PM on Thursdays in November or December between the years 2015 - 2016**.

- **Null Hypothesis (H₀):**  
  There is no specific pattern indicating that most photos were taken at **8 PM on Thursdays in November or December between the years 2015 - 2016**. Photo-taking behavior is random or follows a different pattern.

---

### **Goals**

- Determine the average times of the day I take photos.
- Identify patterns in photo-taking activity across different timeframes (daily, weekly, etc.).
- Visualize photo-taking trends using clear and informative charts.
- Test the hypothesis to uncover insights about photo-taking habits.

---

### **Findings**

Findings will include detailed insights into my photo-taking habits, such as peak times for photography and any interesting trends over time.
