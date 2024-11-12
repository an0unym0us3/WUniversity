import customtkinter as ctk

class Template():
    def __init__(self, title="Template", geometry="600x900"):
        self.root = ctk.CTk()
        self.root.title(title)
        self.root.geometry(geometry)

    def widgets(self):
        labels = [
            "Rank", "Name", "Department", "Course", "Location",
            "School Type", "No. of Seats", "Fees", "Selection Method",
            "Application Period", "Document Screening Results Announcement Date",
            "Interview screening Date", "Final Results Announcement Date",
            "Enrollment Date", "No. of Essays Required (Word Count)",
            "SAT Scores Minimum Requirement", "TOEFL/IELTS Scores Minimum Requirement"
            ]

        for i, text in enumerate(labels):
            self.label = ctk.CTkLabel(self.root, text=text)
            self.label.grid(row=i, column=0, padx=9, pady=5)
            self.entry = ctk.CTkEntry(self.root)
            self.entry.grid(row=i, column=1, padx=9, pady=5)

        self.button = ctk.CTkButton(self.root, text="Submit", command=self.on_button_click)
        self.button.grid(row=i+1, column=1, padx=9, pady=5)

    def on_button_click(self):
        pass

    def run(self):
        self.widgets()
        self.root.mainloop()
