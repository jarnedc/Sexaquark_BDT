#!/bin/bash

#dirName = ./LoopCut20Var2016

mkdir ./LoopCut20Var2016_10062019
for i in {0..19}
do
   #mkdir ./LoopCut20Var2016/$i
   python BDT_2016_Loop.py $i LoopCut20Var2016_10062019
done
