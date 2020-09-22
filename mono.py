from tkinter import *
from random import shuffle
from string import printable

keys = list(printable)
shuffle_keys = list(printable)
shuffle(shuffle_keys)

maps = dict(zip(keys, shuffle_keys))
reverse_map = dict(zip(shuffle_keys, keys))
# print(maps)
# print(reverse_map)

# GUI
root = Tk()
root.title("Mono Alphabetic Cipher Encryption")
root.geometry('400x380')
root.resizable(width=False, height=False)
color = '#20c997'
root.configure(bg=color)


def get_value_encrypt():
    msg = enter.get("1.0", 'end-1c')
    output.insert("1.0", encrypt(msg))


def get_value_decrypt():
    msg = output.get("1.0", 'end-1c')
    output1.insert("1.0", decrypt(msg))


def get_clear():
    enter.delete("1.0", END)
    output.delete("1.0", END)
    output1.delete("1.0", END)


label_heading = Label(root, text="Mono Alphabetic Cipher Encryption", bg='#17a2b8', fg='white', font=('Helvetica', 15, 'bold'))
label_heading.place(x=35, y=10)

label_entry = Label(root, text="Plain Text:", bg=color, font='Helvetica')
label_entry.place(x=40, y=60)

enter = Text(root, height=2, width=20)
enter.place(x=160, y=55)

label_output = Label(root, text="Encrypted Text:", bg=color, font='Helvetica')
label_output.place(x=40, y=140)

output = Text(root, height=2, width=20)
output.place(x=160, y=135)

label_output1 = Label(root, text="Decrypted Text:", bg=color, font='Helvetica')
label_output1.place(x=40, y=220)

output1 = Text(root, height=2, width=20)
output1.place(x=160, y=215)

button = Button(root, text="Encrypt", bg='#343a40',fg='#f9f9f9', command=lambda: get_value_encrypt(), width=10, height=2,
                font=('Arial',12,'bold'))
button.place(x=30, y=300)

button1 = Button(root, text="Decrypt", bg='#343a40',fg='#f9f9f9', command=lambda: get_value_decrypt(), width=10, height=2,
                 font=('Arial',12,'bold'))
button1.place(x=150, y=300)

button_clear = Button(root, text="Clear", bg='#343a40',fg='#f9f9f9', command=lambda: get_clear(), width=10, height=2, font=('Arial',12,'bold'))
button_clear.place(x=270, y=300)


def encrypt(message):
    cipher = []
    for char in message:
        cipher_char = maps[char]
        cipher.append(cipher_char)
    return ''.join(cipher)


def decrypt(cipher):
    plain = []
    for cipher_char in cipher:
        plain_char = reverse_map[cipher_char]
        plain.append(plain_char)
    return ''.join(plain)


root.mainloop()
