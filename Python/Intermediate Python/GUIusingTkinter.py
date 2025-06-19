import tkinter as tk
from tkinter import ttk

# Function to display the message
def message():
    if not hasattr(message, 'message_label'):
        message.message_label = tk.Label(root, text="Button clicked!", font=("Arial", 16))
        message.message_label.pack(pady=(10, 10))
    else:
        message.message_label.config(text="Button clicked!")
        message.message_label.pack(pady=(10, 10))

# Create the main application window
root = tk.Tk()
root.title("An App")

# Create a Label widget with larger font
label = tk.Label(root, text="A simple GUIApp", font=("Arial", 16))
label.pack(pady=(10, 10))

# Create an Entry widget with larger font
entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=(10, 10))

# Create a Button widget with larger font
button = tk.Button(root, text="Click me!", font=("Arial", 16), command=message)
button.pack(pady=(10, 10))
 
# Start the Tkinter event loop
root.mainloop()


