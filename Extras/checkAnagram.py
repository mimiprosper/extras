# function to check if two strings are anagram or not

text = ["hello", "some", "fred", "elbow", "below"]

if sorted(text[3]) == sorted(text[4]):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")


# def check(s1, s2):
     
#     # the sorted strings are checked
#     if(sorted(s1) == sorted(s2)):
#         print("The strings are anagrams.")
#     else:
#         print("The strings aren't anagrams.")        


# s1 = input("enter first word : ")
# s2 = input('enter second word : ')
#  check(s1, s2)
