import argparse
import sys
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, Frame
from Task1 import Task1
from Task2 import Task2
from Task3 import Task3
from Task4 import Task4
from Task5 import Task5
from TaskExtra1 import ExtraTask1
from TaskExtra2 import ExtraTask2
from TaskExtra3 import ExtraTask3
from TaskExtra4 import ExtraTask4
from TaskExtra5 import ExtraTask5
from DataHandler import DataHandler
from VisualizationHandler import VisualizationHandler


class DocumentViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("F20SC Group 17 Document Tracker Analysis Tool") # Window Title
        self.root.geometry("1149x700") # Window default size
        self.root.configure(bg="#FFFFFF") # Background colour

        self.data_handler = DataHandler() # Initialize DataHandler
        self.visualization_handler = VisualizationHandler() # Initialize VizualizationHandler

        self.default_bg = "#f9f9f9"  # Default background color for other buttons
        self.default_fg = "#4B4A67"  # Default foreground color for other buttons

        self.json_button_bg = "#11df02"  # Green background color for the JSON button
        self.json_button_fg = "#FFFFFF"  # White foreground color for the JSON button

        self.create_ui() # Create the user interface method

        self.task1 = Task1(self.data_handler, self.visualization_handler) # Task 1
        self.task2 = Task2(self.data_handler, self.visualization_handler) # Task 2
        self.task3 = Task3(self.data_handler, self.visualization_handler) # Task 3
        self.task4 = Task4(self.data_handler, self.visualization_handler) # Task 4
        self.task5 = Task5(self.data_handler, self.task4) # Task 5
        self.task_extra = ExtraTask1(self.data_handler, self.visualization_handler) # Task 1 Extra
        self.task_extra_2 = ExtraTask2(self.data_handler, self.visualization_handler) # Task 2 Extra
        self.task_extra_3 = ExtraTask3(self.data_handler, self.visualization_handler) # Task 3 Extra
        self.task_extra_4 = ExtraTask4(self.data_handler, self.visualization_handler) # Task 4 Extra
        self.task_extra_5 = ExtraTask5(self.data_handler, self.visualization_handler) # Task 5 Extra

        
