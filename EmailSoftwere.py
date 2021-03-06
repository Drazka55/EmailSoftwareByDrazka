import tkinter as tk
import smtplib

#Variables
FromPositionR = 0
PasswordPositionR = 1
ToPositionR = 2
SubjectPositionR = 3
MessagePositionR = 4
SendButtonPositionR = 5
AddressBookPositionR = 6

ReadFile = open("AddressBook.txt", "r").read()

#Window
window = tk.Tk()
window.geometry("600x1000")
window.title("Email Sender")
window.resizable(False, False)
window.configure(background="yellow")

#From
FromLabel = tk.Label(window, text="From:")
FromLabel.grid(row=FromPositionR, column=0)
FromLabel.configure(background="yellow")

FromEmailInput = tk.Text(window, width=40, height=1, bg="orange", fg = "black", borderwidth=5)
FromEmailInput.grid(row=FromPositionR, column=1)

#Password
PasswordLabel = tk.Label(window, text="Password:")
PasswordLabel.grid(row=PasswordPositionR, column=0)
PasswordLabel.configure(background="yellow")

PasswordEmailInput = tk.Text(window, width=40, height=1, bg="orange", fg = "black", borderwidth=5)
PasswordEmailInput.grid(row=PasswordPositionR, column=1)

#To
ToLabel = tk.Label(window, text="To:")
ToLabel.grid(row=ToPositionR, column=0)
ToLabel.configure(background="yellow")

ToEmailInput = tk.Text(window, width=40, height=1, bg="orange", fg = "black", borderwidth=5)
ToEmailInput.grid(row=ToPositionR, column=1)

#Subject
SubjectLabel = tk.Label(window, text="Subject:")
SubjectLabel.grid(row=SubjectPositionR, column=0)
SubjectLabel.configure(background="yellow")

SubjectInput = tk.Text(window, width=40, height=2, bg="orange", fg = "black", borderwidth=5)
SubjectInput.grid(row=SubjectPositionR, column=1)

#Message
MessageLabel = tk.Label(window, text="Message:")
MessageLabel.grid(row=MessagePositionR, column=0)
MessageLabel.configure(background="yellow")

MessageInput = tk.Text(window, width=40, height=20, bg="orange", fg = "black", borderwidth=5)
MessageInput.grid(row=MessagePositionR, column=1)

#AddressBook
AddressBookLabel = tk.Label(window, text="Address Book:")
AddressBookLabel.grid(row=AddressBookPositionR , column=0)
AddressBookLabel.configure(background="yellow")

AddressBookInput = tk.Text(window, width=40, height=30, bg="orange", fg = "black", borderwidth=5)
AddressBookInput.grid(row=AddressBookPositionR, column=1)
AddressBookInput.insert(tk.END, ReadFile)

#Functions
def sendEmail():
    FromEmail = FromEmailInput.get("1.0","end-1c")
    Password = PasswordEmailInput.get("1.0","end-1c")
    ToEmail = ToEmailInput.get("1.0","end-1c")
    Subject = SubjectInput.get("1.0","end-1c") + "\n"
    Content = MessageInput.get("1.0","end-1c")
    Message = Subject + Content


    emailService = smtplib.SMTP("smtp.gmail.com", 587)

    emailService.ehlo()

    emailService.starttls()

    emailService.login(FromEmail, Password)

    emailService.sendmail(FromEmail, ToEmail, Message)

    emailService.quit()

def QuitProgram():
    AddressBookSave = AddressBookInput.get("1.0","end-1c")

    SaveFile = open("AddressBook.txt", "w")
    SaveFile.write(AddressBookSave)
    SaveFile.close()

    window.destroy()

#Buttons
SendButton = tk.Button(window, text="Send", padx=50, pady=10, command=sendEmail)
SendButton.grid(row=SendButtonPositionR, column=0)

QuitButton = tk.Button(window, text="Quit", padx=50, pady=10, command=QuitProgram)
QuitButton.grid(row=SendButtonPositionR, column=2)

if __name__ == "__main__":
    window.mainloop()