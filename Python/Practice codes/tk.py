# # from tkinter import Tk, messagebox

# # # Initialize Tkinter root (required for messagebox to work)
# # root = Tk()
# # root.withdraw()  # Hide the main window

# # # Display an info dialog
# # messagebox.showinfo(title="Information", message="This is an info message!")

# # # now creating a chatinterface in tkinter using python
# from tkinter import *
# from tkinter import messagebox

# # Create a window
# root = Tk()
# root.title("Chat Interface")
# root.geometry("400x500")

# # # Create a chat window
# # chatWindow = Text(root, bd=1, bg="white", width=50, height=8)
# # chatWindow.place(x=6, y=6, height=385, width=370)

# # # Create a message window
# # messageWindow = Text(root, bg="white", width=30, height=4)
# # messageWindow.place(x=128, y=400, height=88, width=260)

# # # Create a send button
# # sendButton = Button(root, text="Send", bg="blue", activebackground="light blue", width=12, height=5)
# # sendButton.place(x=6, y=400, height=88)

# # # Create a scroll bar
# # scrollbar = Scrollbar(root, command=chatWindow.yview())
# # scrollbar.place(x=375, y=5, height=385)


# def on_click():
#     print("Button clicked!")

# button = Button(root, text="Click Me", command=on_click)
# button.pack()
# label = Label(button, text="Hello, Tkinter!")
# label.pack()

# root.mainloop()
import tkinter as tk
root = tk.Tk()

entry = tk.Entry(root)
entry.pack()
# frame = tk.Frame(root, bg="blue")
# frame.pack(fill="both", expand=True)
   

# # 6. *Canvas*: Draw shapes, lines, or images.

# canvas = tk.Canvas(root, width=300, height=200)
# canvas.pack()
# c
# anvas.create_rectangle(50, 50, 200, 150, fill="red")
# canvas.create_line(0, 0, 300, 200, fill="blue")
root.mainloop()

