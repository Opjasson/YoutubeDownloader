import tkinter
import customtkinter
from pytube import YouTube


def startdownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback = on_progress)
        video = ytObject.streams.get_highest_resolution()
        
        title.configure(text=ytObject.title, text_color="black")
        finishText.configure(text="Download Complete", text_color="green")
        video.download()
        finishText.configure(text="Download Completed")
    except:
        finishText.configure(text="wrong link")
        finishText.configure(text_color="red")
        
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text= per + "%")
    pPercentage.update()
    # update progress bar
    progressBar.set(float(percentage_of_completion / 100))

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Element
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()


# Progres percentages
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# finished Downloading
finishText = customtkinter.CTkLabel(app, text="")
finishText.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command= startdownload)
download.pack(padx=10, pady=10)


# Run app
app.mainloop()



