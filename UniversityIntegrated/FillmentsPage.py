import customtkinter as ctk
from tkinter import filedialog
from modules import fillments_handler as fh

# Function to browse and select a file
def browse_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Image files", "*.jpg;*.jpeg;*.png")])
    entry.delete(0, ctk.END) 
    entry.insert(0, file_path)

# Function to show the next section of the form
def show_frame(frame):
    frame.tkraise()

# Function to submit the form
def submit_form():
    # Collect data from the form fields
    fh.db_personal(first_name_entry.get(),
                last_name_entry.get(),
                dob_entry.get(),
                email_entry.get(),
                phone_entry.get())

    fh.db_documents(passport_entry.get(),
                 residence_front_entry.get(),
                 residence_back_entry.get())

    test = [ielts_entry.get(),
            toefl_entry.get(),
            sat_entry.get(),
            act_entry.get()]
    print('datatypes of scores:',[type(each) for each in test])

    fh.db_scores(float(ielts_entry.get()),
                 int(toefl_entry.get()),
                 int(sat_entry.get()),
                 int(act_entry.get()))

    fh.db_uploads(transcript_entry.get(),
               lor1_entry.get(),
               lor2_entry.get(),
               statement_entry.get())

    # Display a confirmation message
    #messagebox.showinfo("Form Submitted", "Your application has been submitted successfully!")
    show_frame(frames["thank_you_frame"])  # Navigate to the Thank You page

# Initialize the window
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "dark-blue", "green"

root = ctk.CTk()
root.title("University Application Form")
root.geometry("400x600")
root.configure(bg="white")  # Set window background to white

# Create a container to hold frames (for different sections)
container = ctk.CTkFrame(root, fg_color="white")
container.pack(fill="both", expand=True)

# Define the frames for different sections
frames = {}
for frame_name in ("personal_frame", "documents_frame", "test_scores_frame", "upload_documents_frame", "thank_you_frame"):
    frame = ctk.CTkFrame(container, corner_radius=15, fg_color="white")
    frame.grid(row=0, column=0, sticky="nsew")
    frames[frame_name] = frame

# Personal Information Section
def init_personal_frame():
    ctk.CTkLabel(frames["personal_frame"], text="Personal Information", font=("Helvetica", 24, "bold"), text_color="black").pack(pady=20)

    global first_name_entry
    ctk.CTkLabel(frames["personal_frame"], text="First Name:", text_color="black").pack(anchor="w", padx=20)
    first_name_entry = ctk.CTkEntry(frames["personal_frame"], placeholder_text="Enter your first name", fg_color="white", text_color="black", border_color="gray")
    first_name_entry.pack(fill="x", padx=20, pady=10)

    global last_name_entry
    ctk.CTkLabel(frames["personal_frame"], text="Last Name:", text_color="black").pack(anchor="w", padx=20)
    last_name_entry = ctk.CTkEntry(frames["personal_frame"], placeholder_text="Enter your last name", fg_color="white", text_color="black", border_color="gray")
    last_name_entry.pack(fill="x", padx=20, pady=10)

    global dob_entry
    ctk.CTkLabel(frames["personal_frame"], text="Date of Birth (YYYY-MM-DD):", text_color="black").pack(anchor="w", padx=20)
    dob_entry = ctk.CTkEntry(frames["personal_frame"], placeholder_text="Enter your date of birth", fg_color="white", text_color="black", border_color="gray")
    dob_entry.pack(fill="x", padx=20, pady=10)

    global email_entry
    ctk.CTkLabel(frames["personal_frame"], text="Email:", text_color="black").pack(anchor="w", padx=20)
    email_entry = ctk.CTkEntry(frames["personal_frame"], placeholder_text="Enter your email address", fg_color="white", text_color="black", border_color="gray")
    email_entry.pack(fill="x", padx=20, pady=10)

    global phone_entry
    ctk.CTkLabel(frames["personal_frame"], text="Phone:", text_color="black").pack(anchor="w", padx=20)
    phone_entry = ctk.CTkEntry(frames["personal_frame"], placeholder_text="Enter your phone number", fg_color="white", text_color="black", border_color="gray")
    phone_entry.pack(fill="x", padx=20, pady=10)

    ctk.CTkButton(frames["personal_frame"], text="Next", fg_color="black", text_color="white", hover_color="gray", command=lambda: show_frame(frames["documents_frame"])).pack(pady=20)

