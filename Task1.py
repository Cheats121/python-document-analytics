from tkinter import messagebox # Import messagebox module from tkinter

# COUNTRIES/CONTINENTS *****

class Task1:
    def __init__(self, data_handler, visualization_handler):
        self.data_handler = data_handler # Store data handler to access dataset
        self.visualization_handler = visualization_handler # Store visualization handler to access plotting

    def view_by_country(self, doc_uuid):
        if self.data_handler.data is None : # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return # Exit the function

        filtered_data = self.data_handler.filter_by_document(doc_uuid) # Filter the dataset to find the document UUID mentioned withion the text box
        if filtered_data is None or filtered_data.empty: # If the document UUID is not found within the dataset then
            messagebox.showwarning("No Data Found", f"No data found for Document UUID: {doc_uuid}") # Print the error with the document UUID to warn the user
            return # Exit the function

        
        country_counts = filtered_data['visitor_country'].value_counts() # Count the number of views for each country mentioned for the document UUID

       
        self.visualization_handler.plot_bar_chart(country_counts, "Views by Country", "Country", "Views") # Build a histogram and plot the data with the country names and their specific view counts

    def view_by_continent(self, doc_uuid):
        
        if self.data_handler.data is None: # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return # Exit the function

        filtered_data = self.data_handler.filter_by_document(doc_uuid)
        if filtered_data is None or filtered_data.empty: # If the document ID is not found within the dataset then
            messagebox.showwarning("No Data Found", f"No data found for Document UUID: {doc_uuid}") # Print the error with the document ID to warn the user
            return # Exit the function

        # Please note it was hard to find a more dynamic way to map these countried to their respective continets hence why the static mapping!!
        country_to_continent = { # Mapping of countries to their continents (Static)
            'US': 'North America',
            'IN': 'Asia',
            'CA': 'North America',
            'CO': 'South America',
            'PE': 'South America',
            'MX': 'North America',
            'AR': 'South America',
            'CL': 'South America',
            'GT': 'North America',
            'PA': 'North America',
            'JM': 'North America',
            'BR': 'South America',
            'VE': 'South America',
            'FR': 'Europe',
            'KR': 'Asia',
            'SG': 'Asia',
            'TH': 'Asia',
            'VN': 'Asia',
            'ES': 'Europe',
            'IT': 'Europe',
            'DE': 'Europe',
            'UK': 'Europe',
            'NL': 'Europe',
            'SE': 'Europe',
            'ID': 'Asia',
            'ZA': 'Africa',
            'NG': 'Africa',
            'EG': 'Africa',
            'KE': 'Africa',
            'GH': 'Africa',
            'MA': 'Africa',
            'CH': 'Europe',
            'JP': 'Asia',
            'CN': 'Asia',
            'MY': 'Asia',
            'DZ': 'Africa',
            'AU': 'Oceania',
            'NZ': 'Oceania',
            'CU': 'North America',
            'DO': 'North America',
            'FJ': 'Oceania',
            'PG': 'Oceania',
            'AE': 'Asia',
            'SA': 'Asia',
            'IR': 'Asia',
            'TR': 'Asia',
            'IL': 'Asia',
            'TT': 'North America',
        }
        filtered_data['continent'] = filtered_data['visitor_country'].map(country_to_continent) # Map the countries to their respective continent column using dictionary
        continent_counts = filtered_data['continent'].value_counts() # COunts the number of views for each continent

        self.visualization_handler.plot_bar_chart(continent_counts, "Views by Continent", "Continent", "Views") # Build a histogram and plot the data with the continents and their specific view counts
