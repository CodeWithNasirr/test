import tkinter as tk
from PIL import Image, ImageTk  # You'll need to install the 'Pillow' library for this

# Create the main window
root = tk.Tk()
root.title("Special Greeting")
root.geometry("600x400")  # Set the size of the window

# Set the background color
root.configure(bg="#ffe6e6")  # Light pink background color


image = Image.open("photo.png") # Replace 'photo.png' with the path to your image file
image = Image.open("1.png") # Replace 'photo.png' with the path to your image file
image = image.resize((200, 200))  # Resize the image to fit the window
photo = ImageTk.PhotoImage(image)

    # Add the image to the window
image_label = tk.Label(root, image=photo, bg="#ffe6e6")
image_label.pack(pady=10)
for i in range(1,10):
    print("Nasir")
# Add a greeting text
greeting_label = tk.Label(
    root, 
    text="Happy Birthday to the most special person!",
    font=("Arial", 16, "bold"), 
    fg="#ff6699",   # Text color
    bg="#ffe6e6"    # Background color matching the window
)
greeting_label.pack(pady=20)

# Create a button to close the window
close_button = tk.Button(
    root, 
    text="Close", 
    command=root.destroy, 
    font=("Arial", 12), 
    fg="white", 
    bg="#ff6699", 
    activebackground="#ff99cc"
)
close_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()