# Document Upload Section
def init_documents_frame():
    ctk.CTkLabel(frames["documents_frame"], text="Upload Documents", font=("Helvetica", 24, "bold"), text_color="black").pack(pady=20)

    global passport_entry
    ctk.CTkLabel(frames["documents_frame"], text="Passport Copy:", text_color="black").pack(anchor="w", padx=20)
    passport_entry = ctk.CTkEntry(frames["documents_frame"], placeholder_text="Upload your passport copy", fg_color="white", text_color="black", border_color="gray")
    passport_entry.pack(fill="x", padx=20, pady=10)
    ctk.CTkButton(frames["documents_frame"], text="Browse", fg_color="black", text_color="white", hover_color="gray", command=lambda: browse_file(passport_entry)).pack(pady=5)

    global residence_front_entry
    ctk.CTkLabel(frames["documents_frame"], text="Residence Card Front:", text_color="black").pack(anchor="w", padx=20)
    residence_front_entry = ctk.CTkEntry(frames["documents_frame"], placeholder_text="Upload residence card front", fg_color="white", text_color="black", border_color="gray")
    residence_front_entry.pack(fill="x", padx=20, pady=10)
    ctk.CTkButton(frames["documents_frame"], text="Browse", fg_color="black", text_color="white", hover_color="gray", command=lambda: browse_file(residence_front_entry)).pack(pady=5)

    global residence_back_entry
    ctk.CTkLabel(frames["documents_frame"], text="Residence Card Back:", text_color="black").pack(anchor="w", padx=20)
    residence_back_entry = ctk.CTkEntry(frames["documents_frame"], placeholder_text="Upload residence card back", fg_color="white", text_color="black", border_color="gray")
    residence_back_entry.pack(fill="x", padx=20, pady=10)
    ctk.CTkButton(frames["documents_frame"], text="Browse", fg_color="black", text_color="white", hover_color="gray", command=lambda: browse_file(residence_back_entry)).pack(pady=5)

    ctk.CTkButton(frames["documents_frame"], text="Back", fg_color="black", text_color="white", hover_color="gray", command=lambda: show_frame(frames["personal_frame"])).pack(side="left", padx=20, pady=20)
    ctk.CTkButton(frames["documents_frame"], text="Next", fg_color="black", text_color="white", hover_color="gray", command=lambda: show_frame(frames["test_scores_frame"])).pack(side="right", padx=20, pady=20)

# Test Scores Section
def init_test_scores_frame(): 
    ctk.CTkLabel(frames["test_scores_frame"], text="Test Scores", font=("Helvetica", 24, "bold"), text_color="black").pack(pady=20)

    global ielts_entry
    ctk.CTkLabel(frames["test_scores_frame"], text="IELTS Score:", text_color="black").pack(anchor="w", padx=20)
    ielts_entry = ctk.CTkEntry(frames["test_scores_frame"], placeholder_text="Enter your IELTS score (0-9)", fg_color="white", text_color="black", border_color="gray")
    ielts_entry.pack(fill="x", padx=20, pady=10)

    global toefl_entry
    ctk.CTkLabel(frames["test_scores_frame"], text="TOEFL Score:", text_color="black").pack(anchor="w", padx=20)
    toefl_entry = ctk.CTkEntry(frames["test_scores_frame"], placeholder_text="Enter your TOEFL score (0-120)", fg_color="white", text_color="black", border_color="gray")
    toefl_entry.pack(fill="x", padx=20, pady=10)

    global sat_entry
    ctk.CTkLabel(frames["test_scores_frame"], text="SAT Score:", text_color="black").pack(anchor="w", padx=20)
    sat_entry = ctk.CTkEntry(frames["test_scores_frame"], placeholder_text="Enter your SAT score (400-1600)", fg_color="white", text_color="black", border_color="gray")
    sat_entry.pack(fill="x", padx=20, pady=10)

    global act_entry
    ctk.CTkLabel(frames["test_scores_frame"], text="ACT Score:", text_color="black").pack(anchor="w", padx=20)
    act_entry = ctk.CTkEntry(frames["test_scores_frame"], placeholder_text="Enter your ACT score (1-36)", fg_color="white", text_color="black", border_color="gray")
    act_entry.pack(fill="x", padx=20, pady=10)

    ctk.CTkButton(frames["test_scores_frame"], text="Back", fg_color="black", text_color="white", hover_color="gray", command=lambda: show_frame(frames["documents_frame"])).pack(side="left", padx=20, pady=20)
    ctk.CTkButton(frames["test_scores_frame"], text="Next", fg_color="black", text_color="white", hover_color="gray", command=lambda: show_frame(frames["upload_documents_frame"])).pack(side="right", padx=20, pady=20)

