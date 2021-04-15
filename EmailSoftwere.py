#La prima parte, "1.0", significa che l'input deve essere letto dalla riga uno, carattere zero (cioè: il primo carattere). END è una costante importata impostata sulla stringa "end". La parte END significa leggere fino a raggiungere la fine della casella di testo. L'unico problema con questo è che in realtà aggiunge una nuova riga al nostro input. Quindi, per risolverlo dovremmo cambiare END in end-1c (Grazie Bryan Oakley) Il -1c cancella 1 carattere, mentre -2c significherebbe cancellare due caratteri, e così via.

import tkinter as tk


window = tk.Tk()
window.geometry("600x600")
window.title("Email Sender")
window.resizable(False, False)
window.configure(background = "yellow")

ALabel = tk.Label(window, text="A:")
ALabel.grid(row = 0, column = 0)
ALabel.configure(background= "yellow")

AEmailInput = tk.Text(window, width= 40, height=1, bg="orange", fg = "black", borderwidth=5)
AEmailInput.grid(row = 0, column = 1)

def clickTest():
    inputValue=AEmailInput.get("1.0","end-1c")
    print(inputValue)


TestButton = tk.Button(window, text="Test", padx=50, pady=50, command=clickTest)
TestButton.grid(row=1, column=0)

if __name__ == "__main__":
    window.mainloop()