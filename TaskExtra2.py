from tkinter import messagebox

class ExtraTask2:
    def __init__(self, data_handler, visualization_handler):
        self.data_handler = data_handler # Store data handler to access dataset
        self.visualization_handler = visualization_handler # Store visualization handler to access plotting

    def find_most_popular_sources(self):
        if self.data_handler.data is None: # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return # Exit the function

        if 'visitor_source' not in self.data_handler.data.columns: # if the visitor source column not there within dataset then
            messagebox.showerror("Error", "The 'visitor_source' field is not available in the data.") # Print error message to warn the user
            return # Exit the function

        source_counts = self.data_handler.data['visitor_source'].value_counts().to_dict() # Count each instance of the visitor source and put them into a dictionary

        if not source_counts: # If no source count data or is found then
            messagebox.showinfo("No Data", "No visitor source information found.") # Print error message to warn the user
            return # Exit the function
        
        self.visualization_handler.plot_histogram(
            source_counts, # Data for the main plotting
            title="Most Popular Visitor Sources", # Title of the histogram
            xlabel="Visitor Sources", # X axis label
            ylabel="Frequency" # Y axis label
        )
