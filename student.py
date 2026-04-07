#write a user defined function that returns true if student marks is less than 30. 
# The list is passed as an argument.
#use the above function with filter to extract the ids of eligible students
#using lambda function with map,create a new list with student id and updated marks,where students get
#a grace marks of 5, if their marks is below 30.
#student=[(name,id,marks)........] for 5 students
students=[('s',34322,56),('a',343,20),('b',322,22),('c',34,21),('d',122,12)]
def iseligible(student):
    return student[2]<30

eligible_students=list(filter(iseligible,students))
eligible_ids=[student[1] for student in eligible_students]
eligible_names=[student[0] for student in eligible_students]
print(eligible_ids)
print(eligible_names)
new=list(map(lambda x:(x[0],x[1],x[2]+5) if x[2]<30 else x,students))
print(new)
