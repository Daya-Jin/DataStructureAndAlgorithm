import sys

rows = int(sys.stdin.readline().strip())

mat = list()
for i in range(rows):
    mat.append(sys.stdin.readline().strip())

cols = len(mat[0])

mat_cnt = [[0 for _ in range(cols)] for _ in range(rows)]

# 将矩阵转换成相邻的1的个数
for row in range(rows):
    for col in range(0, cols):
        if col==0:
            mat_cnt[row][col]=int(mat[row][col])
            continue
        if mat[row][col] == '1' and mat[row][col - 1]=='1':
            mat_cnt[row][col] = mat_cnt[row][col-1]+1
        elif mat[row][col] == '1' and mat[row][col - 1]=='0':
            mat_cnt[row][col] = int(mat[row][col])

del mat

# 从上往下找连续值
cur_max=0
for col in range(cols):
    sin_col=list()
    for row in range(rows):
        sin_col.append(mat_cnt[row][col])

    for i,val in enumerate(sin_col):
        if val==0:
            continue
        cnt=1
        tmp_idx=i-1
        while tmp_idx>0 and tmp_idx<len(sin_col):
            if sin_col[tmp_idx]>=val:
                tmp_idx-=1
                cnt+=1
            else:
                break
        tmp_idx=i+1
        while tmp_idx>0 and tmp_idx<len(sin_col):
            if sin_col[tmp_idx] >= val:
                tmp_idx += 1
                cnt+=1
            else:
                break
        ret=min(cnt,val)
        if ret>cur_max:
            cur_max=ret

print(cur_max**2)
