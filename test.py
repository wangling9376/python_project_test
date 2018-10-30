#!/usr/bin/python
sum = 0
for i in range(100):
	if(i%10):
		continue
	sum = sum + 1
print(sum)
