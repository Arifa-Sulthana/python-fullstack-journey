# String Challenges
# # # Puzzle 1: FizzBuzz 
# # # ip=int(input("Enter a number: "))
# # # for i in range(1,101):
# # #     if(i%3!= 0 and i%5!=0):
# # #         print(i, " Sorry!")
# # #     elif(i%2==0 and i%5==0):
# # #         print(i, " FizzBuzz")
# # #     elif(i%3==0):
# # #         print(i, " Fizz")
# # #     elif(i%5==0):
# # #         print(i, "Buzz")
    


# # # ip=int(input("Enter a number: "))

# # # if(ip%3 != 0 and ip%5 !=0):
# # #     print("Sorry!")
# # # elif(ip%2==0 and ip%5==0):
# # #     print("FizzBuzz")
# # # elif(ip%3==0):
# # #     print(ip,"Fizz")
# # # elif(ip%5==0):
# # #     print("Buzz")




# # # Puzzle 2: Palindrome Checker
# # # st=input("Enter the word: ")
# # # st1 = "".join(reversed(st)S)
# # # if(st==st1):
# # #     print(f"{st} is a palindrome")
# # # else:
# # #     print("Sorry!!")
# # # st1=""
# # # for ch in st:
# # #     st1 =ch+st1

# # # print(st1)

# # for i in range(0, 101):
# #     output = ""
# #     if i % 3 == 0: output += "Fizz"
# #     if i % 5 == 0: output += "Buzz"
# #     if(output==""):
# #         print(i)
# #     else:
# #         print(output)
# #     # print(output or i)

# print("*")
# i=5
# print(i)
# for i in range(5,0,-1):
#     for j in range(1,i):
#         print(" ", end=" ")
#     for k in range(i,6):
#         print("*", end=" ")
#     print()
# i=1
# for i in range(6,1,-1):
#     for j in range(1,i):
#         print("*", end=" ")
#     print()


# i=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()


# i=1
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ", end=" ")
#     for k in range(6-i,6):
#         print("*", end=" ")
#     print()


# i=1
# for i in range(1,6):
    # for j in range(6-i):
    #     print(" ", end="")
    # for k in range(6-i,6):
    #     print("*", end=" ")
    # print()


# i=1
# for i in range(1,10):
#     if(i%2 != 0):
#         for j in range(10-i):
#             print(" ", end="")
#         for k in range(10-i, 10):
#             print("*", end=" ")
#         print()



# i=10
# for i in range(10,0,-1):
#     if(i%2 != 0):
#         for j in range(10-i):
#             print(" ", end="")
#         for k in range(10-i, 10):
#             print("*", end=" ")
#         print()


# i=1
# for i in range(1,6):
#     for j in range(i):
#         print(i, end="")
#     print()



# books = ["Harry Potter", "The Hobbit", "Pride and Prejudice", "Harry Potter", "The Great Gatsby"]
# books.insert(2, "To Kill a Mockingbird")
# books.remove("The Great Gatsby")
# if books.count("Harry Potter") > 1:
#     books.remove("Harry Potter")
# books1=books[: :-1]
# print(books, books1)




# library_books = ["Harry Potter", "The Hobbit", "1984", "The Alchemist", "Sapiens"]
# library_books.insert(2, "Atomic Habits")
# library_books.remove("1984")
# if "Harry Potter" in library_books:
#     library_books.remove("Harry Potter")
# reversed_library = library_books[: : -1]
# print(library_books)
# print(reversed_library)



# library_books = ["Harry potter", "The Alchemist", "Sapiens", "The Hobbit"]
# n=library_books.index("Sapiens")
# library_books.insert(n+1, "Rich Dad Poor Dad")
# if "The Alchemist" in library_books:
#     library_books.remove("The Alchemist")
# if "The Hobbit" in library_books:
#     library_books[library_books.index("The Hobbit")]= "The Lord of the Rings"
# lb=library_books[: : -1]
# print(library_books)
# print(lb)


# currently_reading = ["Atomic Habits", "Deep Work"]
# wishlist = ["The Alchemist", "Sapiens", "Rich Dad Poor Dad"]
# if "Sapiens" in wishlist:
#     wishlist.remove("Sapiens")
# currently_reading.append("Sapiens")


