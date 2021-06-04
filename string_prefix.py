logu_strlist = ['logu','logan','loganathan','lokesh']

res = ""
prefix = logu_strlist[0]
  
for string in logu_strlist[1:]:
	while string[:len(prefix)] != prefix and prefix:
		prefix = prefix[:len(prefix)-1]
res = prefix      
if not prefix:
	print("-1")
else:
  print(str(res))
