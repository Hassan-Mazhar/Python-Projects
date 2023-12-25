from tkinter import *
import speedtest

def speedcheck():
    # Create a Speedtest object
    sp = speedtest.Speedtest()

    # Get best servers based on ping
    sp.get_best_server()

    # Perform the speed test for download and upload
    download_speed = sp.download()
    upload_speed = sp.upload()

    # Convert the speeds to Mbps and update the labels
    down_mbps = round(download_speed / (10**6), 3)
    up_mbps = round(upload_speed / (10**6), 3)

    lab_down.config(text=f"{down_mbps} Mbps")
    lab_up.config(text=f"{up_mbps} Mbps")

# Set up the main window
root = Tk()
root.title("Internet Speed Test")
root.geometry("500x500")
root.config(bg="Blue")

# Create labels and buttons
Label(root, text="Internet Speed Test", font=("Times New Roman", 20, "bold"), bg="blue", fg="white").place(x=50, y=40, height=50, width=380)
Label(root, text="Downloading Speed", font=("Times New Roman", 20, "bold"), bg="blue", fg="white").place(x=50, y=130, height=50, width=380)

lab_down = Label(root, text="00", font=("Times New Roman", 20, "bold"), bg="blue", fg="white")
lab_down.place(x=50, y=200, height=50, width=380)

Label(root, text="Upload Speed", font=("Times New Roman", 20, "bold"), bg="blue", fg="white").place(x=50, y=290, height=50, width=380)

lab_up = Label(root, text="00", font=("Times New Roman", 20, "bold"), bg="blue", fg="white")
lab_up.place(x=50, y=360, height=50, width=380)

Button(root, text="CHECK SPEED", font=("Times New Roman", 20, "bold"), relief=RAISED, bg="red", command=speedcheck).place(x=60, y=460, height=50, width=380)

# Run the main loop
root.mainloop()
