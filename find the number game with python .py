#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def find_num(x=10):
    """this function for user to guess number
    """
    random_num = random.randint(1,x)
    print(f"I think a number from 1 to {x}. Can you try to find it?", end="")
    attempts = 0
    while True:
        attempts += 1
        guess = int(input(">>>"))
        if guess<random_num:
            print("Wrong. The number I think is bigger. Try again please:", end="")
        elif guess>random_num:
            print("Wrong. The number I think is smaller. Try again please:", end="")
        else:
            break
              
    print(f"Congrats. You found after {attempts} attempts!")
    return attempts


# In[2]:


find_num()


# In[3]:


def find_num_pc(x=10):
    input(f"Think about any number from 1 to {x} and press any button. I will find the number.")
    bottom = 1
    top = x
    attempts = 0
    while True:
        attempts += 1
        if bottom != top:
            guess = random.randint(bottom,top)
        else:
            guess = top
        answer = input(f"You think the number {guess}: right (r),"
                      f"I think bigger number (+), or I think smaller number (-)".lower())
        if answer == "-":
            top = guess - 1
        elif answer == "+":
            bottom = guess + 1
        else:
            break
    print(f"I found after {attempts} attempts!")
    return attempts


# In[4]:


find_num_pc()


# In[6]:


def play(x=10):
    again = True
    while again:
        attempts_user = find_num(x)
        attempts_pc = find_num_pc(x)
                
        if attempts_user>attempts_pc:
            print(f"I found after {attempts_pc} attempts and won!")
        elif attempts_user<attempts_pc:
            print(f"You found after {attempts_user} attempts and won!")
        else:
            print("Draw!")
        again = int(input("Play again? yes(1)/no(0):"))
              
play()


# In[ ]:




