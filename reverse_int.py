logu = 54321
res = 0
while(logu > 0):
	a = logu % 10
	res = res * 10 + a
	logu = logu // 10
print(res)
