from pytube import YouTube
from tkinter import Tk, Label, Entry, Button, Listbox, StringVar, filedialog

def download_video():
    url = url_entry.get()
    all_streams = YouTube(url).streams.all()

    listbox.delete(0, "end")  # Clear the listbox before updating with new streams

    for i, stream in enumerate(all_streams):
        listbox.insert("end", f"{i}; {stream}")

def choose_download_location():
    folder_name = filedialog.askdirectory()
    folder_var.set(folder_name)

def download_selected_video():
    stm_input = listbox.curselection()[0]
    folder_name = folder_var.get()
    all_streams[stm_input].download(folder_name)
    status_label.config(text="Video Download Complete.")

# GUI setup
root = Tk()
root.title("YouTube Video Downloader")

# URL Entry
Label(root, text="Enter Video URL:").pack()
url_entry = Entry(root, width=40)
url_entry.pack()

# Download Button
Button(root, text="Show Available Streams", command=download_video).pack()

# Available Streams Listbox
listbox = Listbox(root, selectmode="SINGLE", width=50, height=10)
listbox.pack()

# Choose Download Location Button
Button(root, text="Choose Download Location", command=choose_download_location).pack()

# Display chosen download location
folder_var = StringVar()
Label(root, textvariable=folder_var).pack()

# Download Selected Video Button
Button(root, text="Download Selected Video", command=download_selected_video).pack()

# Status Label
status_label = Label(root, text="")
status_label.pack()

# Start the GUI
root.mainloop()
