class HR:
   def __init__(self,name,surname,age,salary,languages,department):
       self.name=name
       self.surname=surname
       self.age=age
       self.salary=salary
       self.languages=languages
       self.department=department
   def menu(self):
       while True:
            
           process=input("""     
                    MENU
           ***********************
           1-Show Info
           2-Add Language
           3-Update Info
           4-Quit\n:~""")
                
           if process=="1":
               worker1.show_info()
               
           if process=="2":
               language=input("Enter the Language:")
               worker1.add_language(language)
                
           if process=="3":
               worker1.update()
           if process=="4":
               break
           
   def extra(self):
       amount=int(input("Amount of Addition to Salary:~"))
       self.salary+=amount
       
   def show_info(self):
       print(f"Name:{self.name}\nSurname:{self.surname}\nAge:{self.age}\nSalary:{self.salary} EU\nLanguages:{self.languages}\nDepartment:{self.department}")
            #print("Name:{}\nSurname:{}\nAge:{}\n".format(self.name,self.surname,self.age))
    
   def add_language(self,language):
       self.languages.append(language)
    
   def update(self):
       import time
       while True:
        
            criteria=input("""       
                    MENU
            ********************
            1-Name
            2-Surname
            3-Age
            4-Department
            5-Languages
            6-Quit\n:~""")
        
            if criteria=="6":
                print("It is exiting")
                time.sleep(2)
                break
                           
            if criteria=="1":
                name=input("Enter Name:")
                self.name =name
               
            if criteria=="2":
                surname=input("Enter Surname:")
                self.surname =surname
               
            if criteria=="3":
                age=input("New age:")
                self.age =age

            if criteria=="4":
                department=input("Change the Department:")
                self.department =department
            if criteria=="5":
                languages=input("Update Languages:")
                self.languages =languages
            if criteria=="6":
                  break
                
class Management(HR):
    
   def __init__(self,name,surname,age,salary,languages,department,number_of_worker):
       
       super().__init__(name,surname,age,salary,languages,department)

       self.number_of_worker=number_of_worker
    
   def menu(self):
       while True:
             
           process=input("""
                     MENU
            ***********************
            1-Show Info
            2-Show Worker Info
            3-Add Language
            4-Update Info
            5-Salary Addition
            6-Quit\n:~""")
                 
           if process=="1":
                manager.show_info()
           if process=="2":
                worker1.show_info()

           if process=="3":
                language=input("Enter the Language:")
                worker1.add_language(language)
                 
           if process=="4":
                worker1.update()
           if process=="5":
               worker1.extra()
           if process=="6":
              break
    

        
worker1=HR("Erkan","Öktem",44,3500,["English","Turkisch","German"],"IT") #arbeiter1 =self

worker2=HR("Hans","Edelmann",35,4000,["German","English"],"Human Resources") #arbeiter2=self

manager=Management("Elona","Musk",43,10000,["English"],"CEO",11)

#arbeiter1.show_info()
#arbeiter2.show_info()

#arbeiter1.update()

#Arbeiter.show_info(arbeiter1) #another way

#arbeiter1.extra(500)
#arbeiter2.add_language("Korean")

#arbeiter1.show_info()
#arbeiter2.show_info()

while True:
    modul=input("""                ****************************************
                WELCOME TO INFORMATION MANAGEMENT CENTER
                ****************************************\n
                                 MENU\n
                1-HR
                2-Managemet\n
                *******************************************\n:~""")
    if modul=="1":
        worker1.menu()
    if modul=="2":
        manager.menu()