import tkinter as tk
def encrypt():
    plain_text=entry1.get()
    key=int(entry2.get())
    cipher_text=""
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            position =ord(plain_text[i]) + key
            cipher_text += chr(position)
        else:
            cipher_text +=plain_text[i]
    label3.config(text="CipherText:" + cipher_text)
def decrypt():
    cipher_text=entry1.get()
    key=int(entry2.get())
    plain_text=""
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            new_position = ord(cipher_text[i]) - key
            plain_text += chr(new_position)
        else:
            plain_text += cipher_text[i]
    label3.config(text="PlainText:" + plain_text)

root = tk.Tk()
root.geometry("400x300")

label1=tk.Label(root,text="Enter Text")
label1.pack()
entry1=tk.Entry(root)
entry1.pack()

label2 = tk.Label(root,text="Enter Key")
label2.pack()
entry2=tk.Entry(root)
entry2.pack()

button1 = tk.Button(root,text="Encrypt", command=encrypt)
button1.pack(pady=20)

button2=tk.Button(root,text="Decrypt", command=decrypt)
button2.pack(pady=20)

label3= tk.Label(root,text="")
label3.pack()

root.mainloop()
