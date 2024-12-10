# University Application Hub
A platform that provides comprehensive information on universities, relevant courses, and admission procedures for English-medium engineering undergraduate programs in Japan.

Db viewer
https://inloop.github.io/sqlite-viewer/

welcome = ctk.CTkLabel(root, text='Select your Dream University', text_color="#ffffff", bg_color="#000001", font=("Arial Bold", 20, "bold"))
    welcome.grid(row=0, column=0, columnspan=5, padx=0, pady=(10,20), sticky="n")
    pywinstyles.set_opacity(welcome, color="#000001")


ws = aizu.winfo_screenwidth() 
hs = aizu.winfo_screenheight()
w = 1000
h = 750
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
aizu.geometry('%dx%d+%d+%d' % (w, h, x, y))

 root.geometry(f'1400x700+{(root.winfo_screenwidth() / 2)}x{(root.winfo_screenheight()/ 2) - (700 / 2)}')
