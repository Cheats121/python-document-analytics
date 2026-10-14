import matplotlib.pyplot as plt

class VisualizationHandler:
    @staticmethod
    def plot_histogram(data, title, xlabel, ylabel):
        if not data: # if no data is available then
            print("No data available to plot.") # Print error message stating no data to plot
            return # Exit the function
        plt.figure(figsize=(10, 6)) # Figure size
        plt.bar(data.keys(), data.values(), color='skyblue') # Creates histogram with bars of colour sky blue
        plt.title(title) # Title of the histogram
        plt.xlabel(xlabel) # X axis label
        plt.ylabel(ylabel) # Y axis label
        plt.xticks(rotation=45, ha='right') # Rotate X axis labels to 45 degrees
        plt.tight_layout() # prevent overlapping of labels and title
        plt.show() # Show the histogram

    @staticmethod
    def plot_bar_chart(data_series, title, xlabel, ylabel):
        plt.figure(figsize=(10, 6)) # Figure size
        data_series.plot(kind='bar', color='skyblue') # Creates bar chart with bars of colour sky blue 
        plt.title(title) # Title of the bar chart
        plt.xlabel(xlabel) # X axis label
        plt.ylabel(ylabel) # Y axis label
        plt.xticks(rotation=45) # Rotate X axis labels to 45 degrees
        plt.tight_layout() # prevent overlapping of labels and title
        plt.show() # Show the histogram
