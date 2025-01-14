import tkinter as tk
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataVisualizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Data Visualization")
        self.root.geometry("800x600")

        # Input field for data
        self.input_label = CTkLabel(root, text="Enter Data (comma-separated):", font=("Arial", 14))
        self.input_label.grid(row=0, column=0, padx=10, pady=10)

        self.input_entry = CTkEntry(root, width=300, font=("Arial", 14))
        self.input_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to update visualization
        self.update_button = CTkButton(root, text="Update Visualization", command=self.update_visualization)
        self.update_button.grid(row=0, column=2, padx=10, pady=10)

        # Matplotlib figure for graph and pie chart
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Initialize data storage
        self.data = []

    def update_visualization(self):
        # Get input data
        input_data = self.input_entry.get().strip()
        if not input_data:
            return

        try:
            # Convert input to a list of numbers
            self.data = [float(x) for x in input_data.split(",")]
        except ValueError:
            print("Invalid input. Please enter comma-separated numbers.")
            return

        # Clear previous plots
        self.ax1.clear()
        self.ax2.clear()

        # Plot line graph
        self.ax1.plot(self.data, marker='o', color='b')
        self.ax1.set_title("Line Graph")
        self.ax1.set_xlabel("Index")
        self.ax1.set_ylabel("Value")

        # Plot pie chart
        labels = [f"Data {i+1}" for i in range(len(self.data))]
        self.ax2.pie(self.data, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
        self.ax2.set_title("Pie Chart")

        # Redraw canvas
        self.canvas.draw()

if __name__ == "__main__":
    root = CTk()
    app = DataVisualizationApp(root)
    root.mainloop()