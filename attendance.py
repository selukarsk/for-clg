from tkinter  import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendance:
    def  __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
# ============ variables ===============

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        


# first image  
        
        img=Image.open(r"college_images\smart-attendance.jpg")
        img=img.resize((800,200,))
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
  
  
# image 2
        img1=Image.open(r"college_images\clg.jpg")
        img1= img1.resize((800, 200))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        
  
# bg image
     
        img3=Image.open(r"college_images\bg.jpg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)
        
        
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)
        
        #### left label frame ####
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=580)
        
        img_left=Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        left_inside_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Attendance",font=("times new roman",12,"bold"))
        left_inside_frame.place(x=0,y=200,width=720,height=370)
        
        # Label entry 
        # attendance id 
        
        attendanceID_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10)
        
        # roll
        
        roll_label=Label(left_inside_frame,text="Roll No:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        roll_label.grid(row=0,column=2,padx=10)
        
        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=10)
        
        
        # name 
        
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        name_label.grid(row=1,column=0,padx=10)
        
        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=10)
        
        
        # dep 
        
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        dep_label.grid(row=1,column=2,padx=10)
        
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=10)
        
        
        
        # time 
        
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        time_label.grid(row=2,column=0,padx=10)
        
        tten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        tten_time.grid(row=2,column=1,padx=10)
        
        # date
        
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white")
        date_label.grid(row=2,column=2,padx=10)
        
        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,padx=10)
        
        # attendance status
        
        attendance_label=Label(left_inside_frame,text="Attendance Status:",font=("comicsansns 11 bold",11,"bold"),padx=8,pady=5,bg="white")
        attendance_label.grid(row=3,column=0,pady=10)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=10)
        self.atten_status.current(0)
        
        
        # Button frame 
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=715,height=40)
        
        
        import_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=19,font=("times new roman",12,"bold"),bg= "green",fg="white")
        import_btn.grid(row=0,column=0)
        
        export_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=19,font=("times new roman",12,"bold"),bg= "green",fg="white")
        export_btn.grid(row=0,column=1)
        
        update_btn=Button(btn_frame,text="Update",width=19,command=self.update_data,font=("times new roman",12,"bold"),bg= "green",fg="white")
        update_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",width=19,command=self.reset_data,font=("times new roman",12,"bold"),bg= "green",fg="white")
        reset_btn.grid(row=0,column=3)

      
      
      
      #### right label frame ####
      
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)
        
        # ================= scroll bar ==========
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
# ==================== fetch data =============

    def fetchData(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                    self.AttendanceReportTable.insert("",END,values=i)
                
# =====================import csv ===============

    def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                    csvread=csv.reader(myfile,delimiter=",")
                    for i in csvread:
                            mydata.append(i)
                    self.fetchData(mydata)
                    
#   ===================== export csv ==================
    
    def exportCsv(self):
            
            
            try:
                    if len(mydata)<1:
                            messagebox.showerror("No Data","No Data found to export",parent=self.root)
                            return False
                    fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                    with open(fln,mode="w",newline="") as myfile:
                            exp_write=csv.writer(myfile,delimiter=",")
                            for i in mydata:
                                    exp_write.writerow(i)
                            messagebox.showinfo("Data Export","Data Exported to"+os.path.basename(fln)+"successfully")
                
            except Exception as es:
                        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                   
                
    def get_cursor(self,event=""):
            cursor_row=self.AttendanceReportTable.focus()
            content=self.AttendanceReportTable.item(cursor_row)
            rows=content['values']
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])
                
                
    def reset_data(self):
            self.var_atten_id.set("")
            self.var_atten_roll.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set("")
            
                
                
    def update_data(self):
        # Get the selected row's index
        selected_row = self.AttendanceReportTable.focus()
        
        if not selected_row:
            messagebox.showerror("Error", "Please select a record to update.", parent=self.root)
            return
        
        # Get the values from the entry fields
        atten_id = self.var_atten_id.get()
        atten_roll = self.var_atten_roll.get()
        atten_name = self.var_atten_name.get()
        atten_dep = self.var_atten_dep.get()
        atten_time = self.var_atten_time.get()
        atten_date = self.var_atten_date.get()
        atten_attendance = self.var_atten_attendance.get()
        
        # Validate required fields
        if not (atten_id and atten_roll and atten_name and atten_dep and atten_time and atten_date and atten_attendance):
            messagebox.showerror("Error", "All fields are required.", parent=self.root)
            return
        
        # Update the selected row's values
        updated_data = (atten_id, atten_roll, atten_name, atten_dep, atten_time, atten_date, atten_attendance)
        self.AttendanceReportTable.item(selected_row, values=updated_data)
        
        messagebox.showinfo("Success", "Record updated successfully.", parent=self.root)
        
        # Clear the entry fields after update
        self.reset_data()

            
                
                
                
                
                
                



        
if  __name__=="__main__":
    
    root = Tk()
    obj =Attendance(root)
    root.mainloop()