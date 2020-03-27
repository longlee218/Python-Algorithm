# hàm đi tìm các vùng đất 1 liền kề theo chiều dọc và ngang
def change_value(i, j, matrix):
    matrix[i][j] = 0        # đổi vùng đất thành biển
    if -1 < i < len(matrix)-1 and matrix[i+1][j] == 1:
        change_value(i+1, j, matrix)            # chạy theo chiều dọc xuống bên dưới tới (số hàng -2)
    if -1 < j < len(matrix[0])-1 and matrix[i][j+1] == 1:
        change_value(i, j+1, matrix)            # chạy theo chiều ngang qua phải tới (số cột - 2)
    if 0 < i < len(matrix)+1 and matrix[i-1][j] == 1:
        change_value(i-1, j, matrix)            # chạy theo chiều dọc lên trên tới hàng = 1
    if 0 < j < len(matrix[0])+1 and matrix[i][j-1] == 1:
        change_value(i, j-1, matrix)            # chạy theo chiều ngang qua trái tới cột = 1


def islands_count(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            # đếm số vùng đất
            if matrix[i][j] == 1:
                count += 1
                change_value(i, j, matrix)
    return count


if __name__ == '__main__':
    matrix_input1 = [[1, 1, 0, 0, 0],
                     [1, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 0, 1, 1]]

    matrix_input2 = [[1, 1, 1, 1, 0],
                     [1, 1, 0, 1, 0],
                     [1, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0]]

    print(islands_count(matrix_input1))
    print(islands_count(matrix_input2))
