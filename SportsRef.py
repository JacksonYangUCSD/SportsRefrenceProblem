import json
import os

def create(dataset):
    teams = []
    for team in dataset:
        teams.append(team)
    
    # Finding the column widthtes
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

    # Populate the matrix with win records
    for i in range(len(teams)):
        team1 = teams[i]
        for j in range(len(teams)):
            team2 = teams[j]
            if team1 == team2:
                matrix[i][j] = ' - '
            else:
                record = dataset[team1][team2]
                matrix[i][j] = str(record['W']).rjust(2)

    # Create the final string representation of the matrix
    matrix_str = ""
    for i in range(len(matrix)):
        row_str = teams[i].ljust(column_width)
        for cell in matrix[i]:
            row_str += cell.ljust(column_width)
        matrix_str += row_str + '\n'

    return header + "\n" + matrix_str

# Read JSON data from a file
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
    

