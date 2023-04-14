import tkinter as tk

def display_text():
    text = input_text.get()
    output_label.config(text=text)

# Create main application window
app = tk.Tk()
app.title("Input and Output")

# Create an Entry widget for user input
input_text = tk.StringVar()
input_entry = tk.Entry(app, textvariable=input_text)
input_entry.pack(padx=20, pady=10)

# Create a button to display the input text
display_button = tk.Button(app, text="Display", command=display_text)
display_button.pack(pady=5)

# Create a Label widget to display the output text
output_label = tk.Label(app, text="")
output_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
