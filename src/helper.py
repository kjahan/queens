def check_all_rows(A):
    """
    Check if all rows in 2-dimensional matrix don't have more than one queen
    """
    for row_inx in range(len(A)):
        # compute sum of row row_inx
        if sum(A[row_inx]) > 1:
            return False
    return True

def check_all_columns(A):
    """
    Check if all columns in 2-dimensional matrix don't have more than one queen
    """
    for col_inx in range(len(A)):
        # compute sum of column col_inx
        col_sum = 0
        for row_inx in range(len(A)):
            col_sum += A[row_inx][col_inx]
        if col_sum > 1:
            return False
    return True

def check_all_diagonals(A):
    # first column of each row
    for row_inx in range(len(A)):
        i = row_inx
        j = 0
        diagonal_sum = 0
        while(i >= 0):
            diagonal_sum += A[i][j]
            i -= 1
            j += 1
        if diagonal_sum > 1:
            return False
    for col_inx in range(1, len(A)):
        i = len(A) - 1
        j = col_inx
        diagonal_sum = 0
        while(j <= len(A) - 1):
            diagonal_sum += A[i][j]
            i -= 1
            j += 1
        if diagonal_sum > 1:
            return False
    # first column
    for row_inx in range(len(A)):
        i = row_inx
        j = 0
        diagonal_sum = 0
        while(i <= len(A) - 1):
            diagonal_sum += A[i][j]
            i += 1
            j += 1
        if diagonal_sum > 1:
            return False
    # first row
    for col_inx in range(1, len(A)):
        i = 0
        j = col_inx
        diagonal_sum = 0
        while(j <= len(A) -1):
            diagonal_sum += A[i][j]
            i += 1
            j += 1
        if diagonal_sum > 1:
            return False
    return True

def is_board_valid(A):
    return check_all_rows(A) and check_all_columns(A) and check_all_diagonals(A)
