import tk
from tk import messagebox

# Create the main application window
root = tk.Tk()

def popup_window():
    messagebox.showinfo("Popup", "This is a popup window!")

# Create a button to trigger the popup
popup_button = tk.Button(root, text="Show Popup", command=popup_window)
popup_button.pack()

# Run the main event loop
root.mainloop()
