
#players=list(("Sancho","dembele","benzema"))
#print(players)
#players[0]="kane"
#print(players)
#players.append("mane")
#print(players)
#student=["lucy","ashley","bob"]
#student.remove("bob")
#print(student)
#student.clear()
#print(student)
#students=("lucy","ashley","bob")
#print(students)
#students=list(students)
#students.append("john")
#students=tuple(students)
#print(students)
#DICTIONARY
#class_schedule={
    #'MIT':'morning',
    #'python':'mid_morning',
    #'php':'evening'
#}
#print(class_schedule)
#print(class_schedule['python'])
#print(class_schedule.get('python'))
#print(class_schedule.keys())
#print(class_schedule.items())
#class_schedule['python']='night'
#class_schedule.update({'php':'mid_morning'})
#class_schedule['html']='early'
#print(class_schedule)
#del class_schedule['html']
#class_schedule.popitem()
#class_schedule.clear()
#print(class_schedule)
#NESTED DICTIONARY
#available_courses={
    #'MIT':{
        #'frontend':'html',
        #'backend':'javascript'
    #},
    #'python':{
        #'frontend':'css',
        #'backend':'python'
    #},
    #'cybersecurity':{
     #   'frontend':'javascript',
      #  'backend':'java'
    #},

#}
#print(available_courses)
#ASSIGNMENT
#lists

#name= ['Tracey','Elvis','Joseph','John','James']
#age=['21','20','22','19','23']
#gender=['female','male','male','male','male']
#students = [['Tracey','21','female'],['Elvis','20','male'],['Joseph','22','male'],['John','19','male'],['James','23','male']]
#print(students)
#tuples
#name=('Tracey','Elvis','Joseph','John','James')
#age=('21','20','22','19','23')
#gender=('female','male','male','male','male')
#students=(('Tracey','21','female'),('Elvis','20','male'),('Joseph','22','male'),('John','19','male'),('James','23','male'))
#print(students)
#nested dictionary
#python_students={
 #   'student_1':{
  #      'name':'Tracey',
   #     'age':'21',
    #    'gender':'female'

    #},
    #'student_2':{
     #   'name':'Elvis',
      #  'age':'20',
       # 'gender':'male'

    #},
    #'student_3':{
    #    'name':'Joseph',
     #   'age':'22',
      #  'gender':'male'

    #},
    #'student_4':{
     #   'name':'John',
      #  'age':'19',
       # 'gender':'male'

    #},
    #'student_5':{
     #   'name':'James',
      #  'age':'23',
       # 'gender':'male'

    #},

#}
#print(python_students)
#grade=int(input('Enter your grade: '))
#if grade <=99:
 #   print('A')
#elif grade<=80:
 #   print('B')
#elif grade<=60:
 #   print('C')  
#elif grade<=50      
#else:
#    print('Invalid ')   
#amount=int(input('enter your price: '))
#if amount>=100000:
 #   print('Gold package')
#elif amount >=80000 :
 #   print('Bronze package')  
#elif amount >= 50000:
 #   print('silver package') 
#elif amount< 50000:
 #   print('Not qualified for any package')  

#number=int(input('enter number: '))
#if number % 2==0:
 #   print("this is an even number")
#else:
 #   print('this is an odd number')    
# FOR LOOPS
#songs=['kilometer','for my hand','wild dreams']
#for x in songs:
 #   print(x)

 #RANGE(start,stop,step)
#for i in range(10,100,10):
 #   print(i)
#for i in range(11,20):
 #   print(i)
#for i in range(7):
   # print(i) 
#n = 2
#for i in range(11):
   # print(n*i)
#for i in range(1,11,1):
 #   product= n*i
  #  print(product)
   # if product==8:
    #    break
#songs=['kilometer','for my hand','wild dreams']
#for x in songs:
 #   print(x)  
  #  if x=='for my hand':
   #     break          
#WHILE LOOPS
#i=0
#while i<5:
 #   print(i)
  #  i+=1
#i=0
#while i<21:
 #   print(i)
  #  i+=1 
   # if i==15:
    #    break
#number=int(input('Enter a number'))
#while number>0 :
 #   square= number*number
  #  print(square)
   # break
    
 #FUNCTIONS
#import random 
#name=input('What is your name?')  
#print("hello"+name)
#print('welcome to the guessing game')
#def guess(x):
    #random_number= random.randint(1,x)
   # guess_integer=0

 #   while random_number!=guess_integer:
  #      guess_integer=int(input("Guess between 1 and "+str(x)+"?:"))
 #       if guess_integer>random_number:
  #          print('Too high')
  #      elif guess_integer<random_number:
   #         print('Too low')  
    #    else:
    #        print('correct')     
#guess(10)  
#def Replay():
 #   replay=input('Do you want to replay the game? ')  
  #  while replay=="yes":
   #     replay=input("Do you want to replay the game? ")  
    #    if replay=="yes":
     #       guess(10)
      #  else:
       #     print('Goodbye!!Thankyou for your time')           
#Replay()

#def letmeguess(x):
    #low=0
    #high=x
    #feedback =""
    #while feedback!='correct'and low!=high:
     #   guess= random.randint(low,high)
      #  feedback=input(f"Is my number{guess}? (high/correct/low)".lower())
       # if feedback=='high':
        #    high=guess -1
        #elif feedback=='low': 
          #  low= guess+1
    #print('Yay! I guessed your number!')           
#name=input('what is your name? ')
#print('hello '+name)
#number=int(input('write a number '))
#if number % 2==0:
  #  print('this is an even number')
#elif number % 2!=0:
 #   print('this is an odd number')

#number=int(input('Write a number ')) 
#def checknumber():
 #   if number % 2==0:
  #      print('this is an even number')
   ## elif number % 2!=0:
    #    print('this is an odd number')  
#checknumber()          

#marks=[1,2,3,4,5,6,7]
#for i in marks:
 #   print(i/2)
#marks=[1,2,3,4,5,6,7]
#def add(x):
 #   marks.append(x)
  #  print(marks)
   
#add(8)  
#marks=[1,2,3,4,5,6,7] 
#for i in marks:
 #   if i==5:
  #      print(i)
#marks=[1,2,3,4,5,6,7]
#marks.reverse()

#print(marks)
#print(marks[-1:-7])
student={
    'name':'Tracey',
    'age':'21',
    'gender':'female'
}
#print(student)
student['age']='22'
print(student)
print(student.get('name'))
if 'female' in student.values():
    print('it is present')
else:
    print('it is absent')    

