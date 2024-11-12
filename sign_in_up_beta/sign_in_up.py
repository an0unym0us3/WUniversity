from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from sqlite3 import connect
from account_handler import db_sign_in, db_sign_up, DB_Error

db = connect('user_acc.db')
c = db.cursor()
db.execute('''
create table if not exists users(
id int primary key,
name varchar(30) not null,
token blob not null,
key blob not null,
dob date,
email varchar(30)
);
''')
db.commit()

app = CTk()
app.title('Login Page')
app.geometry("600x480")
app.resizable(False, False)


def show_sign_in():
    app.title('Login Page')
    side_img.configure(dark_image=signin_img_data, light_image=signin_img_data)
    sign_up_frame.pack_forget()
    sign_in_frame.pack(expand=True, side="right")


def on_sign_in():
    username = signin_username_entry.get()
    password = signin_password_entry.get()

    try:
        db_sign_in(username, password)
    except DB_Error as e:
        messagebox.showerror("Sign In", e.info)
    else:
        messagebox.showinfo("Sign In", "Sign In Successful")
        signin_username_entry.delete(0, ctk.END)
        signin_password_entry.delete(0, ctk.END)
        # Transition to the next part of the application


def create_sign_in_frame(master):
    frame = CTkFrame(master=master, width=300, height=480, fg_color="#ffffff")
    frame.pack_propagate(False)

    # Title
    CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
    CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left",
             font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

    # Username cluster
    CTkLabel(master=frame, text="  Username:", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 14), image=user_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
    global signin_username_entry
    signin_username_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88",
                                     border_width=1, text_color="#000000")
    signin_username_entry.pack(anchor="w", padx=(25, 0))

    # Password cluster
    CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    global signin_password_entry
    signin_password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88",
                                     border_width=1, text_color="#000000", show="*")
    signin_password_entry.pack(anchor="w", padx=(25, 0))

    # Button cluster
    CTkButton(master=frame, text="Sign in", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=on_sign_in).pack(anchor="w", pady=(40, 0), padx=(25, 0))
    CTkButton(master=frame, text="Need to sign up?", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Arial Bold", 9),
              text_color="#601E88", width=225, image=user_add_icon, command=show_sign_up).pack(anchor="w", pady=(20, 0),
                                                                                               padx=(25, 0))

    return frame


def show_sign_up():
    app.title('Registration Page')
    side_img.configure(dark_image=signup_img_data, light_image=signup_img_data)
    sign_in_frame.pack_forget()
    sign_up_frame.pack(expand=True, side="right")


def on_sign_up():
    username = signup_username_entry.get()
    password = signup_password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Validate sign up details
    if password != confirm_password:
        messagebox.showerror("Sign Up", "Passwords do not match")
    else:
        try:
            db_sign_up(username, password)
        except DB_Error as e:
            messagebox.showerror("Sign Up", e.info)
        else:
            messagebox.showinfo("Sign Up", "Sign Up Successful")
            # Clear the entry fields
            signup_username_entry.delete(0, ctk.END)
            signup_password_entry.delete(0, ctk.END)
            confirm_password_entry.delete(0, ctk.END)
            # Switch to sign in page
            show_sign_in()


def create_sign_up_frame(master):
    frame = CTkFrame(master=master, width=300, height=480, fg_color="#ffffff")
    frame.pack_propagate(False)
    frame.pack_forget()  # Hide the sign-up frame initially

    # Title
    CTkLabel(master=frame, text="Welcome!", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
    CTkLabel(master=frame, text="Create an Account", text_color="#7E7E7E", anchor="w", justify="left",
             font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

    # Username cluster
    CTkLabel(master=frame, text="  Username:", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 14), image=user_add_icon, compound="left").pack(anchor="w", pady=(19, 0), padx=(25, 0))
    global signup_username_entry
    signup_username_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88",
                                     border_width=1, text_color="#000000")
    signup_username_entry.pack(anchor="w", padx=(25, 0))

    # Password cluster
    CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    global signup_password_entry
    signup_password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88",
                                     border_width=1, text_color="#000000", show="*")
    signup_password_entry.pack(anchor="w", padx=(25, 0))

    # Confirm password cluster
    CTkLabel(master=frame, text="  Confirm password:", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    global confirm_password_entry
    confirm_password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88",
                                      border_width=1, text_color="#000000", show="*")
    confirm_password_entry.pack(anchor="w", padx=(25, 0))

    # Button cluster
    CTkButton(master=frame, text="Sign Up", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=on_sign_up).pack(anchor="w", pady=(40, 0), padx=(25, 0))
    CTkButton(master=frame, text="Back to Sign In", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Arial Bold", 9),
              text_color="#601E88", width=225, image=user_icon, command=show_sign_in).pack(anchor="w", pady=(20, 0),
                                                                                           padx=(25, 0))

    return frame


signin_img_data = Image.open("signin-side-img.png")
signup_img_data = Image.open("signup-side-img.png")
user_icon_data = Image.open("user-icon.png")
user_add_icon_data = Image.open("user-add-icon.png")
password_icon_data = Image.open("password-icon.png")
confirm_password_icon_data = None

side_img = CTkImage(dark_image=signin_img_data, light_image=signin_img_data, size=(300, 480))
user_icon = CTkImage(dark_image=user_icon_data, light_image=user_icon_data, size=(20, 20))
user_add_icon = CTkImage(dark_image=user_add_icon_data, light_image=user_add_icon_data, size=(17, 17))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

sign_up_frame = create_sign_up_frame(app)
sign_in_frame = create_sign_in_frame(app)

sign_in_frame.pack(expand=True, side="right")

app.mainloop()
