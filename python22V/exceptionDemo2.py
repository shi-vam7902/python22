# From Vinit Prajapati to Everyone 03:42 PM
# Write a program to make a new string with the word "the" deleted in the given string.
# eg:
# input string: This is the lion in the cage.
# output: This is lion in cage.

print("Enter the String: ")
text = input()

print("Enter a Word to Delete: ")
word = input()

text = text.replace(word, "")

print()
print(text)