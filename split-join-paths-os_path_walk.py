#!/usr/bin/env python

import fire
import os

def walk_path(parent_path):
    print(r"Checking: {parent_path})
    childs = os.listdir(parent_path) #1.0.
    
    for child in childs:
        child_path = os.path.join(parent_path, child) #2.0. 
        
        if os.path.isfile(child_path): #3.0.
        
last_access = os.path.getatime(child_path) #4.0.
        size = os.path.getsize(child_path) #5.0.
        print(f"File: {child_path")
        print(f"\tsize: {size}")
     elif os.path.isdir(child_path): #6.0.
          walk_path(child_path)
          
 if __name__ == '__main__':
    fire.Fire()
