a = input('Enter the numbers with Spaces in between: ')
a_list = a.split(' ')
new_list = []
for i in a_list:
	if(int(i)>0):
		new_list.append(i)
		print(i)
print(new_list)
