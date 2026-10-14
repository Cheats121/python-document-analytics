from tkinter import messagebox

class ExtraTask4:
    def __init__(self, data_handler, visualization_handler):
        self.data_handler = data_handler # Store data handler to access dataset
        self.visualization_handler = visualization_handler # Store visualization handler to access plotting

    def find_most_popular_referrers(self):
        if self.data_handler.data is None: # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return # Exit the function

        if 'visitor_referrer' not in self.data_handler.data.columns: # if the visitor referrer column not there within dataset then
            messagebox.showerror("Error", "The 'visitor_referrer' field is not available in the data.") # Print error message to warn the user
            return # Exit the function

        referrer_counts = self.data_handler.data['visitor_referrer'].value_counts() # Count each instance of the visitor referrer

        if referrer_counts.empty: # If no referrer count data is found then
            messagebox.showinfo("No Data", "No visitor referrer information found.") # Print error message to warn the user
            return # Exit the function

        top_10_referrers = referrer_counts.head(10).to_dict() # Get the top 10 referrers from the referre_counts using head() 

        self.visualization_handler.plot_histogram(
            top_10_referrers, # Data for the main plotting
            title="Top 10 Most Popular Visitor Referrers",  # Title of the histogram
            xlabel="Visitor Referrers",  # X axis label
            ylabel="Frequency" # Y axis label
        )
