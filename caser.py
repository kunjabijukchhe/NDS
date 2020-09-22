from tkinter import *

from string import printable as letters

# GUI
root = Tk()
root.title("Caser Cipher Encryption")
root.geometry('400x380')
root.resizable(width=False, height=False)
color = '#20c997'
root.configure(bg=color)


def get_value_encrypt():
    msg = enter.get("1.0", 'end-1c')
    output.insert("1.0", encrypt(msg, int(enter_key.get('1.0', 'end-1c'))))


def get_value_decrypt():
    msg = output.get("1.0", 'end-1c')
    output1.insert("1.0", decrypt(msg, int(enter_key.get('1.0', 'end-1c'))))


def get_clear():
    enter.delete("1.0", END)
    enter_key.delete("1.0", END)
    output.delete("1.0", END)
    output1.delete("1.0", END)


label_heading = Label(root, text="Caser Cipher Encryption", bg='#17a2b8', fg='white', font=('Helvetica', 15, 'bold'))
label_heading.place(x=90, y=8)

label_entry = Label(root, text="Plain Text:", bg=color, font='Helvetica')
label_entry.place(x=40, y=55)

enter = Text(root, height=2, width=20)
enter.place(x=160, y=55)

label_key = Label(root, text="Key:", bg=color, font='Helvetica')
label_key.place(x=40, y=115)

enter_key = Text(root, height=2, width=5)
enter_key.place(x=160, y=110)

label_output = Label(root, text="Encrypted Text:", bg=color, font='Helvetica')
label_output.place(x=40, y=175)

output = Text(root, height=2, width=20)
output.place(x=160, y=170)

label_output1 = Label(root, text="Decrypted Text:", bg=color, font='Helvetica')
label_output1.place(x=40, y=235)

output1 = Text(root, height=2, width=20)
output1.place(x=160, y=230)

button = Button(root, text="Encrypt", bg='#343a40',fg='#f9f9f9', command=lambda: get_value_encrypt(), width=10, height=2,
                font=('Arial',12,'bold'))
button.place(x=30, y=300)

button1 = Button(root, text="Decrypt", bg='#343a40',fg='#f9f9f9', command=lambda: get_value_decrypt(), width=10, height=2,
                 font=('Arial',12,'bold'))
button1.place(x=150, y=300)

button_clear = Button(root, text="Clear", bg='#343a40',fg='#f9f9f9', command=lambda: get_clear(), width=10, height=2, font=('Arial',12,'bold'))
button_clear.place(x=270, y=300)


def encrypt(message, key):
    cipher = []
    for c in message:
        position = letters.find(c)
        new_position = position + key % len(letters)
        encrypted_char = letters[new_position]
        cipher.append(encrypted_char)

    return ''.join(cipher)


def decrypt(cipher, key):
    plain_text = []
    for c in cipher:
        position = letters.find(c)
        position = (position - key) % len(letters)
        plain_text.append(letters[position])
    return ''.join(plain_text)


print(type(enter_key))
root.mainloop()