##################################### UI CUSTOMIZATION (START) ###############################################

    def create_ui(self):
        ############################### LEFT PANEL ##########################################
        left_panel = Frame(self.root, bg="#007BFF", width=400, relief="solid", bd=1) # Left side panel
        left_panel.pack(side="left", fill="y") # Position Frame left and fill vertically

        Label( # Left Panel information
            left_panel,
            text="Welcome to Document Tracker",
            bg="#007BFF",
            fg="#FFFFFF",
            font=("Arial", 16, "bold"),
        ).pack(pady=30, padx=20, anchor="n")

        Label( # Left Panel information
            left_panel,
            text=(
                "This tool provides data analysis for a given document\n" 
                "\n"
                "Features include:\n\n"
                "- Country analysis\n"
                "- Browser analysis\n"
                "- Reader insights\n"
                "- Document insights\n"
                "- Graph generation\n\n"
                "- Top Readers/Documents\n"
                "- Top 10 insights\n"
                "\n\n"
                "Explore your data efficiently!"
            ),
            bg="#007BFF",
            fg="#FFFFFF",
            font=("Arial", 12),
            justify="left",
        ).pack(padx=20, pady=10, anchor="n")

        Label( # Left Panel information
            left_panel,
            text="Made by Varun Senthil Kumar and Joseph Emmanuel\n"
                 "F20SC Group-17\n",
            bg="#007BFF",
            fg="#FFFFFF",
            font=("Arial", 10, "italic"),
        ).pack(pady=50, padx=20, anchor="s")

        ############################### RIGHT PANEL ##########################################
        right_panel = Frame(self.root, bg="#FFFFFF") # Right side panel
        right_panel.pack(side="right", fill="both", expand=True) # Position Frame right, fill vertically and horizontaly and expand

        right_panel.grid_columnconfigure(0, weight=1)
        right_panel.grid_columnconfigure(1, weight=1) #######
        for row in range(10): 
            right_panel.grid_rowconfigure(row, weight=1)

        Label( # Right Panel information
            right_panel,
            text="Enter the Details",
            bg="#FFFFFF",
            fg="#4B4A67",
            font=("Arial", 16, "bold"),
        ).grid(row=0, column=0, columnspan=2, pady=20, padx=5, sticky="n")

        self.create_input_field(right_panel, "Document UUID:", "doc_uuid_entry", row=1) # Document UUID Field
        self.create_input_field(right_panel, "Visitor UUID:", "visitor_uuid_entry", row=2) # Visitor UUID Field

        Button( # Right Panel information (JSON BUTTON)
            right_panel,
            text="Load JSON File",
            bg=self.json_button_bg,  
            fg=self.json_button_fg,
            font=("Roboto", 12, "bold"),
            command=self.load_data,
        ).grid(row=3, column=0, columnspan=2, pady=10, padx=10)

        self.create_feature_buttons(right_panel) # Creates the button

    def create_input_field(self, parent, label_text, attribute_name, row): # Input Field customizations
        """Helper method to create labeled input fields."""
        label = Label(parent, text=label_text, bg="#FFFFFF", fg="#4B4A67", font=("Arial", 12))
        label.grid(row=row, column=0, padx=10, pady=10, sticky="e")

        entry = Entry(parent, bg="#F8F8F8", fg="#4B4A67", relief="flat", width=70)
        entry.grid(row=row, column=1, padx=10, pady=10, sticky="w")
        setattr(self, attribute_name, entry)

    def create_feature_buttons(self, parent): # Section for buttons for functionality
        feature_section = Frame(parent, bg="#FFFFFF")
        feature_section.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=20)

        for row in range(8):  # Grid layout for the buttons
            feature_section.grid_rowconfigure(row, weight=1)
        for col in range(2):  # 2 in each side of the grid
            feature_section.grid_columnconfigure(col, weight=1)

        tasks = [ # All the buttons for the functionality
            ("Task 2: View by Country", self.view_by_country),
            ("Task 2: View by Continent", self.view_by_continent),
            ("Task 3: Browser Analysis (Detailed)", self.show_detailed_browser_histogram),
            ("Task 3: View Browser (Symplified)", self.show_generic_browser_histogram),
            ("Task 4: View Top Readers", self.view_top_readers),
            ("Task 5: Get Readers of Document", self.get_readers_button),
            ("Task 5: Get Documents of Visitor", self.get_documents_button),
            ("Task 5: Show Also Likes (5c)", self.show_task_5c),
            ("Task 5: Top 10 Also Likes (5d)", self.show_task_5d),
            ("Task 6: Generate DOT File", self.generate_dot_file),
            ("Task Ex1: Most Popular Devices", self.find_most_popular_devices),
            ("Task EX2: Most Popular Sources", self.find_most_popular_sources),
            ("Task EX3: Most Popular Countries", self.find_most_popular_countries),
            ("Task EX4: Most Popular Referrers", self.find_most_popular_referrers),
            ("Task EX5: Top Visited Documents", self.find_top_visited_documents),
        ]

        for idx, (label, command) in enumerate(tasks): # Loop to customize all the buttons the same (Efficiency)
            row = idx // 2  
            column = idx % 2 
            button = Button(
                feature_section,
                text=label,
                width=30,
                bg=self.default_bg,
                fg=self.default_fg,
                font=("Roboto", 10),
                cursor="hand2",
                command=command,
            )
            button.grid(row=row, column=column, padx=5, pady=10)

