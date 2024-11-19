import tkinter as tk
from tkinter import filedialog, messagebox


# Function to browse and select a file
def browse_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Image files", "*.jpg;*.jpeg;*.png")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)


# Function to show the next section of the form
def show_frame(frame):
    frame.tkraise()


# Function to check if all fields are filled
def validate_personal_info():
    if not first_name_entry.get() or not last_name_entry.get() or not dob_entry.get() or not email_entry.get() or not phone_entry.get():
        messagebox.showerror("Error", "All fields marked with * are required!")
        return False
    return True


def validate_documents():
    if not passport_entry.get() or not residence_front_entry.get() or not residence_back_entry.get() or not passport_photo_entry.get():
        messagebox.showerror("Error", "All fields marked with * are required!")
        return False
    return True


def validate_test_scores():
    if ielts_var.get() == "Select IELTS Score" and toefl_var.get() == "Select TOEFL Score":
        messagebox.showerror("Error", "Please select an IELTS or TOEFL score!")
        return False
    if sat_var.get() == "Select SAT Score" and act_var.get() == "Select ACT Score":
        messagebox.showerror("Error", "Please select a SAT or ACT score!")
        return False
    return True


def validate_upload_documents():
    if not transcript_entry.get() or not lor1_entry.get() or not lor2_entry.get() or not statement_entry.get():
        messagebox.showerror("Error", "All fields marked with * are required!")
        return False
    return True


# Function to submit the form
def submit_form():
    if validate_upload_documents():
        # Collect data from the form fields
        personal_info = {
            "first_name": first_name_entry.get(),
            "last_name": last_name_entry.get(),
            "dob": dob_entry.get(),
            "email": email_entry.get(),
            "phone": phone_entry.get(),
        }

        document_info = {
            "passport_copy": passport_entry.get(),
            "residence_card_front": residence_front_entry.get(),
            "residence_card_back": residence_back_entry.get(),
            "passport_photo": passport_photo_entry.get(),
        }

        test_scores = {
            "ielts": ielts_var.get(),
            "toefl": toefl_var.get(),
            "sat": sat_var.get(),
            "act": act_var.get(),
        }

        uploads = {
            "academic_transcript": transcript_entry.get(),
            "letter_of_recommendation_1": lor1_entry.get(),
            "letter_of_recommendation_2": lor2_entry.get(),
            "personal_statement": statement_entry.get(),
        }

        # Display a confirmation message
        messagebox.showinfo("Form Submitted", "Your application has been submitted successfully!")


# Initialize the window
root = tk.Tk()
root.title("University Application Form")
root.geometry("300x400")

# Create a container to hold frames (for different sections)
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Define the frames for different sections
frames = {}
for frame_name in ("personal_frame", "documents_frame", "test_scores_frame", "upload_documents_frame"):
    frame = tk.Frame(container)
    frame.grid(row=0, column=0, sticky="nsew")
    frames[frame_name] = frame


def init_personal_frame():
    # --- Personal Information Frame ---
    tk.Label(frames["personal_frame"], text="Personal Information", font=("Helvetica", 14)).pack(pady=10)
    tk.Label(frames["personal_frame"], text="First Name *:").pack(anchor="w")

    global first_name_entry
    first_name_entry = tk.Entry(frames["personal_frame"])
    first_name_entry.pack(fill="x", padx=10)

    global last_name_entry
    tk.Label(frames["personal_frame"], text="Last Name *:").pack(anchor="w")
    last_name_entry = tk.Entry(frames["personal_frame"])
    last_name_entry.pack(fill="x", padx=10)

    global dob_entry
    tk.Label(frames["personal_frame"], text="Date of Birth (YYYY-MM-DD) *:").pack(anchor="w")
    dob_entry = tk.Entry(frames["personal_frame"])
    dob_entry.pack(fill="x", padx=10)

    global email_entry
    tk.Label(frames["personal_frame"], text="Email *:").pack(anchor="w")
    email_entry = tk.Entry(frames["personal_frame"])
    email_entry.pack(fill="x", padx=10)

    global phone_entry
    tk.Label(frames["personal_frame"], text="Phone *:").pack(anchor="w")
    phone_entry = tk.Entry(frames["personal_frame"])
    phone_entry.pack(fill="x", padx=10)

    # Next button with validation
    tk.Button(frames["personal_frame"], text="Next",
              command=lambda: [show_frame(frames["documents_frame"]) if validate_personal_info() else None]).pack(
        side="right", padx=10, pady=20)


