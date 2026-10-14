from tkinter import messagebox
from collections import Counter

# ALSO LIKES / A,B,C,D *****

class Task4:
    def __init__(self, data_handler, visualization_handler):
        self.data_handler = data_handler # Store data handler to access dataset
        self.visualization_handler = visualization_handler # Store visualization handler to access plotting

    def get_readers_of_document(self, doc_uuid):
        if not doc_uuid: # If no document UUID is provided then
            messagebox.showwarning("Input Required", "Please enter a Document UUID.") # Print error message to warn the user to provide a document UUID
            return [] # Exit the function
        
        if self.data_handler.data is None: # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return [] # Exit the function

        readers = self.data_handler.data[ # When reading through the data filter
            (self.data_handler.data['event_type'] == 'read') & # People who have done the event type read
            (self.data_handler.data['subject_doc_id'] == doc_uuid) # And get the document UUID 
        ]
        return list(readers['visitor_uuid'].unique()) # Return the visitor UUID (In unique)

    def get_documents_button(self, visitor_uuid=None):
        if not visitor_uuid: # If no visitor UUID is provided then
            messagebox.showwarning("Input Optional", "No Visitor UUID provided. Showing all readers.") # Print error message to warn the user
            document_counts = self.data_handler.data['subject_doc_id'].value_counts().to_dict() # Count the number of instances of the document ID and put it into a dictionary
        else: # Else if the visitor UUID is provided then
            documents = self.get_documents_read_by_visitor(visitor_uuid) # Get documents read by the specified visitor UUID
            if not documents: # If no documents found then
                messagebox.showinfo("No Data", "No documents found for this visitor.") # Print error message warning the user
                return # Exit function
            filtered_data = self.data_handler.data[self.data_handler.data['visitor_uuid'] == visitor_uuid] # Filter data to include only the visitor UUID that matches the visitor UUID
            document_counts = filtered_data['subject_doc_id'].value_counts().to_dict() # Count the instances read by the visitor UUID and place it into the dictionary

        self.visualization_handler.plot_histogram( # Make a histogram of the data visually
            document_counts, "Documents Read by Visitor", "Documents", "Read Count" # Labels for the histogram
        )

    def get_also_likes(self, doc_uuid, visitor_uuid=None, sorting_function=None):
        if self.data_handler.data is None: # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return [] # Exit the function

        readers = self.get_readers_of_document(doc_uuid) # Get the readers of the specified document UUID by calling the get readers function
        if not readers: # If no readers available then
            return [] # Exit the function return nothing

        if visitor_uuid: # If the visitor UUID is provided then
            readers = [reader for reader in readers if reader == visitor_uuid] # Filter the readers to the specifed Visitor UUID

        if not readers: # If there are no readers then
            return [] # Return empty and exit

        related_documents = self.data_handler.data[self.data_handler.data['visitor_uuid'].isin(readers)] # Filter the data to include only visitor UUID in the list of readers
        related_documents = related_documents[related_documents['subject_doc_id'] != doc_uuid] # Exclude any rows where subject doc UUID matches the mentioned document UUID
        related_doc_counts = related_documents['subject_doc_id'].value_counts() # Count the instances of each document UUID within the filtered data

        related_doc_list = list(related_doc_counts.items()) # Conver the document into a list (document UUID and count)
        if sorting_function: # If sorting function is provided
            related_doc_list = sorted(related_doc_list, key=lambda x: sorting_function(x[1]), reverse=True) # Sort the list baed on the count using the sorting function in descending order

        return related_doc_list # Return the sorted list


    def get_documents_read_by_visitor(self, visitor_uuid=None):
        if self.data_handler.data is None: # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return [] # Exit the function

        if not visitor_uuid: # If no visitor UUID is provided then
            messagebox.showwarning("Input Optional", "Visitor UUID not provided. Returning all documents.") # Print error message to warn the user
            documents = self.data_handler.data[self.data_handler.data['event_type'] == 'read'] # Within the document look for the event type read
        else:
            documents = self.data_handler.data[ # When reading through the data filter
                (self.data_handler.data['event_type'] == 'read') & # People who have done the event type read
                (self.data_handler.data['visitor_uuid'] == visitor_uuid) # And get the visitor UUID 
            ]
        
        return list(documents['subject_doc_id'].unique()) # Return the document UUID (In unique)
    
    def get_readers_button(self, doc_uuid):
        if not doc_uuid: # if no document UUID is provided then
            messagebox.showwarning("Input Required", "Please enter a Document UUID.") # Warn the user about the error
            return # Exit the function
        
        if not doc_uuid: # if no document UUID is provided then
            messagebox.showwarning("Input Required", "Please enter a Document UUID.") # Warn the user about the error
            return # Exit the function

        readers = self.get_readers_of_document(doc_uuid) # Get the readers of the specified document UUID

        if not readers: # If no readers are found then
            messagebox.showinfo("No Readers", "No readers found for this document.") # Print out error stating the issue
            return
        filtered_data = self.data_handler.data[self.data_handler.data['subject_doc_id'] == doc_uuid] # Filter data to include only the document UUID that matches the specified document UUID
        reader_counts = filtered_data['visitor_uuid'].value_counts().to_dict() # Count the instances of each visitor UUID and place it into the dictionary
        
        self.visualization_handler.plot_histogram( # Make a histogram of the data visually
            reader_counts, "Readers of Document", "Readers", "View Count" # Labels for the histogram
        )

    def also_likes(self, doc_uuid, visitor_uuid=None):
        also_likes_docs = [] # List to store documents (Document_UUID)
        also_likes_visitors = [] # List to store readers (visitor_UUIDS)

        if visitor_uuid is None: # If the visitor UUID is not mentioned
            try: # Try block to capture any issues or errors
                also_likes_visitors = self.get_readers_of_document(doc_uuid) # Get all the readers for the specified document
                for visitor in also_likes_visitors: # Then use a for loop to loop through each reader
                    visitor_docs = self.get_documents_read_by_visitor(visitor) # Get the documents read for each visitor
                    if visitor_docs: # Once all the docuemnts are foound then
                        also_likes_docs.extend(visitor_docs) # Add the visitors documents to the list
            except Exception as e: # Exception added to handle errors
                messagebox.showerror("Error", f"An error occurred while processing: {e}") # Print out error stating the issue 
        else: # Else if the visitor UUID is specified then
            visitor_docs = self.get_documents_read_by_visitor(visitor_uuid) # Get the document read by this specified visitor
            if visitor_docs: # Once the document is found then
                also_likes_docs.extend(visitor_docs) # Add these documents the list

        document_counts = Counter(also_likes_docs) # Count the instances of each document in the list
        sorted_docs = document_counts.most_common() # Sort the documents in descending order
        return sorted_docs # Return the documents within the list with the count
    

    def show_task_5c_also_likes_list(self, doc_uuid, visitor_uuid=None):
        if not doc_uuid: # if no document UUID is provided then
            messagebox.showwarning("Input Required", "Please enter a Document UUID.") # Warn the user about the error
            return # Exit the function

        also_likes = self.also_likes(doc_uuid, visitor_uuid) # Get the documents for the specified document UUID using the also_likes function (Optionally visitor UUID)

        if also_likes: # If there are documents related to the specified document and/or vistor UUID
            also_likes_list = "\n\n".join([f"{doc}: {count} readers" for doc, count in also_likes]) # Format to a readable string with the document UUID and reader count
            messagebox.showinfo("Task 5C: Also Liked Documents", f"Related Documents:\n--------------------------------------\n{also_likes_list}") # Print out the related documents
        else: # Else if no related documents are found within the also_likes function for the specified document UUID / Visitor UUID
            messagebox.showinfo("No Results", "No related documents found.") # Print out a message telling the user no documents are found


    def show_task_5d_also_likes_list(self, doc_uuid, visitor_uuid=None):
        if not doc_uuid: # if no document UUID is provided then
            messagebox.showwarning("Input Required", "Please enter a Document UUID.") # Warn the user about the error
            return # Exit the fucntion

        top_10_also_likes = self.also_likes_top_10(doc_uuid, visitor_uuid) # Get the top 10 documents for the specified document UUID using the also_likes_top_10 function (Optionally visitor UUID)

        if top_10_also_likes: # If there are documents related to the specified document and/or vistor UUID
            top_10_list = "\n\n".join([f"{doc}: {count} readers" for doc, count in top_10_also_likes]) # Format to a readable string with the document UUID and reader count
            messagebox.showinfo("Task 5D: Top 10 Also Liked Documents", f"Top 10 Documents:\n--------------------------------------\n{top_10_list}") # Print out the related documents
        else: # Else if no related documents are found within the also_likes_top_10 function for the specified document UUID / Visitor UUID
            messagebox.showinfo("No Results", "No related documents found.") # Print out a message telling the user no documents are found

            
    def also_likes_top_10(self, doc_uuid, visitor_uuid=None):
        try: # Try block to catch any errors
            all_also_likes = self.get_also_likes(doc_uuid, visitor_uuid) # Get the specified list documents from the get_also_likes function (Document UUID / Visitor UUID)
            top_10_docs = all_also_likes[:10] # Filter to the top 10 within the list
            return top_10_docs # Return the filtered list (top 10)
        except Exception as e: # If any errors then
            messagebox.showerror("Error", f"An error occurred while processing: {e}") # Print a error messsage warning the user
            return [] # Return empty list and exit function
