#A little script to test functions
from __future__ import division #Import division module from python 3
def hello(name): #define function hello with argument "name"
    print("Hello "+name) #print Hello + specified argument

me='David' #define variable "David"
hello(me) #run above specified function, giving the variable "me" as argument

def get_at_content(dna):
'''script that calculates AT-content of the argument "DNA" by calculating the length, counting the occurrence of A and T in the variable,
and then calculating the ratio of AT relative to the length. Also see files at_content2.py and at_content3_py in the same repository'''
        length = len(dna)
        a_count = dna.count('A')
        t_count = dna.count('T')
        at_content = (a_count + t_count) / length
        return at_content
