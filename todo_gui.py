import customtkinter
import json
import random
#done job view function
def done_task(c):
    global r
    try:
        with open("data.json","r") as file:
            all_data=json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        label_problem=customtkinter.CTkLabel(scroll_frame,text="warning : some issue occured")
        label_problem.grid(row=r,column=0)
        all_data=[]
    uplist=[todo for todo in all_data if todo["id"]==c]
    todo_list=[todo for todo in all_data if todo["id"]!=c]
    with open("data.json","w") as file:
        json.dump(todo_list,file,indent=4)
    print("checked successfully")
    try:
        with open("updateted_data.json","r") as file:
            updated=json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        label_update_error2=customtkinter.CTkLabel(scroll_frame,text="warning:some issuess occured")
        label_update_error2.grid(row=r,column=0)
        updated=[]
    updated.append(uplist[0])
    with open("updateted_data.json","w") as file:
        json.dump(updated,file ,indent=4)
    for widget in scroll_frame.winfo_children():
        widget.destroy()
    r = 0
    view()
    done_view()
def delete_updated_task(l):
    global r
    try:
        with open("updateted_data.json","r") as file:
            updates=json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        label_delete_error=customtkinter.CTkLabel(scroll_frame,text="warning: some issues occured")
        label_delete_error.grid(row=r,column=0)
        updates=[]
    dellist=[todo for todo in updates if todo["id"] == l]
    todolist= [todo for todo in updates if todo["id"] != l]
        
    with open("updateted_data.json","w") as file:
        json.dump(todolist,file , indent=4)
    print("deleted succesfully")
    try:
        with open ("deleted_data.json","r") as file:
            deleted=json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        label_delete_error2=customtkinter.CTkLabel(scroll_frame,text="warning:some issuess occured")
        label_delete_error2.grid(row=r,column=0)
        deleted=[]
    deleted.append(dellist[0])
    with open("deleted_data.json","w") as file:
        json.dump(deleted,file ,indent=4)
    for widget in scroll_frame.winfo_children():
        widget.destroy()
    r = 0
    view()
    done_view()
    

def delete_task(i):
    global r
    try:
        with open("data.json","r") as file:
            task=json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        label_delete_error=customtkinter.CTkLabel(scroll_frame,text="warning: some issues occured")
        label_delete_error.grid(row=r,column=0)
        task=[]
    dellist=[todo for todo in task if todo["id"] == i]
    todolist= [todo for todo in task if todo["id"] != i]
        
    with open("data.json","w") as file:
        json.dump(todolist,file , indent=4)

    print("deleted succesfully")
    try:
        with open ("deleted_data.json","r") as file:
            deleted=json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        label_delete_error2=customtkinter.CTkLabel(scroll_frame,text="warning:some issuess occured")
        label_delete_error2.grid(row=r,column=0)
        deleted=[]
    deleted.append(dellist[0])
    with open("deleted_data.json","w") as file:
        json.dump(deleted,file ,indent=4)
    for widget in scroll_frame.winfo_children():
        widget.destroy()  # clear all old widgets
    r = 0
    view()
    done_view()

def done_view():
    global r
    label_done=customtkinter.CTkLabel(scroll_frame, text="Done",font=("verdana",30), height=35,width=120,fg_color="transparent")
    label_done.grid(row=r, column=0, padx=20 , pady=20 , sticky="w")
    r=r+1
    try:
        with open("updateted_data.json","r") as file:
            done=json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        label_update_error=customtkinter.CTkLabel(scroll_frame,text="warning : some issue occured, previous all to-do is deleted")
        label_update_error.grid(row=r,column=0)
        r=r+1
        done=[]
    id_u_list=[item["id"] for item in done]
    name_u_list=[item["name"] for item in done]
    priority_u_list=[item["priority"]for item in done]
    m=len(id_u_list)
    if m>0:
        for i in range(0,m):
            j=id_u_list[i]
            check_updated_value=customtkinter.BooleanVar(value=True)
            check_updates=customtkinter.CTkCheckBox(scroll_frame,text="",variable=check_updated_value)
            check_updates.grid(rowspan=2,column=0, sticky="w")

            label_dones=customtkinter.CTkLabel(scroll_frame,text=f"{name_u_list[i]}",font=("verdana",14,"overstrike"))
            label_dones.grid(row=r,column=1,columnspan=2,sticky="w")

            label_uppriority=customtkinter.CTkLabel(scroll_frame,text=f"{priority_u_list[i]}",font=("verdana",10))
            label_uppriority.grid(row=r+1,column=1, columnspan=2,sticky="w")    
            button_u_delete=customtkinter.CTkButton(scroll_frame,text="Delete", width=20,command=lambda j=j:delete_updated_task(j))
            button_u_delete.grid(row=r, column=4,sticky="e")
            r=r+2
    else:
        label_update1_error=customtkinter.CTkLabel(scroll_frame,text="NO TASK AVAILABLE")
        label_update1_error.grid(row=r,column=0)
        r=r+1


