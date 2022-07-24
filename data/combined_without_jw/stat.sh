#!/usr/bin/env python

wc -l $1 >> $2
# echo -e "\n">>$2
wc -w $1 >> $2
python indic_tokenize.py $1 $3 $4

wc -w $3 >> $2

tr ' ' '\n' < $1 | sort | uniq -c | wc -l >> $2



