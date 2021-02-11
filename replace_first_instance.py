#!/usr/bin/env python3
s = input("please type in a string :\n") 
position = s[0] #here I have set the index postion to zero this means we will be referencing the first char of
				#the string given as input by the user. 
replace_char = s[1:].replace(position, "*") #simple operation performing the task
											#setting the new char as replace_char "*" and telling it to 
											#replace the first and all occurances of index [0] that is the 	
											#first position of a charactor in a string . 
print(position+replace_char)	
