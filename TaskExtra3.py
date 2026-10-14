from tkinter import messagebox

class ExtraTask3:
    def __init__(self, data_handler, visualization_handler):
        self.data_handler = data_handler # Store data handler to access dataset
        self.visualization_handler = visualization_handler # Store visualization handler to access plotting

    def find_most_popular_countries(self):
        if self.data_handler.data is None: # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return # Exit the function

        if 'visitor_country' not in self.data_handler.data.columns: # if the visitor country column not there within dataset then
            messagebox.showerror("Error", "The 'visitor_country' field is not available in the data.") # Print error message to warn the user
            return # Exit the function

        country_counts = self.data_handler.data['visitor_country'].value_counts().to_dict() # Count each instance of the visitor country and put them into a dictionary

        if not country_counts: # If no country count data is found then
            messagebox.showinfo("No Data", "No visitor country information found.") # Print error message to warn the user
            return # Exit the function

        self.visualization_handler.plot_histogram(
            country_counts, # Data for the main plotting
            title="Most Popular Visitor Countries", # Title of the histogram
            xlabel="Visitor Countries",  # X axis label
            ylabel="Frequency" # Y axis label
        )
