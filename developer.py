from tkinter  import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def  __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"college_images\dev.jpg")
        img_top = img_top.resize((1530, 720))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        
        # ============== frame ============
        
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=55,width=500,height=600)
        
        img1_top=Image.open(r"college_images\shiv.jpeg")
        img1_top = img1_top.resize((200, 200))
        self.photoimg1_top = ImageTk.PhotoImage(img1_top)
        
        f_lbl=Label(main_frame,image=self.photoimg1_top)
        f_lbl.place(x=290,y=0,width=200,height=200)
        
######  dev Info ######
    
        dep_label=Label(main_frame,text="Hello , my name is shivling",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white",fg="blue")
        dep_label.place(x=0,y=5)
        
        dep_label=Label(main_frame,text="I am a Full Stack Developer !!!",font=("times new roman",12,"bold"),padx=8,pady=5,bg="white",fg="blue")
        dep_label.place(x=0,y=40)
        
        
        img2=Image.open(r"college_images\dev1.jpg")
        img2 = img2.resize((500, 380))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=380)  































        
if  __name__=="__main__":
    
    root = Tk()
    obj =Developer(root)
    root.mainloop()