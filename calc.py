import tkinter as tk
from tkinter import filedialog
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel, CTkOptionMenu, CTkCheckBox, CTkComboBox, CTkSlider
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import random
import threading
import time

class ModernDataVisualizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Data Visualization App")
        self.root.geometry("1200x800")

        # Initialize data storage
        self.data = []
        self.df = None  # For imported data

        # Sidebar for controls
        self.sidebar = tk.Frame(root, width=200, bg="#2E3440")
        self.sidebar.grid(row=0, column=0, rowspan=10, sticky="ns")
        self.sidebar.grid_propagate(False)

        # Main content area
        self.main_content = tk.Frame(root, bg="#3B4252")
        self.main_content.grid(row=0, column=1, rowspan=10, sticky="nsew")

        # Input field for data
        self.input_label = CTkLabel(self.sidebar, text="Enter Data (comma-separated):", font=("Arial", 12))
        self.input_label.grid(row=0, column=0, padx=10, pady=10)

        self.input_entry = CTkEntry(self.sidebar, width=180, font=("Arial", 12))
        self.input_entry.grid(row=1, column=0, padx=10, pady=10)

        # Dropdown for chart type
        self.chart_type_label = CTkLabel(self.sidebar, text="Select Chart Type:", font=("Arial", 12))
        self.chart_type_label.grid(row=2, column=0, padx=10, pady=10)

        self.chart_type = CTkOptionMenu(self.sidebar, values=["Line Graph", "Bar Chart", "Pie Chart", "Scatter Plot", "Histogram", "Area Chart"])
        self.chart_type.grid(row=3, column=0, padx=10, pady=10)

        # Button to update visualization
        self.update_button = CTkButton(self.sidebar, text="Update Visualization", command=self.update_visualization)
        self.update_button.grid(row=4, column=0, padx=10, pady=10)

        # Import/Export buttons
        self.import_button = CTkButton(self.sidebar, text="Import Data", command=self.import_data)
        self.import_button.grid(row=5, column=0, padx=10, pady=10)

        self.export_button = CTkButton(self.sidebar, text="Export Graph", command=self.export_graph)
        self.export_button.grid(row=6, column=0, padx=10, pady=10)

        # Real-time data streaming
        self.streaming_var = tk.BooleanVar()
        self.streaming_check = CTkCheckBox(self.sidebar, text="Enable Real-Time Streaming", variable=self.streaming_var)
        self.streaming_check.grid(row=7, column=0, padx=10, pady=10)

        # Machine Learning options
        self.ml_label = CTkLabel(self.sidebar, text="Machine Learning:", font=("Arial", 12))
        self.ml_label.grid(row=8, column=0, padx=10, pady=10)

        self.ml_option = CTkOptionMenu(self.sidebar, values=["None", "Trend Line", "Clustering"])
        self.ml_option.grid(row=9, column=0, padx=10, pady=10)

        # Matplotlib figure for graph
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main_content)
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)

        # Add a toolbar for zoom/pan
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.main_content)
        self.toolbar.update()
        self.toolbar.grid(row=1, column=0, padx=10, pady=10)

        # Start real-time data streaming thread
        self.streaming_thread = threading.Thread(target=self.real_time_streaming, daemon=True)
        self.streaming_thread.start()

    def update_visualization(self):
        # Get input data
        input_data = self.input_entry.get().strip()
        if input_data:
            try:
                self.data = [float(x) for x in input_data.split(",")]
            except ValueError:
                print("Invalid input. Please enter comma-separated numbers.")
                return

        # Clear previous plot
        self.ax.clear()

        # Get selected chart type
        chart_type = self.chart_type.get()

        # Plot based on selected chart type
        if chart_type == "Line Graph":
            self.ax.plot(self.data, marker='o', color='b')
            self.ax.set_title("Line Graph")
            self.ax.set_xlabel("Index")
            self.ax.set_ylabel("Value")
        elif chart_type == "Bar Chart":
            self.ax.bar(range(len(self.data)), self.data, color='g')
            self.ax.set_title("Bar Chart")
            self.ax.set_xlabel("Index")
            self.ax.set_ylabel("Value")
        elif chart_type == "Pie Chart":
            labels = [f"Data {i+1}" for i in range(len(self.data))]
            self.ax.pie(self.data, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
            self.ax.set_title("Pie Chart")
        elif chart_type == "Scatter Plot":
            self.ax.scatter(range(len(self.data)), self.data, color='r')
            self.ax.set_title("Scatter Plot")
            self.ax.set_xlabel("Index")
            self.ax.set_ylabel("Value")
        elif chart_type == "Histogram":
            self.ax.hist(self.data, bins=10, color='purple', edgecolor='black')
            self.ax.set_title("Histogram")
            self.ax.set_xlabel("Value")
            self.ax.set_ylabel("Frequency")
        elif chart_type == "Area Chart":
            self.ax.fill_between(range(len(self.data)), self.data, color='orange', alpha=0.4)
            self.ax.set_title("Area Chart")
            self.ax.set_xlabel("Index")
            self.ax.set_ylabel("Value")

        # Apply Machine Learning
        self.apply_machine_learning()

        # Redraw canvas
        self.canvas.draw()

    def apply_machine_learning(self):
        ml_option = self.ml_option.get()
        if ml_option == "Trend Line" and len(self.data) > 1:
            X = np.array(range(len(self.data))).reshape(-1, 1)
            y = np.array(self.data)
            model = LinearRegression()
            model.fit(X, y)
            trend = model.predict(X)
            self.ax.plot(X, trend, color='red', linestyle='--', label="Trend Line")
            self.ax.legend()
        elif ml_option == "Clustering" and len(self.data) > 1:
            X = np.array(range(len(self.data))).reshape(-1, 1)
            kmeans = KMeans(n_clusters=2)
            kmeans.fit(X)
            clusters = kmeans.predict(X)
            self.ax.scatter(range(len(self.data)), self.data, c=clusters, cmap='viridis')
            self.ax.set_title("Clustering")

    def import_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx"), ("JSON Files", "*.json")])
        if file_path:
            if file_path.endswith(".csv"):
                self.df = pd.read_csv(file_path)
            elif file_path.endswith(".xlsx"):
                self.df = pd.read_excel(file_path)
            elif file_path.endswith(".json"):
                self.df = pd.read_json(file_path)
            self.data = self.df.iloc[:, 0].tolist()  # Use the first column for visualization
            self.update_visualization()

    def export_graph(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("PDF Files", "*.pdf")])
        if file_path:
            self.fig.savefig(file_path)

    def real_time_streaming(self):
        while True:
            if self.streaming_var.get():
                self.data.append(random.randint(1, 100))
                if len(self.data) > 20:  # Limit data points
                    self.data.pop(0)
                self.update_visualization()
            time.sleep(1)

if __name__ == "__main__":
    root = CTk()
    app = ModernDataVisualizationApp(root)
    root.mainloop()