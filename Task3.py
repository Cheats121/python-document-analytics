from tkinter import messagebox # Import messagebox module from tkinter

# READER PROFILES *****
class Task3:
    def __init__(self, data_handler, visualization_handler):
        self.data_handler = data_handler # Store data handler to access dataset
        self.visualization_handler = visualization_handler # Store visualization handler to access plotting

    def view_top_readers(self):
        if self.data_handler.data is None: # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return # Exit the function

        read_time_data = self.data_handler.data[self.data_handler.data['event_type'] == 'pagereadtime'] # Filter the dataset to find the pageread times by the visitor

        if read_time_data.empty: # If the pageread times are not found within the dataset then
            messagebox.showwarning("No Data", "No reading time data available.") # Print the error to warn the user
            return # Exit the function

        total_reading_time = read_time_data.groupby('visitor_uuid')['event_readtime'].sum() # For each visitor group them into visitor_uuid and event_readtime and sum up the total time for each visitor

        top_readers = total_reading_time.nlargest(10) # After summing give the top 10 readers from the list in descending order

        top_readers_str = "\n\n".join([f"{uuid:<}: {time // 60:>} Minutes" for uuid, time in top_readers.items()]) # Format the data into a readable string by the visitor uuid and time in seconds
        messagebox.showinfo("Top 10 Readers", f"Top 10 Readers by Total Time:\n--------------------------------------\n{top_readers_str}") # Print the results within a message box using tkinter
