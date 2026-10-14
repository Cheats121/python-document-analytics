import pandas as pd
from tkinter import messagebox
from collections import Counter

class ExtraTask5:
    def __init__(self, data_handler, visualization_handler):
        self.data_handler = data_handler # Store data handler to access dataset
        self.visualization_handler = visualization_handler # Store visualization handler to access plotting

    def find_top_visited_documents(self):
        if self.data_handler.data is None:  # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return # Exit the function

        if 'subject_doc_id' not in self.data_handler.data.columns:  # if the Subject doc ID column not there within dataset then
            messagebox.showerror("Error", "The 'subject_doc_id' field is not available in the data.") # Print error message to warn the user
            return # Exit the function

        doc_counts = self.data_handler.data['subject_doc_id'].value_counts() # Count each instance of the document UUID

        if doc_counts.empty:  # If no document UUID count data is found then
            messagebox.showinfo("No Data", "No document interaction data found.") # Print error message to warn the user
            return # Exit the function

        top_10_docs = doc_counts.head(10) # Get the top 10 documents from the doc_counts using head() 

        shortened_labels = {doc[-4:]: count for doc, count in top_10_docs.items()} # Shorten the labels to 4 hex characters for ease of viewing

        self.visualization_handler.plot_bar_chart(
            pd.Series(shortened_labels),  # Data for the main plotting
            title="Top 10 Most Visited Documents", # Title of the histogram
            xlabel="Document UUID (Last 4 Hex)", # X axis label
            ylabel="Visit Count" # Y axis label
        )
