import customtkinter
import json
import random
import re
from tkinter import messagebox

def search_contact():
    search_input =search_entry.get().lower().strip()
    if len(search_input)==0:
        view()
        return
    try :
        with open ("contacts.json","r")as file:
            contact_lists=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showwarning("WARNING:", "Some Issue Occured!")
        contact_lists=[]
    search_list=[]
    for c in contact_lists:
        if search_input in c["name"].lower() or search_input in c["phone"] or search_input in c["email"].lower() or search_input in c["address"].lower():
            search_list.append(c)
    global r
    for widget in scroll_frame.winfo_children():
        widget.destroy()

    r = 0

    if len(search_list) == 0:
        messagebox.showinfo("NOT FOUND","No Matching contact Found")
        view()
        return

    for contact in search_list:
        cview = customtkinter.CTkFrame(scroll_frame, corner_radius=10)
        cview.grid(row=r, column=0, padx=20, pady=10, sticky="ew", columnspan=7)

        customtkinter.CTkLabel(cview, text=f"👤 {contact['name']}", font=("verdana",20)).grid(row=0,column=0,padx=30,sticky="w")
        customtkinter.CTkLabel(cview, text=f"📞 {contact['phone']}", font=("verdana",12)).grid(row=1,column=0,padx=30,sticky="w")
        customtkinter.CTkLabel(cview, text=f"✉️ {contact['email']}", font=("verdana",12)).grid(row=2,column=0,padx=30,sticky="w")
        customtkinter.CTkLabel(cview, text=f"🏠 {contact['address']}", font=("verdana",12)).grid(row=3,column=0,padx=30,sticky="w")

        # buttons
        customtkinter.CTkButton(cview, text="Edit", command=lambda j=contact["id"]: update_cont(j)).grid(row=1,column=5,pady=5)
        customtkinter.CTkButton(cview, text="Delete", command=lambda j=contact["id"]: delete_cont(j)).grid(row=2,column=5,pady=5)

        r += 4


def add_contact():
    def saving_data():
        global name_input,add_input,email_input, phone_input
        name_input=entry_name.get()
        phone_input=entry_phone.get()
        add_input=entry_address.get()
        email_input=entry_email.get()



        if name_input == "" or phone_input == "" or email_input == "" or add_input == "":
            messagebox.showwarning("Missing Data", "All fields must be filled!")
            return

    # Phone number validation (must be 10 digits & numeric)
        if not phone_input.isdigit() or len(phone_input) != 10:
            messagebox.showwarning("Invalid Phone", "Phone number must be 10 digits!")
            return

    # Email validation using regex
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email_input):
            messagebox.showwarning("Invalid Email", "Enter a valid email address!")
            return

        # data file reading
        try :
            with open ("contacts.json","r")as file:
                contact_lists=json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showwarning("WARNING:", "Some Issue Occured!")
            contact_lists=[]
        for c in contact_lists:
            if c["phone"]==phone_input or c["email"]==email_input:
                messagebox.showinfo("SORRY","Data Already Exsist")
                return
        # handling unique id
        id_list=[ item["id"] for item in contact_lists]
        id= random.randint(1,500)
        while id in id_list:
            id = random.randint(100,500)

        #generating new to-do dict
        cont ={"id":id,"name":name_input,"phone":phone_input,"email":email_input,"address":add_input}
        contact_lists.append(cont)


        #dump
        with open("contacts.json","w") as file:
            json.dump(contact_lists,file,indent=4)
        messagebox.showinfo("SUCCESS:", "New Contact Added Successfully")
        add_cont.destroy()

        view()

    #new dialouge box
    add_cont = customtkinter.CTkToplevel()
    add_cont.title("Add New Contact")
    add_cont.geometry("400x300")
    add_cont.grab_set()  # main window ke lock kore, ei popup ke active rakhe


    #new task, priority input
    label_new_name=customtkinter.CTkLabel(add_cont,text="enter name:",font=("verdana",14),height=35, width=120)
    label_new_name.grid(row=0, column=0,sticky="w",padx=20)
    entry_name=customtkinter.CTkEntry(add_cont,bg_color="black",width=200,placeholder_text="ex. raghav sampson ")
    entry_name.grid(row=0, column=1,sticky="w")
    label_new_phone=customtkinter.CTkLabel(add_cont,text="enter phone no:",font=("verdana",14),height=35,width=120)
    label_new_phone.grid(row=1, column=0,sticky="w",padx=20)
    entry_phone=customtkinter.CTkEntry(add_cont,bg_color="black",width=200,placeholder_text="ex. 9876543210 ")
    entry_phone.grid(row=1, column=1,sticky="w")
    label_new_email=customtkinter.CTkLabel(add_cont,text="enter email:",font=("verdana",14),height=35,width=120)
    label_new_email.grid(row=2, column=0,sticky="w",padx=20)
    entry_email=customtkinter.CTkEntry(add_cont,bg_color="black",width=200,placeholder_text="ex. abc@gmail.com")
    entry_email.grid(row=2, column=1,sticky="w")
    label_new_address=customtkinter.CTkLabel(add_cont,text="enter address:",font=("verdana",14),height=35,width=120)
    label_new_address.grid(row=3, column=0,sticky="w",padx=20)
    entry_address=customtkinter.CTkEntry(add_cont,bg_color="black",width=200,placeholder_text="ex. westbengal india ")
    entry_address.grid(row=3, column=1,sticky="w")
    buton_save=customtkinter.CTkButton(add_cont,text="Save", command=saving_data)
    buton_save.grid(row=4,column=0,columnspan=2,sticky="ew",padx=20,pady=20)
    

