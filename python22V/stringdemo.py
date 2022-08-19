# s1 = "hello"
# print(s1.capitalize())
# print(s1.casefold)
# print

database = [
"Blockchain A to Z Explained: Become a Blockchain Pro with 400+ Terms",
"Blockchain: Blueprint for a New Economy",
"Inside the machine","Rich dad poor dad",
"shiva trilogy",
"Core Python programming",
"The Psychology of Money",
"The Richest Man in Babylon"
]
database = [i.lower() for i in database]
qr = input("Enter the word to find the book")    
qr = qr.strip()
qr = qr.lower()
l2 = []
for i in database:
    if qr in i:
      l2.append(i)
    else:
        print("not found")



