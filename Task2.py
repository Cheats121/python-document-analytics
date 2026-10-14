from tkinter import messagebox
import re
import httpagentparser

# BROWSER *****

class Task2:
    def __init__(self, data_handler, visualization_handler):
        self.data_handler = data_handler # Store data handler to access dataset
        self.visualization_handler = visualization_handler # Store visualization handler to access plotting

    def show_browser_histogram(self, detailed=True): # Detailed flag set to true by default (Used to handle button logic within the main.py file)
        if self.data_handler.data is None: # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return

        def parse_browser(user_agent):
            try: # Try block to capture any errors
                if detailed: # If flag is set to True then do this
                    parsed = httpagentparser.detect(user_agent) # Extract browser names and versions using httpagentparser
                    browser_info = parsed.get('browser', {}) # Keep the browser details as dictionary
                    name = browser_info.get('name', 'Other') # Extract the browser name and if browser name not found or recoginized then other
                    version = browser_info.get('version', '') # Extract the browser version and if not found or recognized then leave it blank
                    
                    return f"{name} {version}" if version else name # Return the name and version or just the name if version not available
                else: # Else if the flag is set to false then
                    pattern = r"(Chrome|Firefox|Safari|Opera|MSIE|Trident|Edge)" # Extract browser names using regex
                    match = re.search(pattern, user_agent) # Match the search with the user agent found within the json file
                    if match: # If there is a match then
                        browser = match.group(1) # Extract the browser name
                        return "Trident" if browser == "Trident" else browser # Exception handler for this broswer due to error
                    return "Other" # Else if there is no match then simply return with other
            except Exception:
                return "Other" # If some error occurs during pattern matching then simply return with others

        self.data_handler.data['parsed_browser'] = self.data_handler.data['visitor_useragent'].apply(parse_browser) # Create a new column with the parsed browser and agent

        browser_counts = self.data_handler.data['parsed_browser'].value_counts() # Count the instances of each browser within the parsed browser column

        if browser_counts.empty: # If the browser count is empty within the parse column then 
            messagebox.showwarning("No Data", "No browser data available.") # Print error message
            return # Exit the function

        top_browsers = browser_counts.head(10) # Within the broswer count the top 10 most used browsers
        other_count = browser_counts.iloc[10:].sum() # Sum all the top 10 most used browsers
        if other_count > 0: # If the other category is more than 0 then
            top_browsers["Other"] = other_count # Add the other browsers and place them into a seperate other category

        chart_title = "Detailed Browser Usage Histogram" if detailed else "Simplified Browser Histogram" # For the detailed browser print the detailed title else the simplified titile
        self.visualization_handler.plot_bar_chart(top_browsers, chart_title, "Browser", "Count") # Build a histogram and plot the data with the top browsers and their specific usage counts