##################################### UI CUSTOMIZATION (END) ###############################################

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")]) # Open files to select the file
        if not file_path: # If incorrect file is slected or no file selected then
            messagebox.showinfo("No File Selected", "Please select a valid JSON file.") # Error displayed to the user
            return # Exit the fucntion
        if self.data_handler.load_data(file_path): # If file is selected and loaded then
            messagebox.showinfo("Success", "Data loaded successfully!") # Sucess if file is loaded
        else: # Else if it fails
            messagebox.showerror("Error", "Failed to load data.") # Failed if file is not loaded

    # Task 1
    def view_by_country(self):
        doc_uuid = self.doc_uuid_entry.get().strip() # Retrive the document UUID from the input field
        if doc_uuid: # If the document UUID is valid then
            self.task1.view_by_country(doc_uuid) # Call the method view_by_country

    def view_by_continent(self):
        doc_uuid = self.doc_uuid_entry.get().strip() # Retrive the document UUID from the input field
        if doc_uuid: # If the document UUID is valid then
            self.task1.view_by_continent(doc_uuid) # Call the method view_by_continent

    # Task 2
    def show_detailed_browser_histogram(self):
        try: # Try block to catch any errors
            self.task2.show_browser_histogram(detailed=True) # If True button clicked then generate show_browser_histogram (Detailed)
        except Exception as e: # Else if it doesnt generate
            messagebox.showerror("Error", f"An error occurred while generating the detailed browser histogram: {e}") # Throw exception error to user

    def show_generic_browser_histogram(self):
        try: # Try block to catch any errors
            self.task2.show_browser_histogram(detailed=False) # If False button clicked then generate show_browser_histogram (Simplified)
        except Exception as e: # Else if it doesnt generate
            messagebox.showerror("Error", f"An error occurred while generating the generic browser histogram: {e}") # Throw exception error to user

    # Task 3
    def view_top_readers(self):
        self.task3.view_top_readers() # Call method view_top_readers to display top readers in the dataset

    # Task 4
    def get_readers_button(self):
        doc_uuid = self.doc_uuid_entry.get().strip() # Retrive the document UUID from the input field
        if doc_uuid: # If the document UUID is valid then
            self.task4.get_readers_button(doc_uuid) # Call the method get_readers_button

    # Task 4
    def get_documents_button(self):
        visitor_uuid = self.visitor_uuid_entry.get().strip() # Retrive the visitor UUID from the input field
        if visitor_uuid: # If the visitor UUID is valid then
            self.task4.get_documents_button(visitor_uuid) # Call the method get_documents_button

    def show_task_5c(self):
        doc_uuid = self.doc_uuid_entry.get().strip() # Retrive the document UUID from the input field
        visitor_uuid = self.visitor_uuid_entry.get().strip() # Retrive the visitor UUID from the input field
        self.task4.show_task_5c_also_likes_list(doc_uuid, visitor_uuid) # Call the method show_task_5c_also_likes_list

    def show_task_5d(self):
        doc_uuid = self.doc_uuid_entry.get().strip() # Retrive the document UUID from the input field
        visitor_uuid = self.visitor_uuid_entry.get().strip() # Retrive the visitor UUID from the input field
        self.task4.show_task_5d_also_likes_list(doc_uuid, visitor_uuid)  # Call the method show_task_5d_also_likes_list

    # Task 5
    def generate_dot_file(self):
        doc_uuid = self.doc_uuid_entry.get().strip() # Retrive the document UUID from the input field
        user_uuid = self.visitor_uuid_entry.get().strip() # Retrive the visitor UUID from the input field
        if doc_uuid: # If the document UUID is valid then
            self.task5.generate_dot_file(doc_uuid, user_uuid if user_uuid else None) # call the method generate_dot_file and generate dot file

    def find_most_popular_devices(self):
        try: # Try block to catch any errors
            self.task_extra.find_most_popular_devices() # Call method find_most_popular_devices to display popular devices in the dataset
        except Exception as e: # Else if it doesnt generate
            messagebox.showerror("Error", f"An error occurred while finding the most popular devices: {e}") # Throw exception error to user

    def find_most_popular_sources(self):
        try: # Try block to catch any errors
            self.task_extra_2.find_most_popular_sources() # Call method find_most_popular_sources to display popular sources in the dataset
        except Exception as e: # Else if it doesnt generate 
            messagebox.showerror("Error", f"An error occurred while finding the most popular sources: {e}") # Throw exception error to user


    def find_most_popular_countries(self):
        try: # Try block to catch any errors
            self.task_extra_3.find_most_popular_countries() # Call method find_most_popular_countries to display popular countries in the dataset
        except Exception as e: # Else if it doesnt generate
            messagebox.showerror("Error", f"An error occurred while finding the most popular countries: {e}") # Throw exception error to user

    def find_most_popular_referrers(self):
        try: # Try block to catch any errors
            self.task_extra_4.find_most_popular_referrers() # Call method find_most_popular_referrers to display popular referrers in the dataset
        except Exception as e: # Else if it doesnt generate
            messagebox.showerror("Error", f"An error occurred while finding the top 10 visitor referrers: {e}") # Throw exception error to user

    def find_top_visited_documents(self):
        try: # Try block to catch any errors
            self.task_extra_5.find_top_visited_documents() # Call method find_top_visited_documents to display popular referrers in the dataset
        except Exception as e: # Else if it doesnt generate
            messagebox.showerror("Error", f"An error occurred: {e}") # Throw exception error to user



