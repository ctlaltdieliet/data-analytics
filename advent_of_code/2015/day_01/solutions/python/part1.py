#!/usr/bin/python
with open('../../input/part_1.txt') as f:
  lines=f.read()
  going_up=0;
  going_down=0;
  for x in lines:
      if x=='(':
          going_up=going_up+1
      if x==')':
          going_down=going_down-1
floor_level=going_up+going_down
print("Santa went "+str(going_up)+ "leves up and "+str(going_down)+" down. He is at floor level "+str(floor_level) )
f.close()