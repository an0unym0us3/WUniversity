import customtkinter as ctk
from PIL import Image, ImageTk 
import pywinstyles
import subprocess

def UniversityPage():
    global root 
    root = ctk.CTk()
    root.geometry('1400x700')
    ctk.set_appearance_mode('light')
    root.resizable(False, False)

    bg_image = ctk.CTkImage(Image.open("background.jpg"), size=(1400, 700))
    background_label = ctk.CTkLabel(master=root, image=bg_image, text="")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    root.title('University Information Hub')

    welcome = ctk.CTkLabel(root, text='Select your Dream University', text_color="#ffffff", bg_color="#000001", font=("Arial Bold", 20, "bold")) 
    welcome.grid(row=0, column=0, columnspan=5, padx=0, pady=(10,20), sticky="n") 
    pywinstyles.set_opacity(welcome, color="#000001")


    universities = [
    'aizu', 'hiroshima', 'hokkaido', 'keio', 'kobe', 'kuas', 'kyoto', 'kyushu', 'nagoya', 
    'osaka', 'ritsumeikan', 'shibaura', 'sophia', 'science', 'tiu', 'tohoku', 'tokyo', 'toyo', 'tsukuba', 'waseda'
    ]

    buttons = []
    paths = {}

    def click(college):
        print(paths[college])
        subprocess.run(['python', paths[college]])

    for college in universities:
        image_path = f"Logo/{college}.png"
        image = Image.open(image_path)
        image = image.resize((200, 100), Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(image)

        paths[college] = f"{college}.py"

        button = ctk.CTkButton(root, text='', fg_color='#ffffff', hover_color='#ffffff', 
                               text_color="#ffffff", corner_radius=0, border_color='#000000', border_width=5, image=image_tk,
                               command=lambda college=college: click(college))
        
        button.image = image_tk 
        buttons.append(button)

    for i in range(5):
       root.grid_columnconfigure(i, weight=1)

    counter = 0
    for i in range(1, 5):
        for j in range(5):
            if counter < len(buttons):
                buttons[counter].grid(row=i, column=j, padx=20, pady=20, sticky="nsew")
                counter += 1

    root.mainloop()

UniversityPage()
