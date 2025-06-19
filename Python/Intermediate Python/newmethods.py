
#walrus 
n: int = 0 #type def in python
while (n := n + 1) < 10:
    print(n)
#output: 1 2 3 4 5 6 7 8 9

def add(a:int,b:int)->int:
    return a + b

# The walrus operator is a new operator in Python 3.8. It is represented by :=. It is also known as the assignment expression operator. It is used to assign values to variables as part of a larger expression. It is a way to assign a value to a variable and return that value at the same time.

from typing import List,Dict,Tuple,Union
numbers  : List[int] = [1,2,3,4,5]
Scores : Dict[str,int] = {'A':1,'B':2,'C':3}
names : Tuple[str,str,str] = ('A','B','C')
identifier : Union[str,int] = 'A123'


#2 merge two dictionaries
def merge_dict(dict1,dict2):
    return dict1.update(dict2)

def merge_dict(dict1,dict2):
    return dict1 | dict2
