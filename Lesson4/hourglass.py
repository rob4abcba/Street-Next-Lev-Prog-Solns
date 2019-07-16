size = 3
print("size = ", size)
line_length = size*2
spaces_before_line = 0
print("line_length = ", line_length)
while line_length > 2:
    # for i in range(line_length):    #to iterate on the factors of the number
    #     print(i, end =" ")
    print(" "*spaces_before_line + "*"*line_length)
    line_length = line_length - 2
    spaces_before_line = spaces_before_line + 1
while line_length <= size*2:
    # for i in range(line_length):    #to iterate on the factors of the number
    #     print(i, end =" ")
    print(" "*spaces_before_line + "*"*line_length)
    line_length = line_length + 2
    spaces_before_line = spaces_before_line - 1
    # print(" "*spaces_before_line + "*"*line_length)