#view function
def view():
    global r
    #data file fetch
    try:
        with open("data.json","r") as file:
            task=json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        label_view_error=customtkinter.CTkLabel(scroll_frame,text="warning : some issue occured, previous all to-do is deleted")
        label_view_error.grid(row=r,column=0)
        r=r+1
        task=[]
    #sorthing by prority
    task_sorted=sorted(task, key=lambda x: x["priority"])
    #data collecting in different list
    id_list=[item["id"] for item in task_sorted]
    name_list=[item["name"] for item in task_sorted]
    priority_list=[item["priority"]for item in task_sorted]
    #print high low instead of 123
    pt={1:"high",2:"medium",3:"low"}
    priority_list2 = [pt[plt] for plt in priority_list ]
    n=len(id_list)
    #print
    if n>0:
        for i in range(0,n):
            j=id_list[i]
            check_value=customtkinter.BooleanVar(value=False)
            check_tasks=customtkinter.CTkCheckBox(scroll_frame,text="",variable=check_value, command=lambda j=j: done_task(j))
            check_tasks.grid(row=r,rowspan=2,column=0, sticky="w")
            label_tasks=customtkinter.CTkLabel(scroll_frame,text=f"{name_list[i]}",font=("verdana",14))
            label_tasks.grid(row=r,column=1,columnspan=2,sticky="w")
            label_priority=customtkinter.CTkLabel(scroll_frame,text=f"{priority_list2[i]}",font=("verdana",10))
            label_priority.grid(row=r+1,column=1, columnspan=2,sticky="w")
            button_delete=customtkinter.CTkButton(scroll_frame,text="Delete", width=20,command=lambda j=j:delete_task(j))
            button_delete.grid(row=r, column=4,sticky="e")
            r=r+2
    else:
        label_view1_error=customtkinter.CTkLabel(scroll_frame,text="NO TASK AVAILABLE")
        label_view1_error.grid(row=r,column=0)
        r=r+1

#adding new task
def add_task():
    def saving_data():
        global task_input
        task_input=entry_task.get()
        print(prio,task_input)
        # data file reading
        try :
            with open ("data.json","r")as file:
                todolists=json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("warning : some issue occured, previous all to-do is deleted ")
            todolists=[]
    

        # handling unique id
        id_list=[ item["id"] for item in todolists]
        id= random.randint(100,500)
        while id in id_list:
            id =random.randint(100,500)

        #generating new to-do dict
        todo ={"id":id,"name":task_input,"priority":prio,"checked":False}
        todolists.append(todo)


        #dump
        with open("data.json","w") as file:
            json.dump(todolists,file,indent=4)
        print("new to-do added successfully")

        # for fresshing the screen we will delete all the widget
        for widget in scroll_frame.winfo_children():
            widget.destroy()
        entry_task.delete(0, "end")

        # saved data display
        view()
        done_view()
    

    def priority_selected(prt):
        p={"medium":2,"low":3,"high":1}
        global prio
        prio=p[prt]

    #sub screen new
    app1 = customtkinter.CTk()
    app1.geometry("450x200")

    #new task, priority input
    label_new_tasks=customtkinter.CTkLabel(app1,text="enter new task:",font=("verdana",14),height=35, width=120)
    label_new_tasks.grid(row=0, column=0,sticky="e",padx=20)
    entry_task=customtkinter.CTkEntry(app1,bg_color="black",width=200,placeholder_text="ex. python coding ")
    entry_task.grid(row=0, column=1,sticky="w")
    option_priority=customtkinter.CTkOptionMenu(app1,values=["high","medium","low"],command=lambda value:priority_selected(value),width=200)
    option_priority.grid(row=1, column=0,columnspan=2,sticky="ew",padx=20,pady=20)
    option_priority.set("medium")


    buton_save=customtkinter.CTkButton(app1,text="Save", command=saving_data)
    buton_save.grid(row=2,column=0,columnspan=2,sticky="ew",padx=20,pady=20)
    app1.mainloop()

#starting , screen size, title
app = customtkinter.CTk()
app.geometry("800x800")
app.title("What To Do !?")

#task + button
label_tasks=customtkinter.CTkLabel(app, text="Task",font=("verdana",30), height=35,width=120)
label_tasks.grid(row=0, column=0, padx=20 , pady=20 , sticky="w")
button_plus = customtkinter.CTkButton(app, text="+",font=("verdana",30), width=40, height=40,corner_radius=100, command=add_task)
button_plus.grid(row=0, column=0,padx=20 ,pady=20, sticky="e")

#canvas
canvas=customtkinter.CTkCanvas(app, height=760, width=1500)
canvas.grid(row=1,column=0,columnspan=5,padx=20,pady=20)

#scroll if no. of task gets higher
scroll=customtkinter.CTkScrollbar(app,orientation="vertical", command=canvas.yview)
scroll.grid(row=1,column=10, sticky="ns",pady=20)

canvas.configure(yscrollcommand=scroll.set)

# Frame inside canvas
scroll_frame = customtkinter.CTkFrame(canvas, height=760, width=2000)
scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

for i in range(0, 9):  # max column 9
    scroll_frame.grid_columnconfigure(i, weight=1)

canvas.create_window((0,0), window=scroll_frame, anchor="nw",width=2000)
scroll_frame.configure(fg_color=app._fg_color)
r=0
view()
done_view()
app.mainloop()