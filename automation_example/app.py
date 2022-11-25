#example that automates updating spreadsheets.

#import open excel workbook, and name it xl for easier reference
import openpyxl as xl

#load the file
wb = xl.load_workbook('transactions.xlsx')
#load the sheet to work on
sheet = wb['Sheet1']

#load the cell we want to work in
cell = sheet['a1']
#alternatively
cell = sheet.cell(1,1)

print (cell.value)