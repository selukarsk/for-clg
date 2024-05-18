from tkinter  import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def  __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

#================ variables ==================

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
       
        
        
        



# first image  
        
        img=Image.open(r"college_images\iStock-1163542789-945x630.jpg")
        img=img.resize((500,130,))
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
  
  
# image 2
        img1=Image.open(r"college_images\bg3.jpg")
        img1= img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=525,height=130)
        
# image 3
        img2=Image.open(r"college_images\smart-attendance.jpg")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=525,height=130)      
  
  
# bg image
     
        img3=Image.open(r"college_images\bg1.jpg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)
        
        #### left label frame ####
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=580)
      
        
        img_left=Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130) 
        

        #### current course information ####
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)
######  Department ######
    
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        dep_combo['values']=('Select Department',"Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
###### Course ####### 
    
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        course_label.grid(row=0,column=2,padx=10)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="readonly")
        course_combo['values']=('Select Course',"FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
######   Year   ######
    
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        year_label.grid(row=1,column=0,padx=10)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="readonly")
        year_combo['values']=('Select Year',"2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
######   Semester   ######
    
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        semester_label.grid(row=1,column=2,padx=10)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=20,state="readonly")
        semester_combo['values']=('Select Semester',"Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
######  Class Student information ####
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

###### student id ####        
        StudentId_label=Label(class_student_frame,text="StudentId:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        StudentId_label.grid(row=0,column=0,padx=10)
        
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10)
        
####### student name  ###### 
        StudentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        StudentName_label.grid(row=0,column=2,padx=10)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10)

######  class division  #######
        Class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        Class_div_label.grid(row=1,column=0,padx=10)
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        div_combo['values']=('A',"B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
###### Roll No ########
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        roll_no_label.grid(row=1,column=2,padx=10)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10)
        
### gender  ####
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo['values']=('Male',"Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)
  
        
###### DOB ######
        dob_label=Label(class_student_frame,text="Date of Birth:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        dob_label.grid(row=2,column=2,padx=10)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10)

##### E-mail ########
        email_label=Label(class_student_frame,text="E-mail:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        email_label.grid(row=3,column=0,padx=10)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10)
        
##### Mo no. ##### 
        mo_no_label=Label(class_student_frame,text="Mo.no:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        mo_no_label.grid(row=3,column=2,padx=10)
        
        mo_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        mo_no_entry.grid(row=3,column=3,padx=10)
        
#######  Address  ######
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        address_label.grid(row=4,column=0,padx=10)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10)
        
####### teacher name ########
        teacher_name_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        teacher_name_label.grid(row=4,column=2,padx=10)
        
        teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10)
        
#########     radio buttons
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(class_student_frame,text="take a photo sample",variable=self.var_radio1,value="Yes")
        Radiobutton1.grid(row=6,column=0)
        
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No a photo sample",value="No")
        Radiobutton1.grid(row=6,column=1)
        
        # Button frame 
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=715,height=35)
        
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg= "green",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg= "green",fg="white",command=self.update_data)
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg= "green",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg= "green",fg="white")
        reset_btn.grid(row=0,column=3)
        
         # Button frame 
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=250,width=715,height=35)
              
        take_photo_btn=Button(btn_frame1,text="Take Photo",command=self.generate_dataset,width=40,font=("times new roman",12,"bold"),bg= "green",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update Photo",command=self.update_photo,width=40,font=("times new roman",12,"bold"),bg= "green",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        

         #### right label frame ####
        
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=740,height=580)
        
        right=Image.open(r"college_images\student.jpg")
        right = right.resize((720, 130))
        self.right = ImageTk.PhotoImage(right)
        
        f_lbl=Label(right_frame,image=self.right)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        
