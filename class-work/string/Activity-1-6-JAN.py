# string1 = "hello"
# string2 = "India"
# ans1 = string1 + " " + string2
# print(ans1, "\n")


# # print("writing 3 times \n ", (ans1 * 3))
# # printing 3 times by using for loop
# for i in range(3):
#     print(ans1, "\n")

# # slicing the string of ans1
# slicedAns1 = ans1[2:]
# # there are many diffrent steps to get differente type of sliced if string
# print(slicedAns1, "\n")

# take input name and age from user
name = input("Enter your Name : \n")
age = input("Enter your Age : \n")
age = int(age)
print("Hello {name} your age is {age} years old".format(name=name, age=age))
