
import customtkinter
import random
import string
    

def generate_password():
    password_length_str = length_entry.get()
    if not password_length_str.isdigit():
        result_label.configure(text="Please enter a valid password length (a positive integer).")
        return

    password_length = int(password_length_str)
    password_length = int(length_entry.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    
    lowercase_chars = string.ascii_lowercase if include_lowercase else ''
    uppercase_chars = string.ascii_uppercase if include_uppercase else ''
    digit_chars = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    if not all_chars:
        result_label.configure(text="Please select at least one character type.")
    else:
        password = ''.join(random.choice(all_chars) for _ in range(password_length))
        result_label.configure(text=f"Generated Password: {password}")


app = customtkinter.CTk()
app.title("Password generator")
app.geometry("400x350") 

length_label = customtkinter.CTkLabel(app, text="Password Length:")
length_entry =customtkinter.CTkEntry(app)

lowercase_var =customtkinter.StringVar()

lowercase_check = customtkinter.CTkCheckBox(app, text="Include Lowercase Letters", variable=lowercase_var, fg_color="#C850C0", 
                                            checkbox_height=30, checkbox_width=30, corner_radius=36)
uppercase_var = customtkinter.StringVar()

uppercase_check = customtkinter.CTkCheckBox(app, text="Include Uppercase Letters", variable=uppercase_var, fg_color="#C850C0", 
                                            checkbox_height=30, checkbox_width=30, corner_radius=36)
digits_var = customtkinter.StringVar()

digits_check = customtkinter.CTkCheckBox(app, text="Include Random Digits", variable=digits_var, fg_color="#C850C0", 
                                            checkbox_height=30, checkbox_width=30, corner_radius=36)
special_chars_var = customtkinter.StringVar()

special_chars_check = customtkinter.CTkCheckBox(app, text="Include Special Characters", variable=special_chars_var, fg_color="#C850C0", 
                                            checkbox_height=30, checkbox_width=30, corner_radius=36)
generate_button = customtkinter.CTkButton(app, text="Generate Password", command=generate_password)

result_label = customtkinter.CTkLabel(app, text="", font=("Arial", 16), wraplength=300, text_color="#C850C0")


length_label.pack(pady=10)
length_entry.pack(pady=5)
lowercase_check.pack()
uppercase_check.pack()
digits_check.pack()
special_chars_check.pack()
generate_button.pack(pady=10)
result_label.pack()


app.mainloop()