# Create a function that given a string as a parameter of upper/lower case letters and empty space characters (“ “), return the length of the last word. Meaning, the word that appears far most to the right if we loop through the words.
# Example Input: “Hello World”
# Example Output: 5
# Example Input: “We’re learning about a great full-stack web application called Flask”
# Example Output: 5

str1 = "Hello World"
str2 = "We’re learning about a great full-stack web application called Flask"

# def lenOfLastWord(string):
#     last = string.split()
#     print(len(last[-1]))

def lastWord(string):
    count = 0
    while string[len(string)-1-count] != ' ':
        count +=1
    return count
    
lastWord(str1)