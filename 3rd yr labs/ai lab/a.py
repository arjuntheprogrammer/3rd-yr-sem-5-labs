"""
a=[11,12,13,14,15,16]
for count, item in enumerate(a, start=0):   # default is zero
    print(item, count)
    #print `index`+" "+	`j`
 
for i in xrange(3):
    a.append([])
    for j in xrange(3):
            a[i].append(i+j)



# Create a list.  =>for 2d array
elements = []

# Append empty lists in first two indexes.
elements.append([])
elements.append([])

# Add elements to empty lists.
elements[0].append(1)
elements[0].append(2)

elements[1].append(3)
elements[1].append(4)

# Display top-left element.
print(elements[0][0])

# Display entire list.
print(elements)

# Loop over rows.
for row in elements:
    # Loop over columns.
    for column in row:
        print(column, end="")
    print(end="\n")
"""