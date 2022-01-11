 #1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())
    # Answer return 5 

#2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
    #Answer undefined, number of days... not definied 

# #3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())
    #Answer 5 first return ends function


# #4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())
    #Answer 5 


# #5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x) #no value for x 
    #Answer 5

# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))
    #Answer (3,5)

# #7
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5)) # concatenate = a+b=ab or 1+2=12 
    #Answer 7


# #8
# def number_of_oceans_or_fingers_or_continents():
    # b = 100 #num of oceans ... was already defined in function , included in answer 
    # print(b)
    # if b < 10:
    #     return 5
    # else:
    #     return 10
    # return 7
# print(number_of_oceans_or_fingers_or_continents())
    #Answer 10


# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
    #3rd line chances to (7) +(14)=21 
    #Answer 7,14,14 // TOTAL ANSWER IS 7,14,21

# #10
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))
    #Answer return 8 

# #11
# b = 500
# print(b)#500
# def foobar():
#     b = 300
#     print(b)
# print(b) # goes back to 500 because this going down does not belong to def foobar 
# foobar()#300
# print(b)#500
    #answer 500, 300, err,err,err // correct ans: 500,500,300,500


# #12
# b = 500
# print(b) #500
# def foobar(): #only def for foobar 
#     b = 300
#     print(b) 
# print(b)#500 
# foobar()#300 
# print(b)#500 
 #Ans 500,500,300,500 

# #13
# b = 500
# print(b) #500
# def foobar():
#     b = 300
#     print(b) #300 
#     return b #300 
# print(b)#500
# b=foobar() #300 //new variable that is being definied effecting line below 
# print(b)#300  


# #14
# def foo():
#     print(1) #1
#     bar() # def bar is 3 
#     print(2) #2
# def bar():
#     print(3)
# foo() #(1,2)3? // correct ans (1,3,2)


# #15
# def foo():
#     print(1) #1
#     x = bar()#3
#     print(x) #x 
#     return 10
# def bar():
#     print(3) #3
#     return 5 # return overshadows print command
# y = foo()
# print(y)# ans 1,3,10,3,5