def init_documents_frame():
    # --- Passport and Photos Upload Frame ---
    tk.Label(frames["documents_frame"], text="Upload Passport and Photos", font=("Helvetica", 14)).pack(pady=10)

    global passport_entry
    # Passport upload
    tk.Label(frames["documents_frame"], text="Passport Copy *:").pack(anchor="w")
    passport_entry = tk.Entry(frames["documents_frame"])
    passport_entry.pack(fill="x", padx=10)
    tk.Button(frames["documents_frame"], text="Browse", command=lambda: browse_file(passport_entry)).pack(pady=5)

    global residence_front_entry
    # Residence card front upload
    tk.Label(frames["documents_frame"], text="Residence Card (Front) *:").pack(anchor="w")
    residence_front_entry = tk.Entry(frames["documents_frame"])
    residence_front_entry.pack(fill="x", padx=10)
    tk.Button(frames["documents_frame"], text="Browse", command=lambda: browse_file(residence_front_entry)).pack(pady=5)

    global residence_back_entry
    # Residence card back upload
    tk.Label(frames["documents_frame"], text="Residence Card (Back) *:").pack(anchor="w")
    residence_back_entry = tk.Entry(frames["documents_frame"])
    residence_back_entry.pack(fill="x", padx=10)
    tk.Button(frames["documents_frame"], text="Browse", command=lambda: browse_file(residence_back_entry)).pack(pady=5)

    global passport_photo_entry
    # Passport size photo upload
    tk.Label(frames["documents_frame"], text="Passport Size Photo *:").pack(anchor="w")
    passport_photo_entry = tk.Entry(frames["documents_frame"])
    passport_photo_entry.pack(fill="x", padx=10)
    tk.Button(frames["documents_frame"], text="Browse", command=lambda: browse_file(passport_photo_entry)).pack(pady=5)

    # Back and Next buttons with validation
    tk.Button(frames["documents_frame"], text="Back", command=lambda: show_frame(frames["personal_frame"])).pack(
        side="left", padx=10, pady=20)
    tk.Button(frames["documents_frame"], text="Next",
              command=lambda: [show_frame(frames["test_scores_frame"]) if validate_documents() else None]).pack(
        side="right", padx=10, pady=20)


