from customtkinter import *
from tkinter import messagebox
from PIL import Image
from modules import access_handler as ah, transition_handler as th

# Application setup
app = CTk()
app.geometry("700x600")
app.resizable(False, False)

# Load and set background image
bg_image = CTkImage(Image.open("images/side-img.png"), size=(700, 600))
background_label = CTkLabel(master=app, image=bg_image, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Functions for Sign In and Sign Up
def show_sign_in():
    app.title('Login Page')
    sign_up_frame.pack_forget()
    sign_in_frame.pack(expand=True, side="right", anchor="e")

def on_sign_in():
    username = signin_username_entry.get()
    password = signin_password_entry.get()

    try:
        ah.db_sign_in(username, password)
    except ah.DB_Error as e:
        messagebox.showerror("Sign In", e.info)
    else:
        messagebox.showinfo("Sign In", "Sign In Successful")
        signin_username_entry.delete(0, END)  # Clear entry field
        signin_password_entry.delete(0, END)  # Clear entry field
        th.switch_to('Main.py')

def create_sign_in_frame(master):
    frame = CTkFrame(master=master, width=320, height=560, fg_color="#ffffff", corner_radius=10)  # Adjusted size for content
    frame.pack_propagate(False)

    # Title
    CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
    CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left",
             font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

    # Username cluster
    CTkLabel(master=frame, text="  Username:", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 14)).pack(anchor="w", pady=(38, 0), padx=(25, 0))
    global signin_username_entry
    signin_username_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88",
                                     border_width=1, text_color="#000000")
    signin_username_entry.pack(anchor="w", padx=(25, 0))

    # Password cluster
    CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 0))
    global signin_password_entry
    signin_password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88",
                                     border_width=1, text_color="#000000", show="*")
    signin_password_entry.pack(anchor="w", padx=(25, 0))

    # Button cluster
    CTkButton(master=frame, text="Sign in", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=on_sign_in).pack(anchor="w", pady=(40, 0), padx=(25, 0))
    CTkButton(master=frame, text="Need to sign up?", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Arial Bold", 9),
              text_color="#601E88", width=225, command=show_sign_up).pack(anchor="w", pady=(20, 0), padx=(25, 0))

    return frame

def show_sign_up():
    app.title('Registration Page')
    sign_in_frame.pack_forget()
    sign_up_frame.pack(expand=True, side="right", anchor="e")

def on_sign_up():
    username = signup_username_entry.get()
    password = signup_password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Validate sign up details
    if password != confirm_password:
        messagebox.showerror("Sign Up", "Passwords do not match")
    else:
        try:
            ah.db_sign_up(username, password)
        except ah.DB_Error as e:
            messagebox.showerror("Sign Up", e.info)
        else:
            messagebox.showinfo("Sign Up", "Sign Up Successful")
            # Clear the entry fields
            signup_username_entry.delete(0, END)
            signup_password_entry.delete(0, END)
            confirm_password_entry.delete(0, END)
            # Switch to sign in page
            show_sign_in()

def create_sign_up_frame(master):
    frame = CTkFrame(master=master, width=320, height=560, fg_color="#ffffff", corner_radius=10)  # Adjusted size for content
    frame.pack_propagate(False)
    frame.pack_forget()  # Hide the sign-up frame initially

    # Title
    CTkLabel(master=frame, text="Welcome!", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
    CTkLabel(master=frame, text="Create an Account", text_color="#7E7E7E", anchor="w", justify="left",
             font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

    # Username cluster
    CTkLabel(master=frame, text="  Username:", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 14)).pack(anchor="w", pady=(19, 0), padx=(25, 0))
    global signup_username_entry
    signup_username_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88",
                                     border_width=1, text_color="#000000")
    signup_username_entry.pack(anchor="w", padx=(25, 0))

    # Password cluster
    CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 0))
    global signup_password_entry
    signup_password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88",
                                     border_width=1, text_color="#000000", show="*")
    signup_password_entry.pack(anchor="w", padx=(25, 0))

    # Confirm password cluster
    CTkLabel(master=frame, text="  Confirm password:", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 0))
    global confirm_password_entry
    confirm_password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88",
                                      border_width=1, text_color="#000000", show="*")
    confirm_password_entry.pack(anchor="w", padx=(25, 0))

    # Button cluster
    CTkButton(master=frame, text="Sign Up", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=on_sign_up).pack(anchor="w", pady=(40, 0), padx=(25, 0))
    CTkButton(master=frame, text="Back to Sign In", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Arial Bold", 9),
              text_color="#601E88", width=225, command=show_sign_in).pack(anchor="w", pady=(20, 0), padx=(25, 0))

    return frame

# Create the sign-up and sign-in frames
sign_up_frame = create_sign_up_frame(app)
sign_in_frame = create_sign_in_frame(app)

# Start with the Sign-In frame
show_sign_in()

# Run the app
app.mainloop()
