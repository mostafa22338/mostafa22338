import json 
class Course:
    def __init__(self,code,name,number_of_hours,iscore):
        self.code=code
        self.name=name
        self.number_of_hours=number_of_hours
        self.iscore=iscore
    def __str__(self):
        return f"Course code: {self.code} , Course name: {self.name} , Number of hours: {self.number_of_hours} , iscore: {self.iscore}"




class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.enrolled_courses={}

    def enroll_course(self,course):
        if course.code in self.enrolled_courses:
            raise Exception(f"student already enrolled in course {course.name}")
        else : 
            self.enrolled_courses[course.code]=course
    def drop_course(self,course_code):
        if course_code in self.enrolled_courses:
            del self.enrolled_courses[course_code]
        else:
            raise Exception(f"course {course_code} not found ") 
    def list_course(self):
        return list(self.enrolled_courses.values())
    



             

class System:
    def __init__(self) :
        self.courses={}
        self.students={}
    def add_course(self,course_code,course_name,number_of_hours,iscore):
        if course_code in self.courses:
            raise Exception(f" course with code {course_code} already exists")
        else:
            self.courses[course_code]=Course(course_code,course_name,number_of_hours,iscore)

    def enroll_student(self,std_id,std_name,course_code):
        if std_id not in self.students:
            self.students[std_id]=Student(std_id,std_name)
        student=self.students[std_id]
        if course_code not in self.courses:
            raise Exception(f"course does not exist")
        
        student.enroll_course(self.courses[course_code])

    def drop_course(self,course_code,std_id):
        if std_id not in self.students:
            raise Exception(f"student not found")
        else: 
            student=self.students[std_id]
            student.drop_course(course_code)

    def list_courses(self,stud_id):
        if stud_id not in self.students:
             raise Exception(f"student not found")
        else: 
            return self.students[stud_id].list_course()
        
    def save_course_catalog(self,filename):
        courses_dc={}
        for code,course in self.courses.items():
            courses_dc[code]=vars(course)
        with open(filename,"w") as file:
            json.dump(courses_dc,file)

    def load_course_catalog(self,filename):
        with open(filename,"r") as file:
            data=json.load(file)
            for code,course in data.items():
                self.courses[code]=Course(course['code'],course['name'],course['number_of_hours'],course['iscore'])

system=System()
while (True):
    print("1. add course \n 2.enroll student in course \n 3.drop course for student \n 4.list all student course \n 5.save course catalogue \n 6.load course catalogue \n 7.exit")
    n=int(input("enter your choice"))
    if(n==1):
        a=input("enter course code: ")
        b=input("enter course name: ")
        c=int(input("enter number of hours: "))
        d=input("enter if its core or not:")
        system.add_course(a,b,c,d)
        
    elif(n==2):
        e=input("enter student name: ")
        f=input("enter student id: ")
        j=input("enter course code: ")
        system.enroll_student(f,e,j)
        
    elif(n==3):
        m=input("enter course code: ")
        l=input("enter student id: ")
        system.drop_course(m,l)
       
    elif(n==4):
        u=input("enter student id: ")
        courses=system.list_courses(u)
        for course in courses:
            print(course)
        
    elif(n==5):
        i=input("enter filename: ")
        system.save_course_catalog(i)
        
    elif(n==6):
        q=input("enter filename: ")
        system.load_course_catalog(q)
        
    elif(n==7):
        break












        




  
        
    
        