# ======================= Search system ============================

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)
        
        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),padx=8,pady=5,bg="orange",fg="white")
        search_label.grid(row=0,column=0,padx=10)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo['values']=('Select',"Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10)
        
        
        search_btn=Button(search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg= "blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg= "blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)


#  ================ table frame ==================

         
        table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(
                table_frame,
                columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"),
                xscrollcommand=scroll_x.set,
                yscrollcommand=scroll_y.set
        )
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Mo_no")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)  
        self.student_table.column("div", width=100)   
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        
        
# ================= function declaration =================

    def add_data(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
                
        else:
                try:
                                conn=mysql.connector.connect(host="localhost",port="3306",username="root",password="123",database="face_recognizer",ssl_disabled=True)
                                my_cursor=conn.cursor()
                                my_cursor.execute('''INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_id.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get()
                                        
                                                                                                                                
                                                                                                                                ) )
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
                
                except Exception as es:
                        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
               
               
# =================== fetch data =================
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",port="3306",username="root",password="123",database="face_recognizer",ssl_disabled=True)
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()
            
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                        self.student_table.insert('', 'end', values=i)
                conn.commit()
            conn.close()
                    
    
        
# ===================== get cursor =================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
        
        
    # ==================== update function ================

    def update_data(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
             try:
                 Update=messagebox.askyesno("Update","Do you want to update this student details",parent = self.root)
                 if Update>0:
                         conn=mysql.connector.connect(host="localhost",port="3306",username="root",password="123",database="face_recognizer",ssl_disabled=True)
                         my_cursor=conn.cursor()
                         my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                 
                                
                                 self.var_dep.get(),
                                 self.var_course.get(),
                                 self.var_year.get(),
                                 self.var_semester.get(),
                                 self.var_std_name.get(),
                                 self.var_div.get(),
                                 self.var_roll.get(),
                                 self.var_gender.get(),
                                 self.var_dob.get(),
                                 self.var_email.get(),
                                 self.var_phone.get(),
                                 self.var_address.get(),
                                 self.var_teacher.get(),
                                 self.var_radio1.get(),
                                 self.var_std_id.get()
                                 
                                            
))
                 else:
                         if not Update:
                                return
                 messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                                   
             except Exception  as es:
                     messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



    ############# delete function ####################

    def delete_data(self):
            if self.var_std_id.get()=="":
                    messagebox.showerror("Error","Student Id must be required",parent=self.root)
            else:
                    try:
                            delete=messagebox.askyesno("Student Delete Page","Do you Want to delete this student",parent=self.root)
                            if delete>0:
                                conn=mysql.connector.connect(host="localhost",port="3306",username="root",password="123",database="face_recognizer",ssl_disabled=True)
                                my_cursor=conn.cursor()
                                sql="delete from student where Student_id=%s"
                                val=(self.var_std_id.get(),)
                                my_cursor.execute(sql,val)
                            
                            else:
                                    if not delete:
                                            return
                            conn.commit()
                            self.fetch_data()
                            conn.close()
                            messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
                    
                    except Exception  as es:
                     messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)        




  ########### Reset function ###########
    def reset_data(self):
            self.var_dep.set("Select Department")
            self.var_course.set("Select Course")
            self.var_year.set("Select Year")
            self.var_semester.set("Select Semester")
            self.var_std_id.set("")
            self.var_std_name.set("")
            self.var_div.set("Select Division")
            self.var_roll.set("")
            self.var_gender.set("Male")
            self.var_dob.set("")
            self.var_email.set("")
            self.var_phone.set("")
            self.var_address.set("")
            self.var_teacher.set("")
            self.var_radio1.set("")
            
            
            
        #     ========================  update photo =========================
        
        
    def update_photo(self):
        try:
            if self.var_std_id.get() == "":
                messagebox.showerror("Error", "Please select a student to update the photo.", parent=self.root)
                return
            
            # Initialize face classifier for face detection
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
            # Function to crop faces from input frame
            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                
                for (x, y, w, h) in faces:
                    face_cropped = img[y:y+h, x:x+w]
                    return face_cropped
    
            # Open video capture device (webcam)
            cap = cv2.VideoCapture(0)
            img_id = 0
    
            while True:
                # Capture frame-by-frame
                ret, my_frame = cap.read()
    
                # Detect and crop face from the frame
                cropped_face = face_cropped(my_frame)
    
                if cropped_face is not None:
                    img_id += 1
                    
                    # Resize and convert to grayscale
                    face = cv2.resize(cropped_face, (450, 450))
                    face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    
                    # Define file path for saving cropped face
                    file_name_path = f"data/user.{self.var_std_id.get()}.{img_id}.jpg"
    
                    # Save cropped face image
                    cv2.imwrite(file_name_path, face_gray)
    
                    # Display cropped face with image ID
                    cv2.putText(face_gray, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 2)
                    cv2.imshow("Cropped Face", face_gray)
                
                # Check for key press to exit loop (Enter key or limit of 50 images)
                if cv2.waitKey(1) == 13 or img_id == 100:
                    break
    
            # Release video capture device and close OpenCV windows
            cap.release()
            cv2.destroyAllWindows()
    
            # Display completion message
            messagebox.showinfo("Result", "Photo updated successfully.")
    
        except Exception as es:
            # Display error message in case of exception
            messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)

        
        
            
   #=========== generate data set or take photo samples ==========         

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Connect to MySQL database
                conn = mysql.connector.connect(host="localhost", port="3306", username="root", password="123", database="face_recognizer",ssl_disabled=True)
                my_cursor = conn.cursor()

                # Fetch all records from 'student' table
                my_cursor.execute("SELECT * FROM student")
                myreslut = my_cursor.fetchall()
                id=self.var_std_id.get()
                for x in myreslut:
                    id=id
                    
                # myresult = my_cursor.fetchall()
                
                # # Calculate the next available student ID
                # id = len(myresult) + 1

                # Update student record in the database
                update_query = "UPDATE student SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s"
                update_data = (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                               self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(),
                               self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                               self.var_teacher.get(), self.var_radio1.get(), id)
                my_cursor.execute(update_query, update_data)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Initialize face classifier for face detection
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                # Function to crop faces from input frame
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                    
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                # Open video capture device (webcam)
                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    # Capture frame-by-frame
                    ret, my_frame = cap.read()

                    # Detect and crop face from the frame
                    cropped_face = face_cropped(my_frame)

                    if cropped_face is not None:
                        img_id += 1
                        
                        # Resize and convert to grayscale
                        face = cv2.resize(cropped_face, (450, 450))
                        face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        # Define file path for saving cropped face
                        file_name_path = f"data/user.{id}.{img_id}.jpg"

                        # Save cropped face image
                        cv2.imwrite(file_name_path, face_gray)

                        # Display cropped face with image ID
                        cv2.putText(face_gray, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 2)
                        cv2.imshow("Cropped Face", face_gray)
                    
                    # Check for key press to exit loop (Enter key or limit of 100 images)
                    if cv2.waitKey(1) == 13 or img_id == 50:
                        break

                # Release video capture device and close OpenCV windows
                cap.release()
                cv2.destroyAllWindows()

                # Display completion message
                messagebox.showinfo("Result", "Generating datasets completed!!!")

            except Exception as es:
                # Display error message in case of exception
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)












        
if  __name__=="__main__":
    
    root = Tk()
    obj =Student(root)
    root.mainloop()