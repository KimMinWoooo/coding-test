def solution(sizes):
    row, col = 0,0
    for s in sizes:
        row = max(max(s[0],s[1]), row)
        col = max(min(s[0],s[1]), col)
    return row*col