class Task8CommandLine:
    def __init__(self):
        self.data_handler = DataHandler() # Initialize DataHandler for CLI
        self.visualization_handler = VisualizationHandler() # Initialize VizualizationHandler for CLI

        self.task1 = Task1(self.data_handler, self.visualization_handler) # Task 1 (CLI)
        self.task2 = Task2(self.data_handler, self.visualization_handler) # Task 2 (CLI)
        self.task3 = Task3(self.data_handler, self.visualization_handler) # Task 3 (CLI)
        self.task4 = Task4(self.data_handler, self.visualization_handler) # Task 4 (CLI)
        self.task5 = Task5(self.data_handler, self.task4) # Task 5 (CLI)
        self.task_extra = ExtraTask1(self.data_handler, self.visualization_handler) # Task 1 Extra (CLI)
        self.task_extra_2 = ExtraTask2(self.data_handler, self.visualization_handler) # Task 2 Extra (CLI)
        self.task_extra_3 = ExtraTask3(self.data_handler, self.visualization_handler) # Task 3 Extra (CLI)
        self.task_extra_4 = ExtraTask4(self.data_handler, self.visualization_handler) # Task 4 Extra (CLI)
        self.task_extra_5 = ExtraTask5(self.data_handler, self.visualization_handler) # Task 5 Extra (CLI)

    def execute_task(self, args):
        if not self.data_handler.load_data(args.file_name): # If the file is not loaded or incorect file is given
            print("Failed to load data poease ensure the file path is correct.") # Print out error stating the issue to the user
            return # Exit the function

        if args.task_id == "2a": # If the task ID is 2a then
            if args.doc_uuid: # If the document UUID is valid then
                self.task1.view_by_country(args.doc_uuid) # call the method view_by_country
            else: # else if not valid then
                print("Task 2a requires a Document UUID (-d).") # Print out error to user
        elif args.task_id == "2b": # If the task ID is 2b then
            if args.doc_uuid: # If the document UUID is valid then
                self.task1.view_by_continent(args.doc_uuid) # call the method view_by_continent
            else: # else if not valid then
                print("Task 2b requires a Document UUID (-d).") # Print out error to user
        elif args.task_id == "3a": # If the task ID is 3a then
            self.task2.show_browser_histogram(detailed=True) # call the method show_browser_histogram (detailed)
        elif args.task_id == "3b": # Else if the task ID is 3a then
            self.task2.show_browser_histogram(detailed=False) # call the method show_browser_histogram (simplified)
        elif args.task_id == "4": # If the task ID is 4 then
            self.task3.view_top_readers() # call the method view_top_readers
        elif args.task_id == "5d": # If the task ID is 5 then
            if args.doc_uuid: # If the document UUID is valid then
                self.task4.show_task_5d_also_likes_list(args.doc_uuid, args.user_uuid) # call the method show_task_5d_also_likes_list
            else: # else if not valid then
                print("Task 5d requires a Document UUID (-d).") # Print out error to user
        elif args.task_id == "6": # If the task ID is 6 then
            if args.doc_uuid: # If the document UUID is valid then
                self.task5.generate_dot_file(args.doc_uuid, args.user_uuid) # call the method generate_dot_file
            else: # else if not valid then
                print("Task 6 requires a Document UUID (-d).")  # Print out error to user
        elif args.task_id == "7":
            if args.doc_uuid: # If the document UUID is valid then
                self.task5.generate_dot_file(args.doc_uuid, args.user_uuid) # call the method generate_dot_file again
                print("dot file has been generated....opening GUI")
                import tkinter as tk
                gui_root = tk.Tk() # Launch GUI (tkinter)
                gui_app = DocumentViewerApp(gui_root) # Initalize GUI application
                gui_root.mainloop() # Start the GUI application loop
            else:
                print("Task 7 requires a Document UUID (-d).")
        elif args.task_id == "ex1": # If the task ID is ex1 then
            self.task_extra.find_most_popular_devices() # call the method find_most_popular_devices
        elif args.task_id == "ex2": # If the task ID is ex2 then
            self.task_extra_2.find_most_popular_sources() # call the method find_most_popular_sources
        elif args.task_id == "ex3": # If the task ID is ex3 then
            self.task_extra_3.find_most_popular_countries() # call the method find_most_popular_countries
        elif args.task_id == "ex4": # If the task ID is ex4 then
            self.task_extra_4.find_most_popular_referrers() # call the method find_most_popular_referrers
        elif args.task_id == "ex5": # If the task ID is ex5 then
            self.task_extra_5.find_top_visited_documents() # call the method find_top_visited_documents
        else:
            print(f"Unknown task ID: {args.task_id}. Please provide a valid task ID.") # If wrong task id is provided then handle error cases

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description="Document Tracker Analysis Tool - CLI") # Description
        parser.add_argument("-u", "--user_uuid", type=str, help="Visitor UUID for tasks requiring a user ID") # Visitor UUID (Optional)
        parser.add_argument("-d", "--doc_uuid", type=str, help="Document UUID for tasks requiring a document ID") # DOcument UUID
        parser.add_argument("-t", "--task_id", type=str, required=True, help="Task ID (e.g., 2a, 2b, 3a, 3b, 4, 5d, 6, ex1, ex2, ex3, ex4, ex5.)") # Task ID
        parser.add_argument("-f", "--file_name", type=str, required=True, help="Please give a JSON file containing the document tracking data") # File for processing
        return parser.parse_args()

if __name__ == "__main__":
    if len(sys.argv) > 1:  # If the length of the command is more than 1 then
        task8 = Task8CommandLine() # Call Task8CommandLine class to handle CLI usage
        args = Task8CommandLine.parse_arguments() # Parse the arguments to the CLI
        task8.execute_task(args) # Execute the parsed arguments
    else:  # Default to launching the GUI
        root = Tk() # Create the tkinter application
        app = DocumentViewerApp(root) # Instantiate DocumentViewerApp class
        root.mainloop() # Keep the application running after every action