# currently_reading = ["Atomic Habits", "Deep Work", "Ikigai"]
# wishlist = ["The Alchemist", "Sapiens", "Rich Dad Poor Dad", "Ikigai"]
# wishlist.remove("Ikigai")
# currently_reading.insert(currently_reading.index("Atomic Habits")+1, "The Psychology of Money")
# library_shelf=currently_reading+wishlist
# print(currently_reading)
# print(wishlist)
# print(library_shelf)



# Available_products = ["Shoes", "Shirt", "Watch", "Sunglasses", "Bag"]
# Cart = []
# wishlist=["Perfume", "Cap"]
# Cart=Cart+["Shoes", "Watch"]
# if "Shoes" in Cart:
#     Cart.insert(Cart.index("Shoes"), "Sunglasses")
#     Cart.remove("Shoes")
# Cart.insert(Cart.index("Watch")-1, "Bag")
# full_cart=Cart+wishlist
# print(Cart)
# print(wishlist)
# print(full_cart)



# locations = [("Paris", 48.8566, 2.3522),
#              ("Tokyo", 35.6895, 139.6917),
#              ("Delhi", 28.6139, 77.2090)]
# ll=int(len(locations))
# for i in range(ll):
#     for j in range(ll):
#         if type(locations[i][j])==str:
#           print(locations[i][j])



# student_data = ("Anya", 23, "IT", 8.7, "Placed")
# print(student_data[0:2])
# print(student_data[2:])
# print(student_data[-1])

# students = [
#     ("Anya", 23, "IT", 8.7, "Placed"),
#     ("Raj", 22, "ECE", 9.1, "Not Placed"),
#     ("Meera", 24, "CSE", 8.9, "Placed")
# ]

# for i,j,k,l,m in students:
#     if(m =="Placed"):
#         print(i)



students = [
    ("Anya", 23, "IT", 8.7, "Placed"),
    ("Raj", 22, "ECE", 9.1, "Not Placed"),
    ("Meera", 24, "CSE", 8.9, "Placed"),
    ("Kabir", 23, "EEE", 7.9, "Not Placed")
]

# for i,j,k,l,m in students:
#     if m=="Not Placed":
#         print(f"{i} is not placed")
#     if l>8.5:
#         print(f"{i}'s GPA is greater than 8.5")
# students = [
#     ("Anya", 23, "IT", 8.7, "Placed"),
#     ("Raj", 22, "ECE", 9.1, "Not Placed"),
#     ("Meera", 24, "CSE", 8.9, "Placed"),
#     ("Kabir", 23, "EEE", 7.9, "Not Placed")
# ]
# c=0
# print(students[2:])
# for i,j,k,l,m in students:
#     # print()
#     print(i, k)
#     if i != "null":
#         c+=1
# print(c)
# print(students[2:])
# for f in range(len(students)):
#     print(students[f][0], students[f][2])
#     if students[f][0] != "null":
#         c+=1
# print(c)



# colors = ("Red", "Green", "Blue", "Yellow", "Purple", "Pink")
# # Fill in the blank to print: ("Pink", "Yellow", "Green")
# print(colors[: :-2])

# brands = ("Nike", "Adidas", "Puma", "Reebok", "Fila", "Converse")
# # Fill in the blank to print: ("Converse", "Fila", "Reebok")
# print(brands[-1:-4:-1])


# devices = ("Laptop", "Tablet", "Smartphone", "Smartwatch", "Camera", "Speaker")
# d1=devices[2:-1]
# print(d1)
# print(d1[::-1])


# weekly_sales = ("Laptop", "Tablet", "Smartphone", "Smartwatch", "Camera", "Speaker", "Camera", "Laptop")
# w1=weekly_sales[5: ]
# print(w1[::-1])

# weekly_sales = ("Laptop", "Tablet", "Smartphone", "Smartwatch", "Camera", "Speaker", "Camera", "Laptop")
# c=[]
# for i in weekly_sales:
#     w1=weekly_sales.count(i)
#     if w1>1:
#         if c.__contains__(i):
#             continue
#         else:
#             c.append(i)
#             print(weekly_sales.count(i),i)

        # print(f"{i} is sold more than once!!!")