# Academic Documents Upload Section
def init_upload_documents_frame():
    ctk.CTkLabel(frames["upload_documents_frame"], text="Upload Academic Documents", font=("Helvetica", 24, "bold"), text_color="black").pack(pady=20)

    global transcript_entry
    ctk.CTkLabel(frames["upload_documents_frame"], text="Academic Transcript:", text_color="black").pack(anchor="w", padx=20)
    transcript_entry = ctk.CTkEntry(frames["upload_documents_frame"], placeholder_text="Upload your transcript", fg_color="white", text_color="black", border_color="gray")
    transcript_entry.pack(fill="x", padx=20, pady=10)
    ctk.CTkButton(frames["upload_documents_frame"], text="Browse", fg_color="black", text_color="white", hover_color="gray", command=lambda: browse_file(transcript_entry)).pack(pady=5)

    global lor1_entry
    ctk.CTkLabel(frames["upload_documents_frame"], text="Letter of Recommendation 1:", text_color="black").pack(anchor="w", padx=20)
    lor1_entry = ctk.CTkEntry(frames["upload_documents_frame"], placeholder_text="Upload Recommendation Letter 1", fg_color="white", text_color="black", border_color="gray")
    lor1_entry.pack(fill="x", padx=20, pady=10)
    ctk.CTkButton(frames["upload_documents_frame"], text="Browse", fg_color="black", text_color="white", hover_color="gray", command=lambda: browse_file(lor1_entry)).pack(pady=5)

    global lor2_entry
    ctk.CTkLabel(frames["upload_documents_frame"], text="Letter of Recommendation 2:", text_color="black").pack(anchor="w", padx=20)
    lor2_entry = ctk.CTkEntry(frames["upload_documents_frame"], placeholder_text="Upload Recommendation Letter 2", fg_color="white", text_color="black", border_color="gray")
    lor2_entry.pack(fill="x", padx=20, pady=10)
    ctk.CTkButton(frames["upload_documents_frame"], text="Browse", fg_color="black", text_color="white", hover_color="gray", command=lambda: browse_file(lor2_entry)).pack(pady=5)

    global statement_entry
    ctk.CTkLabel(frames["upload_documents_frame"], text="Personal Statement:", text_color="black").pack(anchor="w", padx=20)
    statement_entry = ctk.CTkEntry(frames["upload_documents_frame"], placeholder_text="Upload Personal Statement", fg_color="white", text_color="black", border_color="gray")
    statement_entry.pack(fill="x", padx=20, pady=10)
    ctk.CTkButton(frames["upload_documents_frame"], text="Browse", fg_color="black", text_color="white", hover_color="gray", command=lambda: browse_file(statement_entry)).pack(pady=5)

    ctk.CTkButton(frames["upload_documents_frame"], text="Back", fg_color="black", text_color="white", hover_color="gray", command=lambda: show_frame(frames["test_scores_frame"])).pack(side="left", padx=20, pady=20)
    ctk.CTkButton(frames["upload_documents_frame"], text="Submit", fg_color="green", text_color="white", hover_color="darkgreen", command=submit_form).pack(side="right", padx=20, pady=20)

# Thank You Page
def init_thank_you_frame():
    ctk.CTkLabel(
        frames["thank_you_frame"],
        text="Thank You for Submitting Your Application!",
        font=("Helvetica", 17, "bold"),
        text_color="black",
    ).place(relx=0.5, rely=0.4, anchor="center")

    ctk.CTkLabel(
        frames["thank_you_frame"],
        text="You will receive the final results within 2 months.",
        font=("Helvetica", 16),
        text_color="black",
    ).place(relx=0.5, rely=0.5, anchor="center")

    ctk.CTkButton(
        frames["thank_you_frame"],
        text="Close",
        fg_color="red",
        text_color="white",
        hover_color="darkred",
        command=root.destroy,  # Close the application
    ).place(relx=0.5, rely=0.6, anchor="center")

# Initialize Frames
init_personal_frame()
init_documents_frame()
init_test_scores_frame()
init_upload_documents_frame()
init_thank_you_frame()
show_frame(frames["personal_frame"])

root.mainloop()
