import os
from tkinter import *
from PIL import Image, ImageTk  
#import pywinstyles


window = Tk()
window.title("University Application Hub")
window.geometry("900x600")  
window.resizable(False, False)


bg_image_path = "School Project/HomePage/m.jpg"  
if os.path.exists(bg_image_path):
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((900, 600), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    
    bg_label = Label(window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
else:
    print(f"Error: Background image '{bg_image_path}' not found!")
    Label(window, text="Background image not found!", font=("Arial", 20)).pack(pady=20)


heading_label = Label(
    window,
    text="University Application Hub",
    font=("Arial", 30, "bold"),
    background="#000001"  
)
heading_label.place(relx=0.5, y=50, anchor="center") 
#pywinstyles.set_opacity(heading_label, color="#000001") 


subheading_label = Label(
    window,
    text="You Dream. We Support. You Achieve.",
    font=("Arial", 18, "italic"),
    background="#000001"  
)
subheading_label.place(relx=0.5, y=120, anchor="center") 
#pywinstyles.set_opacity(subheading_label, color="#000001") 


def on_get_started():
    print("Get Started button clicked!")


button_canvas = Canvas(window, width=180, height=60, highlightthickness=0, background="#000001")
button_canvas.place(relx=0.5, y=300, anchor="center")
radius = 30  
button_canvas.create_arc(10, 10, 10 + 2 * radius, 50, start=90, extent=180, fill="red", outline="red") 
button_canvas.create_arc(170 - 2 * radius, 10, 170, 50, start=270, extent=180, fill="red", outline="red")  
button_canvas.create_rectangle(10 + radius, 10, 170 - radius, 50, fill="red", outline="red")
button_text = button_canvas.create_text(90, 30, text="Get Started", font=("Arial", 16, "bold"), fill="white")
button_canvas.tag_bind(button_text, "<Button-1>", lambda event: on_get_started())
#pywinstyles.set_opacity(button_canvas, color="#000001")

window.mainloop()