def delete_cont(J):
    global r
    try:
        with open("contacts.json","r") as file:
            contacts=json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        messagebox.showwarning("WARNING", "Some Issue Occured")
        contacts=[]
    #dellist=[todo for todo in task if todo["id"] == i]
    contact_list= [todo for todo in contacts if todo["id"] != J]
        
    with open("contacts.json","w") as file:
        json.dump(contact_list,file , indent=4)

    messagebox.showinfo("DELETED:", "Contact Deleted")
    for widget in scroll_frame.winfo_children():
        widget.destroy()  # clear all old widgets
    r = 0
    view()
def update_cont(J):
    def saving_update():
        global name_input,add_input,email_input, phone_input
        name_input=entry_name.get()
        phone_input=entry_phone.get()
        add_input=entry_address.get()
        email_input=entry_email.get()

        if name_input == "" or phone_input == "" or email_input == "" or add_input == "":
            messagebox.showwarning("Missing Data", "All fields must be filled!")
            return

    # Phone number validation (must be 10 digits & numeric)
        if not phone_input.isdigit() or len(phone_input) != 10:
            messagebox.showwarning("Invalid Phone", "Phone number must be 10 digits!")
            return

    # Email validation using regex
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email_input):
            messagebox.showwarning("Invalid Email", "Enter a valid email address!")
            return

        # data file reading
        try :
            with open ("contacts.json","r")as file:
                contact_lists=json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showwarning("WARNING:", "Some Issue Occured!")
            contact_lists=[]
    

        for c in contact_lists:
            if c["id"]==J:
                c["name"]=name_input
                c["phone"]=phone_input
                c["email"]=email_input
                c["address"]=add_input

        #dump
        with open("contacts.json","w") as file:
            json.dump(contact_lists,file,indent=4)
        messagebox.showinfo("SUCCESS:", " Contact Updated Successfully")

        update.destroy()

        view()

    try:
        with open("contacts.json","r") as file:
            contacts=json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        messagebox.showwarning("WARNING", "Some Issue Occured")
        contacts=[]
    
    for c in contacts:
        if c["id"]==J:
            updateing=c

    #new dialouge box
    update= customtkinter.CTkToplevel()
    update.title("Add New Contact")
    update.geometry("400x300")
    update.grab_set()  # main window ke lock kore, ei popup ke active rakhe


    #new task, priority input
    label_new_name=customtkinter.CTkLabel(update,text="enter name:",font=("verdana",14),height=35, width=120)
    label_new_name.grid(row=0, column=0,sticky="w",padx=20)
    entry_name=customtkinter.CTkEntry(update,bg_color="black",width=200)
    entry_name.grid(row=0, column=1,sticky="w")
    entry_name.insert(0,updateing["name"])
    label_new_phone=customtkinter.CTkLabel(update,text="enter phone no:",font=("verdana",14),height=35,width=120)
    label_new_phone.grid(row=1, column=0,sticky="w",padx=20)
    entry_phone=customtkinter.CTkEntry(update,bg_color="black",width=200)
    entry_phone.grid(row=1, column=1,sticky="w")
    entry_phone.insert(0,updateing["phone"])
    label_new_email=customtkinter.CTkLabel(update,text="enter email:",font=("verdana",14),height=35,width=120)
    label_new_email.grid(row=2, column=0,sticky="w",padx=20)
    entry_email=customtkinter.CTkEntry(update,bg_color="black",width=200)
    entry_email.grid(row=2, column=1,sticky="w")
    entry_email.insert(0,updateing["email"])
    label_new_address=customtkinter.CTkLabel(update,text="enter address:",font=("verdana",14),height=35,width=120)
    label_new_address.grid(row=3, column=0,sticky="w",padx=20)
    entry_address=customtkinter.CTkEntry(update,bg_color="black",width=200)
    entry_address.grid(row=3, column=1,sticky="w")
    entry_address.insert(0,updateing["address"])
    buton_save=customtkinter.CTkButton(update,text="Save", command=saving_update)
    buton_save.grid(row=4,column=0,columnspan=2,sticky="ew",padx=20,pady=20)
    

    
    
