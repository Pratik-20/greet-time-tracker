import gspread

# Load credentials from a JSON file (replace with your own file path)
gc = gspread.service_account(filename="github-actions-py1-b1b85f37d6c1.json")

# Open the Google Sheet named "Github Action"
wks = gc.open("Github Action").sheet1

# Read the existing data from the first column (column A)
existing_data = wks.col_values(1)

# Add "Helloworld" to the next row
next_row = len(existing_data) + 1
wks.update(f'A{next_row}', [["Helloworld"]])

# Print the updated data
print(f"'Helloworld' added to row {next_row} in column A.")
