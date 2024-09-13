import tkinter as tk
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha(): 
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def encrypt_text():
    text = entry_text.get()  
    shift = int(entry_shift.get()) 
    encrypted_message = encrypt(text, shift)
    label_result.config(text=f"cipher text = {encrypted_message}")


def decrypt_text():
    text = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_message = decrypt(text, shift)
    label_result.config(text=f"plain text = {decrypted_message}")


window = tk.Tk()
window.title("encryption tool")
window.config(bg="#FFFFFF")
window.geometry("700x700")



label_text = tk.Label(window, text="enter plain text" , width=50 , bg="white", fg="blue")
label_text.pack(pady=5)
entry_text = tk.Entry(window, width=50 , bg="yellow", fg="black")
entry_text.pack(pady=5)



label_shift = tk.Label(window, text="shift value :" , width=50 , bg="white", fg="blue")
label_shift.pack(pady=5)
entry_shift = tk.Entry(window, width=5 , bg="yellow", fg="black" ,  font=("Lucida Console", 9) )
entry_shift.pack(pady=5)


button_encrypt = tk.Button(window, text="encrypt", command=encrypt_text , bg="blue", fg="black" ,  font=("Lucida Console", 9))
button_encrypt.pack(pady=5)

button_decrypt = tk.Button(window, text="decrypt ", command=decrypt_text,  bg="blue", fg="black", font=("Lucida Console", 9))
button_decrypt.pack(pady=5)

label_result = tk.Label(window, text="")
label_result.pack(pady=10)

window.mainloop()
