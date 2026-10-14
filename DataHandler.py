import pandas as pd

class DataHandler:
    def __init__(self):
        self.data = None # Data attribute to store the dataset

    def load_data(self, file_path, chunk_size=100000):
        try: # try block to capture any errors
            chunks = [] # list to store chunks of data file
            for chunk in pd.read_json(file_path, lines=True, chunksize=chunk_size): # JSON file is read in chunks in a for loop
                chunks.append(chunk)  # Append each chunk to the list.

            if not chunks: # If no chunks found then 
                raise ValueError("No data found in the file.") # Raise a error stating no data found

            self.data = pd.concat(chunks, ignore_index=True)  # Combine all chunks into one frame and reset index

            self.data = self.data.convert_dtypes() # COnvert column data for optimization
            return True # Return true if susccesfull
        except Exception as e: # Else return
            print(f"Error loading data: {e}") # Error to the user
            return False # And return false when failed
        
    def filter_by_document(self, doc_uuid):
        if self.data is None:  # If there is no data to read or loaded then 
            raise ValueError("Error No data loaded.") # Print out error to the user
        
        filtered_data = self.data[self.data['subject_doc_id'] == doc_uuid]
        return filtered_data if not filtered_data.empty else pd.DataFrame() # filter out the rows based on subject_doc_id and return the filtered data if its not empty else return nothing
    
    def get_readers_of_document(self, doc_uuid):
        filtered_data = self.filter_by_document(doc_uuid) # Get the filtered data for the specified document UUID
        return filtered_data['visitor_uuid'].unique() if filtered_data is not None else [] # Return the visitor UUID for that document else nothing
