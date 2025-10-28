import customtkinter as ctk
import random

Alphabet1=['a','c','e','g','i','k','m','o','q','s','u','w','y']
Alphabet2=['b','d','f','h','j','l','n','p','r','t','v','x','z']
number=['1','3','5','7','9','0','2','4','6','8']
schar=['!','@','#','&','^','*','(',')','-','_','=','+',':','.','/','<','>','?','$','%']


def generate_password():
    n = int(input_entry.get())
    password=str.upper(random.choice(Alphabet1))
    for i in range (0,n-1):
        a=random.randint(3,645)
        if a>562:
            s=random.choice(number)
        elif a>432:
            s=random.choice(schar)
        elif a>319:
            s=random.choice(Alphabet2)
            r2=random.randint(543,987)
            if r2%2!=0:
                s=s.upper()
        elif a>298:
            s=random.choice(Alphabet2)
        elif a>97:
            s=random.choice(number)
        else:
            s=random.choice(Alphabet1)
            r2=random.randint(456,679)
            if r2%2==0:
                s=s.upper()
        password+=s
    password = list(password)
    for i in range(0,n):
        random.shuffle(password)
    password =''.join(password)
    output_label.configure(text=f"generated number:\n {password}")









    
screen=ctk.CTk()
screen.geometry("600x600")
heading_label=ctk.CTkLabel(screen,text="Strong Password Generator",font=("verdana",30),text_color="#AECCE4",anchor="center",height=40, width=120,fg_color="transparent")
heading_label.pack(padx=50,pady=50)
canvas=ctk.CTkCanvas(screen,height=600,width=500)
canvas.pack(padx=50,pady=80)
canvas.configure(background="#AECCE4")
input_label=ctk.CTkLabel(canvas,text="enter number of characters:",font=("verdana",14,"italic"),text_color="black",anchor="w")
input_label.pack(padx=25,pady=15)
input_entry=ctk.CTkOptionMenu(canvas,values=["4","5","6","7","8","9","10","11","12"], anchor="w")
input_entry.pack(padx=25,pady=15)
submit_button=ctk.CTkButton(canvas, text="Submit",width=120,height=30,command= lambda:generate_password())
submit_button.pack(padx=25,pady=15)
output_label=ctk.CTkLabel(canvas,text="Generated pasword:\n",font=("verdana",14,"italic"))
output_label.pack(padx=25,pady=15)
screen.mainloop()