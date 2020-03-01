def word_search(matrix, word):
    a = ''
    check = False
    for i in range(len(matrix)):
        matrix[i] = ''.join(matrix[i])
        if word in matrix[i]:
            check = True
        for j in range(len(matrix[0])):
            a += matrix[j][i]
        if word in a:
            check = True
        a = ''
    return check

# solution 2


def dfs(matrix, word, i, j, position_of_words, rows, cols):
    if position_of_words+1 == len(word):
        return True
    next_char = word[position_of_words+1]
    if j+1 < cols and matrix[i][j+1] == next_char:
        if dfs(matrix, word, i, j+1, position_of_words+1, rows, cols):
            return True
    if i+1 < rows and matrix[i+1][j] == next_char:
        if dfs(matrix, word, i+1, j, position_of_words+1, rows, cols):
            return True
    return False


def word_search2(matrix, word):
    check = False
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == word[0]:
                if dfs(matrix, word, i, j, 0, rows, cols):
                    check = True
    return check


if __name__ == '__main__':
    matrix = [['F', 'A', 'C', 'I'],
              ['O', 'B', 'Q', 'P'],
              ['A', 'N', 'O', 'B'],
              ['M', 'A', 'S', 'S']]
    print(word_search(matrix, 'ASS'))
    print(word_search2(matrix, 'ASS'))
