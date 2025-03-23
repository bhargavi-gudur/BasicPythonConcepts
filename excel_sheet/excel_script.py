from openpyxl import Workbook

# Step 1: Create a new workbook
workbook = Workbook()

# Step 2: Access the active worksheet
sheet = workbook.active

# Step 3: Add data to the sheet
sheet['A1'] = "Name"
sheet['B1'] = "Age"
sheet['A2'] = "Alice"
sheet['B2'] = 30

# Step 4: Save the workbook
workbook.save("example.xlsx")
