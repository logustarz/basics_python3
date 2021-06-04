import xlrd
  
loc = ("C:\system") #path for reading the file
logu = xlrs.open_workbook(loc)
sheet = logu.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(sheet.ncols):
	for j in range(sheet.nrows):
		print(sheet.cell_value(j,i))
