grid = []
size = range(6)

for i in size:
  row = []
  for j in size:
    row.append("A")
  grid.append(row)

for i in grid:
  emptyRow = ''
  for j in i:
    emptyRow = emptyRow + j + ' '
  print(emptyRow)
