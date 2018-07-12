"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
 
"""

import os
import sys

def main():
    words = ["gin", "zen", "gig", "msg"]
    dict = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",
            'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",
            'm':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",
            's':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",
            'y':"-.--",'z':"--.."}

    arr = []
    tmp = 0
    ask = ""
    for i in range(len(words)):
        letters = words[i]
        list(letters)
        for j in range(len(letters)):
            ask += (dict[letters[j]])
        if ask not in arr:
            tmp += 1
        arr.append(ask)
        ask = ""
        
    print(arr,tmp)

if __name__ == '__main__':
    main()