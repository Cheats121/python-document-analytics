from tkinter import messagebox

class ExtraTask1:
    def __init__(self, data_handler, visualization_handler):
        self.data_handler = data_handler # Store data handler to access dataset
        self.visualization_handler = visualization_handler # Store visualization handler to access plotting

    def find_most_popular_devices(self):
        if self.data_handler.data is None: # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return # Exit the function

        if 'visitor_device' not in self.data_handler.data.columns: # if the visitor device column not there within dataset then
            messagebox.showerror("Error", "The 'visitor_device' field is not available in the data.") # Print error message to warn the user
            return # Exit the function

        device_counts = self.data_handler.data['visitor_device'].value_counts().to_dict() # Count each instance of the visitor device and put them into a dictionary

        if not device_counts: # If no device data or count is found then
            messagebox.showinfo("No Data", "No visitor device information found.") # Print error message to warn the user
            return # Exit the function

        self.visualization_handler.plot_histogram(
            device_counts, # Data for the main plotting
            title="Most Popular Visitor Devices", # Title of the histogram
            xlabel="Visitor Devices", # X axis label
            ylabel="Frequency" # Y axis label
        )
