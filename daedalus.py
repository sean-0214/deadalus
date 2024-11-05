import tkinter as tk
import keyboard
import webbrowser
import re  # Import the regular expressions module

# Global variable to store the previous transparency state
previous_alpha = 0.3

def toggle_transparent_window():
    global previous_alpha
    
    if window.attributes("-alpha") == previous_alpha:
        # If the current transparency is the same as the previous one, toggle to fully visible
        window.attributes("-alpha", 1)
        window.deiconify()  # Make the window visible
    else:
        # If the current transparency is different, toggle to the previous transparency state
        window.attributes("-alpha", previous_alpha)
        window.iconify()  # Minimize the window to the taskbar

def search_items():
    items = input_text.get("1.0", "end").splitlines()
    for item in items:
        item = item.strip()  # Remove leading and trailing whitespaces
        
        # Check if the item matches a URL pattern
        if re.match(r"https?://", item):
            webbrowser.open_new_tab(item)  # Open the URL directly
        else:
            webbrowser.open_new_tab("https://www.google.com/search?q=" + item)  # Search the item on Google

window = tk.Tk()
window.title("Daedalus")  # Window title
window.geometry("600x400+100+100")  # Initial size and position of the window
window.resizable(False, False)  # Disable window resizing

input_text = tk.Text(window, wrap="word", height=10, width=60)
input_text.pack(pady=10)

search_button = tk.Button(window, text="Search", command=search_items)
search_button.pack()

keyboard.add_hotkey('ctrl+shift+/', toggle_transparent_window)

# Set initial transparency to 30%
window.attributes("-alpha", 0.3)

window.mainloop()
