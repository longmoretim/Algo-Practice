#Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only.

#Input: s = "Hello World"
#Output: 5
#Explanation: The last word is "World" with length 5.

def length(snt):
    word = snt.split()
    #this is a check to see if there is a period could add check for all punctuation or use regex
    if list(word[-1])[-1] == ".":
        return len(word[-1]) - 1
    else:
        return len(word[-1])

print(length("Hello World."))
print(length("Hello World"))