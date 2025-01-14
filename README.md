# Modern Data Visualization App

## Overview
The **Modern Data Visualization App** is a Python-based application built using `CustomTkinter` for the graphical user interface (GUI) and `Matplotlib` for data visualization. It allows users to import datasets, perform real-time data visualization, and analyze data using various chart types and machine learning techniques. The app is designed to be user-friendly and flexible, supporting both numerical and categorical data.

---

## Features
1. **Data Import**:
   - Import datasets in CSV format.
   - Automatically detect numerical and categorical columns.

2. **Data Visualization**:
   - Supports multiple chart types:
     - Line Graph
     - Bar Chart
     - Pie Chart
     - Scatter Plot
     - Histogram
     - Area Chart
   - Dynamically update visualizations based on user input.

3. **Real-Time Data Streaming**:
   - Simulate real-time data updates for dynamic visualization.

4. **Machine Learning Integration**:
   - Apply machine learning techniques:
     - Trend Line (Linear Regression)
     - Clustering (K-Means)

5. **Overall Calculations**:
   - Display summary statistics for numerical columns (mean, median, min, max, etc.).
   - Display value counts for categorical columns.

6. **Export Graphs**:
   - Save visualizations as PNG, JPEG, or PDF files.

---

## How to Use
1. **Import Data**:
   - Click the **Import Data** button to load a CSV file.
   - The app will automatically detect and display the columns in the dataset.

2. **Select Column and Chart Type**:
   - Choose a column from the dropdown menu.
   - Select a chart type (e.g., Line Graph, Bar Chart, Pie Chart).

3. **Update Visualization**:
   - Click the **Update Visualization** button to generate the graph.

4. **Enable Real-Time Streaming**:
   - Check the **Enable Real-Time Streaming** checkbox to simulate real-time data updates.

5. **Apply Machine Learning**:
   - Select a machine learning option (Trend Line or Clustering) from the dropdown menu.

6. **Export Graphs**:
   - Click the **Export Graph** button to save the current visualization as an image.

---

## Prerequisites
To run the app, ensure you have the following Python libraries installed:
- `customtkinter`
- `matplotlib`
- `pandas`
- `numpy`
- `scikit-learn`

You can install the required libraries using pip:
```bash
pip install customtkinter matplotlib pandas numpy scikit-learn
```

---

## Code Structure
- **GUI**:
  - Built using `CustomTkinter` for a modern and customizable interface.
  - Includes a sidebar for controls and a main content area for visualizations.

- **Data Handling**:
  - Uses `pandas` to read and process CSV files.
  - Automatically detects numerical and categorical columns.

- **Visualization**:
  - Uses `matplotlib` to create and display graphs.
  - Supports multiple chart types and dynamic updates.

- **Machine Learning**:
  - Integrates `scikit-learn` for trend line fitting and clustering.

---

## Example Dataset
The app works with any CSV dataset. Here’s an example dataset (`students.csv`):

```csv
Name,Age,Math Score,Science Score,English Score,Grade
Alice,18,85,90,88,A
Bob,17,78,82,75,B
Charlie,19,92,88,91,A
Diana,18,65,70,68,C
Eva,17,88,85,90,A
Frank,19,72,75,70,B
Grace,18,95,92,94,A
Henry,17,60,65,62,D
Ivy,19,80,78,82,B
Jack,18,55,50,58,F
```

---



## Explanation
The app is designed to be a versatile tool for data visualization and analysis. It combines the simplicity of a GUI with the power of Python's data science libraries. Key features include:
- **Dynamic Updates**: Visualizations update in real-time based on user input.
- **Flexibility**: Supports both numerical and categorical data.
- **Extensibility**: Easy to add new features and enhancements.

---

## How to Run
1. Clone the repository or download the script.
2. Install the required libraries (see **Prerequisites**).
3. Run the script:
   ```bash
   python app.py
   ```
4. Use the app to import data, visualize it, and perform analysis.

---

## License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## Author
- **Hariom Kumar**
- Contact: [Your Email Address]

---

Enjoy exploring your data with the **Modern Data Visualization App**! Let me know if you have any questions or suggestions. 🚀