def view():
    global r
    for widget in scroll_frame.winfo_children():
        widget.destroy() 
    #data file fetch
    try:
        with open("contacts.json","r") as file:
            contacts=json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        label_view_error=customtkinter.CTkLabel(scroll_frame,text="warning : some issue occured")
        label_view_error.grid(row=0,column=1)
        contacts=[]
    contact_sorted=sorted(contacts, key=lambda x: x["name"])  
    id_list=[item["id"] for item in contact_sorted]
    name_list=[item["name"] for item in contact_sorted]
    phone_list=[item["phone"]for item in contact_sorted]
    email_list=[item["email"] for item in contact_sorted]
    address_list=[item["address"] for item in contact_sorted]
    #print high low instead of 123
    n=len(id_list)
    #print
    if n>0:
        for i in range(0,n):
            j=id_list[i]
            cview = customtkinter.CTkFrame(scroll_frame, corner_radius=10)
            cview.grid(row=r, column=0, padx=20, pady=10, sticky="ew", columnspan=7)
            

            label_names=customtkinter.CTkLabel(cview,text=f"👤 {name_list[i]}",font=("verdana",20))
            label_names.grid(row=r,column=0,columnspan=2,sticky="w",pady=5,padx=30)
            label_phoneno=customtkinter.CTkLabel(cview,text=f"📞 {phone_list[i]}",font=("verdana",12))
            label_phoneno.grid(row=r+1,column=0, columnspan=2,sticky="w",pady=5,padx=30)
            label_email=customtkinter.CTkLabel(cview,text=f"✉️ {email_list[i]}",font=("verdana",12))
            label_email.grid(row=r+2,column=0,columnspan=2,sticky="w",pady=5,padx=30)
            label_address=customtkinter.CTkLabel(cview,text=f"🏠 {address_list[i]}",font=("verdana",12))
            label_address.grid(row=r+3,column=0,columnspan=2,sticky="w",pady=5,padx=30)
            button_delete=customtkinter.CTkButton(cview,text="edit", width=20,command=lambda j=j:update_cont(j))
            button_delete.grid(row=r+1, column=9,sticky="e",padx=20,pady=5)
            button_update=customtkinter.CTkButton(cview,text="Delete", width=20,command=lambda j=j:delete_cont(j))
            button_update.grid(row=r+2, column=9,sticky="e",padx=20,pady=5)

            r=r+3
    else:
        label_view1_error=customtkinter.CTkLabel(scroll_frame,text="NO TASK AVAILABLE")
        label_view1_error.grid(row=r,column=0)
        r=r+1


app=customtkinter.CTk()
app.geometry("800x800")
app.title("📒MY CONTACTS...")

label_title=customtkinter.CTkLabel(app, text="Contacts",font=("verdana",30,"bold"), height=35,width=120)
label_title.pack(pady=20)

main_frame=customtkinter.CTkFrame(app)
main_frame.pack(pady=10)

search_entry=customtkinter.CTkEntry(main_frame,placeholder_text="search contact by name or number...",font=("verdana",16),width=700,height=40)
search_entry.grid(row=0,column=0,padx=10,pady=2,sticky="ew")
button_search=customtkinter.CTkButton(main_frame,text="search",font=("verdana",30),width=40,height=40,command=search_contact)
button_search.grid(row=0,column=1,padx=0,pady=2,sticky="ew")
button_plus = customtkinter.CTkButton(main_frame, text="+",font=("verdana",30), width=40, height=40,command=add_contact)
button_plus.grid(row=0, column=2,padx=0,pady=2, sticky="w")



canvas=customtkinter.CTkCanvas(app, height=500, width=850)
canvas.pack(side="left",fill="both", expand=True,padx=(20,0),pady=20)

#scroll if no. of task gets higher
scroll=customtkinter.CTkScrollbar(app,orientation="vertical", command=canvas.yview)
scroll.pack(side="right", fill="y", pady=20)

canvas.configure(yscrollcommand=scroll.set)

# Frame inside canvas
scroll_frame = customtkinter.CTkFrame(canvas)
scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

for i in range(0, 9):  # max column 9
    scroll_frame.grid_columnconfigure(i, weight=1)

canvas.create_window((0,0), window=scroll_frame, anchor="nw",width=2000)
scroll_frame.configure(fg_color=app._fg_color)
r=2
view()
app.mainloop()