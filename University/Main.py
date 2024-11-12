import customtkinter as ctk
from PIL import Image, ImageTk 
import sqlite3


conn = sqlite3.connect("University.db")
cursor = conn.cursor()
create_table_query = '''
CREATE TABLE IF NOT EXISTS University (
    Rank INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Course TEXT NOT NULL,
    Location TEXT NOT NULL,
    School_Type TEXT NOT NULL,
    No_of_Seats INTEGER NOT NULL,
    Fees INTEGER NOT NULL,
    Selection_Method TEXT NOT NULL,
    Application_Period TEXT NOT NULL, 
    Document_Screening_Results_Announcement_Date TEXT NOT NULL,
    Interview_Screening_Date TEXT NOT NULL,
    Final_Results_Announcement_Date TEXT NOT NULL,
    Enrollment_Date TEXT NOT NULL,
    No_of_Essays_Required_Word_Count INTEGER NOT NULL,
    SAT_Scores_Minimum_Requirement INTEGER,
    TOEFL_IELTS_Scores_Minimum_Requirement INTEGER
    );
'''
cursor.execute(create_table_query)
conn.commit()
conn.close()

pageOpen = False

def UniversityPage():
    global root 
    root = ctk.CTk()
    root.geometry('1300x700')
    ctk.set_appearance_mode('light')


    root.title('University Application Platform')

    welcome = ctk.CTkLabel(root, text='Select your Dream University', font=("Helvetica", 20, "bold"))
    welcome.grid(row=0, column=3, padx=10, pady=15)

    universities = [
    'aizu', 'hiroshima', 'hokkaido', 'keio', 'kobe', 'kuas', 'kyoto', 'kyushu', 'nagoya', 
    'osaka', 'ritsumeikan', 'shibaura', 'sophia', 'tit', 'tiu', 'tohoku', 'tokyo', 'toyo', 'tsukuba', 'waseda'
    ]

    buttons = []
    paths = {}

    def click(college):
        print(paths[college])
        with open(paths[college]) as file:
            exec(file.read())

    for college in universities:
        image_path = f"Logo/{college}.png"
        image = Image.open(image_path)
        image = image.resize((180, 100), Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(image)

        paths[college] = f"University/{college}.py"

        button = ctk.CTkButton(root, text='', cursor='hand2', fg_color='#FFFFFF', hover_color='#000000', 
                               corner_radius=100, border_color='#000000', border_width=3, image=image_tk,
                               command=lambda college=college: click(college))
        
        button.image = image_tk 
        buttons.append(button)
    
    counter = 0
    for i in range(5):
        for j in range(5):
            if counter < len(buttons):
                buttons[counter].grid(row=i + 1, column=j, padx=10, pady=10)
                print(buttons[counter])
                print(counter)
                counter += 1
            else:
                break

    root.mainloop()

UniversityPage()
