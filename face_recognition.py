# from tkinter  import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# from time import strftime
# from datetime import datetime
# import csv
# import cv2
# import os
# import numpy as np


# class Face_Recognition:
#     def  __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")
        
#         title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
#         title_lbl.place(x=0,y=0,width=1530,height=45)
#         #  left img
#         img_left=Image.open(r"college_images\face_detector1.jpg")
#         img_left = img_left.resize((650, 700))
#         self.photoimg_left = ImageTk.PhotoImage(img_left)
        
#         f_lbl=Label(self.root,image=self.photoimg_left)
#         f_lbl.place(x=0,y=55,width=650,height=700)
        
#         # right img
#         img_right=Image.open(r"college_images\face.jpg")
#         img_right = img_right.resize((950, 700))
#         self.photoimg_right = ImageTk.PhotoImage(img_right)
        
#         f_lbl=Label(self.root,image=self.photoimg_right)
#         f_lbl.place(x=650,y=55,width=950,height=700)
        
#         # button 
#         b1_btn=Button(f_lbl,text="Face Recognition",command=self.face_recog,font=("times new roman",18,"bold"),bg= "darkgreen",fg="white")
#         b1_btn.place(x=365,y=620,width=200,height=40)
        
#     # ============ attendance ============
#     def mark_attendance(self, student_id, roll, name, department):
#         current_date = datetime.now().strftime("%d/%m/%Y")
#         current_time = datetime.now().strftime("%H:%M:%S")
        
#         # Check if the student is already marked present for today
#         with open("attendance.csv", "a+", newline="\n") as f:
#             f.seek(0)  # Move the cursor to the start of the file for reading
#             reader = csv.reader(f)
#             rows = list(reader)
            
#             # Filter rows for the current date and the specified student ID
#             filtered_rows = [row for row in rows if row and row[0] == str(student_id) and row[5] == current_date]
            
#             if not filtered_rows:  # Student hasn't been marked present today
#                 # Append attendance record to the file
#                 with open("attendance.csv", "a", newline="\n") as f:
#                     writer = csv.writer(f)
#                     writer.writerow([student_id, roll, name, department, current_time, current_date, "Present"])
#                     print(f"Attendance marked for {name} ({roll}) - {department} on {current_date}")
            
#  ### ====================  face recognition ==================
#     def face_recog(self):
#         def draw_boundry(img, classifier, scaleFactor, minNeighbors, color, text, clf):
#             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=(50, 50), maxSize=(200, 200))
#             # features = classifier.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
            
#             coord = []
#             for (x, y, w, h) in features:
#                 cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                
#                 face_roi = gray_image[y:y+h, x:x+w]
#                 id, predict = clf.predict(face_roi)
#                 confidence = int((100 * (1 - predict / 300)))
                
#                 # Establish MySQL connection
#                 conn = mysql.connector.connect(host="localhost", port="3306", username="root", password="123", database="face_recognizer", ssl_disabled=True)
#                 my_cursor = conn.cursor()
                
#                 # Retrieve student information from database based on Student_id
#                 my_cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id = %s", (id,))
#                 result = my_cursor.fetchone()
#                 if result:
#                     name, roll, dep = result
                    
#                     # Convert to string and handle potential None values
#                     n = name if name else ""
#                     r = roll if roll else ""
#                     d = dep if dep else ""
#                     i = str(id) if id else ""

#                     # Display information on the image if confidence is high
#                     if confidence > 80:
#                         cv2.putText(img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                         cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                         cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                         cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                         # Assuming mark_attendance is defined elsewhere
#                         self.mark_attendance(i,r,n,d)
#                     else:
#                         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
#                         cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                
#                 # Close MySQL connection
#                 conn.close()
                
#                 coord = [x, y, w, h]  # Update coord with the last detected face coordinates
            
#             return coord

        
#         def recognize(img,clf,faceCascade):
#             coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
#             return img
        
#         faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf=cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier.xml")
        
#         video_cap=cv2.VideoCapture(0)
        
#         while True:
#             ret,img=video_cap.read()
#             img=recognize(img,clf,faceCascade)
#             cv2.imshow("Welcome To Face Recognition",img)
            
            
#             if cv2.waitKey(1)==13:
#                 break
#         video_cap.release()
#         cv2.destroyAllWindows()
            



# if  __name__=="__main__":
    
#     root = Tk()
#     obj =Face_Recognition(root)
#     root.mainloop()





from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
import csv
import cv2
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Left image
        img_left = Image.open(r"college_images/face_detector1.jpg")
        img_left = img_left.resize((650, 700))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # Right image
        img_right = Image.open(r"college_images/face.jpg")
        img_right = img_right.resize((950, 700))
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_btn = Button(f_lbl, text="Face Recognition", command=self.face_recog, font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_btn.place(x=365, y=620, width=200, height=40)

    def mark_attendance(self, student_id, roll, name, department):
        current_date = datetime.now().strftime("%d/%m/%Y")
        current_time = datetime.now().strftime("%H:%M:%S")

        with open("attendance.csv", "a+", newline="\n") as f:
            f.seek(0)
            reader = csv.reader(f)
            rows = list(reader)

            filtered_rows = [row for row in rows if row and row[0] == str(student_id) and row[5] == current_date]

            if not filtered_rows:
                with open("attendance.csv", "a", newline="\n") as f:
                    writer = csv.writer(f)
                    writer.writerow([student_id, roll, name, department, current_time, current_date, "Present"])
                    print(f"Attendance marked for {name} ({roll}) - {department} on {current_date}")

    def face_recog(self):
        def draw_boundry(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=(50, 50), maxSize=(200, 200))
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                face_roi = gray_image[y:y+h, x:x+w]
                id, predict = clf.predict(face_roi)
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", port="3306", username="root", password="123", database="face_recognizer", ssl_disabled=True)
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id = %s", (id,))
                result = my_cursor.fetchone()
                conn.close()

                if result:
                    name, roll, dep = result

                    if confidence > 80:
                        cv2.putText(img, f"ID:{id}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll:{roll}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name:{name}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department:{dep}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(id, roll, name, dep)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundry(img, faceCascade, 1.1, 10, clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
