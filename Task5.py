from tkinter import messagebox

class Task5:
    def __init__(self, data_handler, task4):
        self.data_handler = data_handler # Store data handler to access dataset
        self.task4 = task4 # Store visualization handler to access plotting

    def generate_dot_file(self, input_document, user_uuid=None, output_file="also_likes_graph.dot"):
        if self.data_handler.data is None: # If there is no data to read or loaded then
            messagebox.showerror("Error", "No data loaded. Please load a JSON file first.") # Print error message to warn the user
            return # Exit the function
        
        total_entries = self.data_handler.data.shape[0] # Get the total number of entries within the given dataset
        total_entries_k = f"{total_entries // 1000}k" if total_entries >= 1000 else f"{total_entries}" # Format the total number in the thousands so 1k,2k and so on

        dot_lines = [ # GRaph customizations
            "digraph AlsoLikes {", # Dot graph format
            "node [shape=circle];", # Node shape is circle
            "subgraph cluster_static_section {", # Subgraph for static labels
            "style=invis;", # SUbgraph is invisible
            '"Readers" [shape=plaintext, fontsize=16];', # Labels (Readers)
            '"Documents" [shape=plaintext, fontsize=16];', # Labels (DOcuments)
             f'"Readers" -> "Documents" [label="Size: {total_entries_k}"];', # Edge between readers and documents with the total size of the dataset
            "}",
        ]

        input_doc_short = input_document[-4:] # Last for hex characters as input for the graph
        dot_lines.append(f'"{input_doc_short}" [style=filled, fillcolor=green];') # Input document is green colour

        added_documents = set() # Trackers to avoid duplication (Documents)
        added_readers = set() # Trackers to avoid duplication (Readers)

        readers = self.task4.get_readers_of_document(input_document) # Get all the readers for the specified document UUID

        if not readers: # If there are no readers then
            messagebox.showinfo("No Readers", "No readers found for the input document.") # Print out message telling the user no visitors found
            return # Exit the function

        for reader in readers: # Loop through the readers of the document and then
            reader_short = reader[-4:] # Print out the last 4 hex characters only
            if reader == user_uuid: # If the reader is the specified vistor UUID then
                dot_lines.append(f'"{reader_short}" [style=filled, fillcolor=green, shape=rect];') # Make the node green and rectangular
                dot_lines.append(f'"{reader_short}" -> "{input_doc_short}";') # connect the reader to to the input doc via a arrow
                added_readers.add(reader_short) # Track the reader as added to prevent duplication
            else: # if the reader is not specified within the visitor UUID then
                dot_lines.append(f'"{reader_short}" [shape=rect];') # Make the node rectangular
                dot_lines.append(f'"{reader_short}" -> "{input_doc_short}";') # connect the reader to to the input doc via a arrow
                added_readers.add(reader_short) # Track the reader as added to prevent duplication

                documents_read = self.task4.get_documents_read_by_visitor(reader) # Get documents read by the current visitor

                for document in documents_read: # For loop through each document read by the visitor
                    if document != input_document: # if the document is the input document then skip else
                        document_short = document[-4:] # Get the last 4 hex of the document
                        dot_lines.append(f'"{reader_short}" -> "{document_short}";') # And connect the reader to the document
                        if document not in added_documents: # If the document is not added then
                            dot_lines.append(f'"{document_short}" [label="{document_short}"];') # Add the document as a node with the shortened name (last 4 hex) 
                            added_documents.add(document) # Track the document as added to prevent duplication

        dot_lines.append("}") # Close the graph once done

        with open(output_file, "w") as f:
            f.write("\n".join(dot_lines)) # write the dot file out

        messagebox.showinfo("DOT File Generated", f"DOT file '{output_file}' has been saved.") # Print out a message informing user the graph generation is done
