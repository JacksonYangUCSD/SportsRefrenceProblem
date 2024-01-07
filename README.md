# SportsRefrence Engineering Problem
Seeing that this is a matrix problem, the optimal way to solve it is the with a 2d array. I initilized a method ``create`` to make the matrix and to turn it into a string, which is step 1 through 3.
## Step 1
The first step for the problem is to collect the team names and setting up the 2d matrix. The column_width is for aesthetic purposes. The header row is created by one for loop and using ljust to ensure correct formatting. The 2d matrix is initialized by a nested for loop that created each cell with a length of `len(teams[1]) + 3`.
```py
teams = []
for team in dataset:
    teams.append(team)
    
# Finding the column width
column_width = len(teams[1]) + 3

# Creating the header row
header = "Tm".ljust(column_width)
for team in teams:
    header += team.ljust(column_width)

# Initialize the matrix to store win records
matrix = []
for i in range(len(teams)):
    row = []
    for j in range(len(teams)):
        row.append('')
matrix.append(row)
```
## Step 2
The second step was populating the 2d matrix by using a nested for loop and the method rjust. This section checks if team1 is against itself and if so it's replaced with a ``-``. If not then the amount of wins will be put in their respected cell.
```py
# Populate the matrix with win/lose records
for i in range(len(teams)):
    team1 = teams[i]
    for j in range(len(teams)):
        team2 = teams[j]
        if team1 == team2:
            matrix[i][j] = ' - '
        else:
            record = dataset[team1][team2]
            matrix[i][j] = str(record['W']).rjust(2)
```
## Step 3
The third step was creating the string version of the matrix. We first create the matrix without the header by a nested for loop. The second loop creates the whole row of the string and is combined to the matrix_str. After every row of the matrix is added to the string it is returend with the header.
```py
# Create the final string representation of the matrix
matrix_str = ""
for i in range(len(matrix)):
    row_str = teams[i].ljust(column_width)
    for cell in matrix[i]:
        row_str += cell.ljust(column_width)
    matrix_str += row_str + '\n'

return header + "\n" + matrix_str
```
## Step 4
The fourth step is reading the JSON file and printing it. This is done with import os and import json, where if the JSON file can be found in the folder it breaks the loop otherwise the loop keeps going until a valid JSON file is found. Then the program opens it and loads it to userdata and then goes back to the method create which was [steps 1-3]. The string is then put into variable table and printed.
```py
while True:
    data = input("Enter the JSON file name: ")
    if os.path.exists(data):
        break
    else:
        print("File not found. Please enter a valid file name.")

with open(data, 'r') as file:
    userdata = json.load(file)
table = create(userdata)
print(table)
```