def init_test_scores_frame():
    # --- Test Scores Frame ---
    tk.Label(frames["test_scores_frame"], text="English Proficiency", font=("Helvetica", 14)).pack(pady=10)

    global ielts_var
    # IELTS Dropdown (0.0 to 9.0, 0.5 interval)
    tk.Label(frames["test_scores_frame"], text="IELTS Score *:").pack(anchor="w")
    ielts_var = tk.StringVar(frames["test_scores_frame"])
    ielts_var.set("Select IELTS Score")
    ielts_scores = [str(i) for i in [round(i * 0.5, 1) for i in range(0, 19)]]
    ielts_dropdown = tk.OptionMenu(frames["test_scores_frame"], ielts_var, *ielts_scores)
    ielts_dropdown.pack(fill="x", padx=10)

    global toefl_var
    # TOEFL Dropdown (0 to 120, 1 interval)
    tk.Label(frames["test_scores_frame"], text="TOEFL Score *:").pack(anchor="w")
    toefl_var = tk.StringVar(frames["test_scores_frame"])
    toefl_var.set("Select TOEFL Score")
    toefl_scores = [str(i) for i in range(0, 121)]
    toefl_dropdown = tk.OptionMenu(frames["test_scores_frame"], toefl_var, *toefl_scores)
    toefl_dropdown.pack(fill="x", padx=10)

    # Standardized Exams Scores
    tk.Label(frames["test_scores_frame"], text="Standardized Exams", font=("Helvetica", 14)).pack(pady=10)

    global sat_var
    # SAT Dropdown (400 to 1600, 10 interval)
    tk.Label(frames["test_scores_frame"], text="SAT Score *:").pack(anchor="w")
    sat_var =    tk.StringVar(frames["test_scores_frame"])
    sat_var.set("Select SAT Score")
    sat_scores = [str(i) for i in range(400, 1601, 10)]
    sat_dropdown = tk.OptionMenu(frames["test_scores_frame"], sat_var, *sat_scores)
    sat_dropdown.pack(fill="x", padx=10)

    global act_var
    # ACT Dropdown (1 to 36)
    tk.Label(frames["test_scores_frame"], text="ACT Score *:").pack(anchor="w")
    act_var = tk.StringVar(frames["test_scores_frame"])
    act_var.set("Select ACT Score")
    act_scores = [str(i) for i in range(1, 37)]
    act_dropdown = tk.OptionMenu(frames["test_scores_frame"], act_var, *act_scores)
    act_dropdown.pack(fill="x", padx=10)

    # Back and Next buttons with validation
    tk.Button(frames["test_scores_frame"], text="Back", command=lambda: show_frame(frames["documents_frame"])).pack(side="left", padx=10, pady=20)
    tk.Button(frames["test_scores_frame"], text="Next", command=lambda: [show_frame(frames["upload_documents_frame"]) if validate_test_scores() else None]).pack(side="right", padx=10, pady=20)


def init_upload_documents_frame():
    # --- Upload Additional Documents Frame ---
    tk.Label(frames["upload_documents_frame"], text="Upload Academic Documents", font=("Helvetica", 14)).pack(pady=10)

    global transcript_entry
    # Academic Transcript upload
    tk.Label(frames["upload_documents_frame"], text="Academic Transcript *:").pack(anchor="w")
    transcript_entry = tk.Entry(frames["upload_documents_frame"])
    transcript_entry.pack(fill="x", padx=10)
    tk.Button(frames["upload_documents_frame"], text="Browse", command=lambda: browse_file(transcript_entry)).pack(pady=5)

    global lor1_entry
    # Letter of Recommendation 1 upload
    tk.Label(frames["upload_documents_frame"], text="Letter of Recommendation 1 *:").pack(anchor="w")
    lor1_entry = tk.Entry(frames["upload_documents_frame"])
    lor1_entry.pack(fill="x", padx=10)
    tk.Button(frames["upload_documents_frame"], text="Browse", command=lambda: browse_file(lor1_entry)).pack(pady=5)

    global lor2_entry
    # Letter of Recommendation 2 upload
    tk.Label(frames["upload_documents_frame"], text="Letter of Recommendation 2 *:").pack(anchor="w")
    lor2_entry = tk.Entry(frames["upload_documents_frame"])
    lor2_entry.pack(fill="x", padx=10)
    tk.Button(frames["upload_documents_frame"], text="Browse", command=lambda: browse_file(lor2_entry)).pack(pady=5)

    global statement_entry
    # Personal Statement upload
    tk.Label(frames["upload_documents_frame"], text="Personal Statement *:").pack(anchor="w")
    statement_entry = tk.Entry(frames["upload_documents_frame"])
    statement_entry.pack(fill="x", padx=10)
    tk.Button(frames["upload_documents_frame"], text="Browse", command=lambda: browse_file(statement_entry)).pack(pady=5)

    # Back and Submit buttons with validation
    tk.Button(frames["upload_documents_frame"], text="Back", command=lambda: show_frame(frames["test_scores_frame"])).pack(side="left", padx=10, pady=20)
    tk.Button(frames["upload_documents_frame"], text="Submit", command=submit_form).pack(side="right", padx=10, pady=20)


# Initialize frames and show the first frame
init_personal_frame()
init_documents_frame()
init_test_scores_frame()
init_upload_documents_frame()
show_frame(frames["personal_frame"])

root.mainloop()

