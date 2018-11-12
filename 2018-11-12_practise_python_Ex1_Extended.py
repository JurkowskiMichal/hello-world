
#Exercise 1 getting user age and printing at what year will the user turn 100 
name = input("Please enter Your name ")
age = int(input("Please enter Your age "))
print("Your name is %s and You are %s years old"%(name,age))
turnhundred = 100 - age
year = 2018 + turnhundred
print("You will turn 100 in %s" % year)

#Exercise 1 extension 1 & 2  printing x messages using multiply and "for" loop
message= "You will turn 100 in %s" % year
multimessage = int(input("Please enter number and I will print that many messages "))
print("One way of printing everything together in one line")
print(multimessage * message)
print("Another clearer way of printing the same text: ")
for x in range (0, multimessage):
    print (message)
