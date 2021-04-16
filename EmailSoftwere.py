#La prima parte, "1.0", significa che l'input deve essere letto dalla riga uno, carattere zero (cioè: il primo carattere). END è una costante importata impostata sulla stringa "end". La parte END significa leggere fino a raggiungere la fine della casella di testo. L'unico problema con questo è che in realtà aggiunge una nuova riga al nostro input. Quindi, per risolverlo dovremmo cambiare END in end-1c (Grazie Bryan Oakley) Il -1c cancella 1 carattere, mentre -2c significherebbe cancellare due caratteri, e così via.
import tkinter as tk

#Variables
FromPositionR = 0
PasswordPositionR = 1
ToPositionR = 2
ObjectPositionR = 3
MessagePositionR = 4

#Window
window = tk.Tk()
window.geometry("600x600")
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

#Object
ObjectLabel = tk.Label(window, text="Object:")
ObjectLabel.grid(row=ObjectPositionR, column=0)
ObjectLabel.configure(background="yellow")

ObjectInput = tk.Text(window, width=40, height=2, bg="orange", fg = "black", borderwidth=5)
ObjectInput.grid(row=ObjectPositionR, column=1)

#Message
MessageLabel = tk.Label(window, text="Message:")
MessageLabel.grid(row=MessagePositionR, column=0)
MessageLabel.configure(background="yellow")

MessageInput = tk.Text(window, width=40, height=20, bg="orange", fg = "black", borderwidth=5)
MessageInput.grid(row=MessagePositionR, column=1)

#Functions
def clickTest():
    inputValue=ToEmailInput.get("1.0","end-1c")
    print(inputValue)

#Buttons
TestButton = tk.Button(window, text="Test", padx=50, pady=50, command=clickTest)
TestButton.grid(row=9, column=0)

if __name__ == "__main__":
    window.mainloop()