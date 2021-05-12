import smtplib
import tkinter as tk
from tkinter import BOTH, END, LEFT
root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="White")
frame.place(relwidth = 0.8, relheight =0.8, relx = 0.1, rely = 0.1)
whom = ""
body = ""
subject = ""
def emailSend():
    gmailaddress = "Enter your email here"
    gmailpassword = "Enter your password here"
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, whom.get(), body.get("1.0",END))
    print(" \n Sent!")
    mailServer.quit()

def emailCreate():
    global whom
    global subject
    global body
    rootM = tk.Tk()
    frameM = tk.Frame(rootM, width = 500, height = 400, bg="#263D42")
    frameM.pack(fill = None, expand = True)
    frameM.place(x=500,y=500)
    whom = tk.Entry(rootM)
    whom.pack()
    whom.insert(tk.END, "Recipients")
    subject = tk.Entry(rootM)
    subject.pack()
    subject.insert(tk.END, "Subject")
    body = tk.Text(rootM, height = 20, width = 30)
    body.pack()
    body.insert(tk.END, "Body \n \n \n \n \n \n \n")
    send = tk.Button(rootM, text="Send", padx = 10, pady = 5, fg="White", bg="#263D42", command = emailSend)
    send.pack()
    rootM.mainloop()

newEmail = tk.Button(root, text="New Email", padx = 10, pady=5, fg="White", bg="#263D42", command = emailCreate)
newEmail.pack()

root.mainloop()


