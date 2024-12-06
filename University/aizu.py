import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from PIL import Image
import subprocess
#import pywinstyles



aizu = ctk.CTk()
aizu.title('The University of Aizu')
aizu.geometry('1000x1000')
ctk.set_appearance_mode('light')

def open_window():

    main_frame = Frame(aizu)
    main_frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(main_frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    second_frame = Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=second_frame, anchor="nw")



    bg_image = ctk.CTkImage(Image.open("Campus/aizu_campus.jpg"), size=(1000, 250))
    background_label = ctk.CTkLabel(master=second_frame, image=bg_image, text="")
    background_label.grid(row=0, column=0, columnspan=5, padx=0, pady=(1,2), sticky="w")



    title = ctk.CTkLabel(second_frame, text='University of Aizu', font=("Arial", 30, "bold"))
    title.grid(row=0, column=0, padx=10, pady=(10, 20), sticky="n")
    #pywinstyles.set_opacity(title, color="#000001")



    pin_image = ctk.CTkImage(Image.open("Symbols/pin.png"), size=(20, 20))
    pin_label = ctk.CTkLabel(master=second_frame, image=pin_image, text="")
    pin_label.grid(row=1, column=0, padx=30, pady=20, sticky='w')

    location = ctk.CTkLabel(second_frame, text='Aizuwakamatsu, Japan', font=("Arial", 20))
    location.grid(row=1, column=1,  padx=1, pady=10, sticky="n")



    type_image = ctk.CTkImage(Image.open("Symbols/type.png"), size=(20, 20))
    type_label = ctk.CTkLabel(master=second_frame, image=type_image, text="")
    type_label.grid(row=2, column=0, padx=30, pady=20, sticky='w')

    type = ctk.CTkLabel(second_frame, text='Public', font=("Arial", 20))
    type.grid(row=2, column=1, padx=10, pady=10, sticky="n")



    ty_image = ctk.CTkImage(Image.open("Symbols/rank.png"), size=(20, 20))
    ty_label = ctk.CTkLabel(master=second_frame, image=ty_image, text="")
    ty_label.grid(row=3, column=0, padx=30, pady=20, sticky='w')

    rank = ctk.CTkLabel(second_frame, text='QS National University Rankings 2024', font=("Arial", 20))
    rank.grid(row=3, column=1, padx=10, pady=10, sticky="n")

    rank_no = ctk.CTkLabel(second_frame, text='#10', font=("Arial", 30, "bold"))
    rank_no.grid(row=3, column=2, padx=10, pady=10, sticky="n")



    dept_image = ctk.CTkImage(Image.open("Symbols/department.png"), size=(20, 20))
    dept_label = ctk.CTkLabel(master=second_frame, image=dept_image, text="")
    dept_label.grid(row=4, column=0, padx=30, pady=20, sticky='w')

    department = ctk.CTkLabel(second_frame, text='Department :', font=("Arial", 20, "bold"))
    department.grid(row=4, column=1, padx=10, pady=10, sticky="n")

    department_name = ctk.CTkLabel(second_frame, text='Engineering', font=("Arial", 20))
    department_name.grid(row=4, column=2, padx=10, pady=10, sticky="n")



    course_image = ctk.CTkImage(Image.open("Symbols/course.png"), size=(20, 20))
    course_label = ctk.CTkLabel(master=second_frame, image=course_image, text="")
    course_label.grid(row=5, column=0, padx=30, pady=20, sticky='w')

    course = ctk.CTkLabel(second_frame, text='Course :', font=("Arial", 20, "bold"))
    course.grid(row=5, column=1, padx=10, pady=10, sticky="n")

    course_name = ctk.CTkLabel(second_frame, text='GSEP', font=("Arial", 20))
    course_name.grid(row=5, column=2, padx=10, pady=10, sticky="n")



    fees_image = ctk.CTkImage(Image.open("Symbols/fees.png"), size=(20, 20))
    fees_label = ctk.CTkLabel(master=second_frame, image=fees_image, text="")
    fees_label.grid(row=6, column=0, padx=30, pady=20, sticky='w')

    fees = ctk.CTkLabel(second_frame, text='Fees :', font=("Arial", 20, "bold"))
    fees.grid(row=6, column=1, padx=10, pady=10, sticky="n")

    fees_name = ctk.CTkLabel(second_frame, text='1000000 yen', font=("Arial", 20))
    fees_name.grid(row=6, column=2, padx=10, pady=10, sticky="n")



    score_image = ctk.CTkImage(Image.open("Symbols/score.png"), size=(20, 20))
    score_label = ctk.CTkLabel(master=second_frame, image=score_image, text="")
    score_label.grid(row=7, column=0, padx=30, pady=20, sticky='w')

    min_score = ctk.CTkLabel(second_frame, text='Minimum Score Requirement', font=("Arial", 20, "bold"))
    min_score.grid(row=7, column=1, padx=10, pady=10, sticky="n")

    min_toefl = ctk.CTkLabel(second_frame, text='TOEFL :       100', font=("Arial", 20))
    min_toefl.grid(row=8, column=1, padx=10, pady=10, sticky="n")

    min_ielts = ctk.CTkLabel(second_frame, text='IELTS :       7', font=("Arial", 20))
    min_ielts.grid(row=9, column=1, padx=10, pady=10, sticky="n")

    min_sat = ctk.CTkLabel(second_frame, text='SAT :           1400', font=("Arial", 20))
    min_sat.grid(row=10, column=1, padx=10, pady=10, sticky="n")

    min_act = ctk.CTkLabel(second_frame, text='ACT :           30', font=("Arial", 20))
    min_act.grid(row=11, column=1, padx=10, pady=10, sticky="n")



    seats_image = ctk.CTkImage(Image.open("Symbols/seats.png"), size=(20, 20))
    seats_label = ctk.CTkLabel(master=second_frame, image=seats_image, text="")
    seats_label.grid(row=12, column=0, padx=30, pady=20, sticky='w')

    seats = ctk.CTkLabel(second_frame, text='Number of Students Admitted  :', font=("Arial", 20, "bold"))
    seats.grid(row=12, column=1, padx=10, pady=10, sticky="n")

    seats_name = ctk.CTkLabel(second_frame, text='20', font=("Arial", 20))
    seats_name.grid(row=12, column=2, padx=10, pady=10, sticky="n")



    method_image = ctk.CTkImage(Image.open("Symbols/method.png"), size=(20, 20))
    method_label = ctk.CTkLabel(master=second_frame, image=method_image, text="")
    method_label.grid(row=13, column=0, padx=30, pady=20, sticky='w')

    selection_method = ctk.CTkLabel(second_frame, text='Document Screening & Interview', font=("Arial", 20))
    selection_method.grid(row=13, column=1, padx=10, pady=10, sticky="n")



    dates_image = ctk.CTkImage(Image.open("Symbols/date.png"), size=(20, 20))
    dates_label = ctk.CTkLabel(master=second_frame, image=dates_image, text="")
    dates_label.grid(row=14, column=0, padx=30, pady=20, sticky='w')

    dates = ctk.CTkLabel(second_frame, text='Important Dates :', font=("Arial", 20, "bold"))
    dates.grid(row=14, column=1, padx=10, pady=10, sticky="n")

    application_period = ctk.CTkLabel(second_frame, text='Application Period :', font=("Arial", 20, "bold"))
    application_period.grid(row=15, column=1, padx=10, pady=10, sticky="n")

    application_period_date = ctk.CTkLabel(second_frame, text='10th Jan 2024 - 10th Feb 2024', font=("Arial", 20))
    application_period_date.grid(row=15, column=2, padx=10, pady=10, sticky="n")

    first_screening = ctk.CTkLabel(second_frame, text='First Screening Result : :', font=("Arial", 20, "bold"))
    first_screening.grid(row=16, column=1, padx=10, pady=10, sticky="n")

    first_screening_date = ctk.CTkLabel(second_frame, text='28th Feb 2024', font=("Arial", 20))
    first_screening_date.grid(row=16, column=2, padx=10, pady=10, sticky="n")

    interview = ctk.CTkLabel(second_frame, text='Interview Date :', font=("Arial", 20, "bold"))
    interview.grid(row=17, column=1, padx=10, pady=10, sticky="n")

    interview_date = ctk.CTkLabel(second_frame, text='10th March 2024', font=("Arial", 20))
    interview_date.grid(row=17, column=2, padx=10, pady=10, sticky="n")

    result = ctk.CTkLabel(second_frame, text='Final Result Date :', font=("Arial", 20, "bold"))
    result.grid(row=18, column=1, padx=10, pady=10, sticky="n")

    result_date = ctk.CTkLabel(second_frame, text='10th April 2024', font=("Arial", 20))
    result_date.grid(row=18, column=2, padx=10, pady=10, sticky="n")

    enrollment = ctk.CTkLabel(second_frame, text='Enrollment Date :', font=("Arial", 20, "bold"))
    enrollment.grid(row=19, column=1, padx=10, pady=10, sticky="n")

    enrollment_date = ctk.CTkLabel(second_frame, text='10th May 2024', font=("Arial", 20))
    enrollment_date.grid(row=19, column=2, padx=10, pady=10, sticky="n")



    essay_image = ctk.CTkImage(Image.open("Symbols/essay.png"), size=(20, 20))
    essay_label = ctk.CTkLabel(master=second_frame, image=essay_image, text="")
    essay_label.grid(row=20, column=0, padx=30, pady=20, sticky='w')

    essay = ctk.CTkLabel(second_frame, text='Essay (Word Count) :', font=("Arial", 20, "bold"))
    essay.grid(row=20, column=1, padx=10, pady=10, sticky="n")

    essay_no = ctk.CTkLabel(second_frame, text='3 Essays (300 words each)', font=("Arial", 20))
    essay_no.grid(row=20, column=2, padx=10, pady=10, sticky="n")



    application = ctk.CTkButton(second_frame, text='Apply', fg_color='#601E88', hover_color='#E44982', 
                    text_color="#ffffff", corner_radius=5, border_color='#ffffff', border_width=0, command= open_fillments_page)
    application.grid(row=21, column=1, padx=10, pady=10)



def open_fillments_page():   
    aizu.destroy()
    
    try:
        subprocess.run(['python', 'FillmentsPage.py'], check=True)
    except FileNotFoundError:
        print("Error: FillmentsPage.py not found!")
    except Exception as e:
        print(f"An error occurred while opening FillmentsPage.py: {e}")
        

open_window()
aizu.mainloop()