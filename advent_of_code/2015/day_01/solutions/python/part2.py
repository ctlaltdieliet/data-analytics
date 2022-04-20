#!/usr/bin/python
import sys
with open('../../input/part_1.txt') as f:
  lines=f.read()
  floorlevel=0
  counter=0;
  for x in lines:
    if x=='(':
      counter=counter+1
      floorlevel=floorlevel+1
    if x==')':
      counter=counter+1
      floorlevel=floorlevel-1
    if floorlevel==-1:
      print("After "+str(counter)+ " moves Santa has reached the basement the first time ")
      f.close()
      sys.exit()