# print(weekly_sales.count(i))


# from collections import Counter
# weekly_sales = ("Laptop", "Tablet", "Smartphone", "Smartwatch", "Camera", "Speaker", "Camera", "Laptop")
# li=[]
# for i in range(len(weekly_sales)):
#     li.append(weekly_sales[i])
# c=Counter(li)
# for key, value in c.items():
#     if value>1:
#         print(key)


# from collections import Counter
# weekly_sales = ("Laptop", "Tablet", "Smartphone", "Smartwatch", "Camera", "Speaker", "Camera", "Laptop")
# c=Counter(weekly_sales)

# for item, count in c.items():
#     if count>1:
#         print(f"{item}: {count} times")


# from collections import Counter
# feedback_scores = (5, 4, 5, 3, 4, 5, 2, 1, 3, 5, 4, 2)
# c=Counter(feedback_scores)
# li=[]
# for item, count in sorted(c.items(), reverse=True):
#     if count>1:
#         print(f"{item}: {count} times")


# from collections import Counter
# visits = ("Paris", "London", "Paris", "Tokyo", "Berlin", "London")
# c=Counter(visits)
# li=[]
# for city, count in c.items():
#     if count<=1 or city not in li:
#         li.append(city)
#     if city == "Tokyo":
#         print("Yes Traveler visited Tokoyo")
# print(f"The distinct cities are: {li}")
# print(f"The traveler visited {len(li)} cities")


# from collections import Counter
# travel_log = ("Delhi", "Paris", "New York", "Delhi", "London", "Paris", "Berlin", "Rome", "Delhi")
# c=Counter(sorted(travel_log),reversed=False)
# distinct_cities=[set(travel_log)]
# print(distinct_cities)
# highest_visited_count=max(c.values())
# cities_list=[]
# for city, count in c.items():
#     if city=="Delhi":
#         print(count)
#     if count>1:
#         cities_list.append(city)
#     if count==highest_visited_count:
#         print(city)
# print(cities_list)


# text = "Python makes you powerful"
# li=text.split(" ")
# print(text)
# li.reverse()
# tx= ' '.join(li)
# print(tx)


# text = "Apple is an amazing fruit that everyone enjoys"
# tx=text
# li=tx.split(" ")
# temp=" "
# vowels=['a','A','e','E', 'i','I','o','O','u','U']
# for i in li:
#     for j in range(len(li)):
#         if li[j]==i:
#             break
#     if vowels.__contains__(i[0]):
#         li[j]= i[::-1]
# output=' '.join(li)
# print(output)



# from collections import Counter
# devices = ("Laptop", "Tablet", "Phone", "Laptop", "Tablet", "Camera", "Phone", "Camera")
# c=Counter(devices)
# print(c.items())
# for key, value in c.items():
#     if value>1:
#         print(key)


# log = "[INFO] 2025-05-22 10:45:01 User: john_doe123 logged in."
# li=log.split(" ")
# print(li)
# username=li[4]
# date=li[1]
# action=li[-2]+" "+li[-1].strip(".")
# print(f"Username = {username}, Date = {date}, Action = {action}")


# text = "PYTHONMASTER"
# print(text[::-2])
# print(text[::-1])


# sentence = "Learning Python is super fun and rewarding"
# li=sentence.split(" ")
# temp=[]
# for i in reversed(range(len(li))):
#     if i>=1 and i<6:
#         li.pop(i)
# for i in li:
#     i=i[::-1]
#     temp.append(i)
# txt='-'.join(temp)
# print(txt)

# msg = "automation"
# print(msg[::2]) 

# txt = "powerful"
# mid = len(txt) // 2
# print(txt[mid-1:mid+2])


# log = "ERROR 2025-05-22 14:33:58 - Disk space low"
# words=log.split(" ")
# Date=words[1]
# Time=words[2]
# Message=' '.join(words[4: ])
# print(f"{Date}, {Time}, {Message}")
