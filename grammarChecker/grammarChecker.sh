#!/bin/bash
#입력:찾는 단어
#색상 export GREP_OPTIONS='--color=auto'
#     export GREP_OPTIONS='--color=always' GREP_COLOR='1;31' 

while true
do
 clear
echo "[GRAMMAR CHECKER] Enter the word you want to check."  
read word

grep -n --color=always "$word" grammar.txt

echo "[GRAMMAR CHECKER] Press '/' to add the grammar."
read check

if [ "$check" == "/" ]; then 
 echo "[GRAMMAR CHECKER] Enter the new grammar."
 read reword
 echo "$word / $reword" >> grammar.txt
 cat grammar.txt
fi

echo "----------------------------------"

done
