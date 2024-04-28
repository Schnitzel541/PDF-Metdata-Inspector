import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import PyPDF2

def get_metadata(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            document_info = pdf.metadata
            metadata = {
                "Title": document_info.get('/Title', None),
                "Author": document_info.get('/Author', None),
                "Creator": document_info.get('/Creator', None),
                "Creation Date": document_info.get('/CreationDate', None),
                "Producer": document_info.get('/Producer', None)
            }
            return {k: v for k, v in metadata.items() if v is not None}
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read PDF file: {e}")
        return None

def load_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    tree.delete(*tree.get_children())  
    
    # Clear existing entries in the tree
    if file_path:
        metadata = get_metadata(file_path)
        if metadata:
            for i, (k, v) in enumerate(metadata.items()):
                tree.insert("", 'end', values=(k, v))
        else:
            messagebox.showinfo("No Metadata", "No metadata found or unable to read PDF.")

# Setting up the main application window
app = tk.Tk()
app.title("PDF Metadata Reader")
app.geometry("800x600")

# Frame to hold other widgets
frame = ttk.Frame(app)
frame.pack(pady=20)

# Treeview to display metadata
tree = ttk.Treeview(frame, columns=("Property", "Value"), show="headings")
tree.heading("Property", text="Property")
tree.heading("Value", text="Value")
tree.column("Property", width=100, anchor="center")
tree.column("Value", width=400, anchor="w")
tree.pack(expand=True, fill='both')

# Button to load PDF and display metadata
btn_load = ttk.Button(app, text="Load PDF", command=load_pdf)
btn_load.pack(fill='x', expand=True, padx=20, pady=10)

# Start the Tkinter event loop
app.mainloop()
