def package_dp(price, weight, flag, n):
    c = [[0 for i in range(n)] for j in range(n)]
    for j in range(n):
        c[0][j] = 0

    for i in range(n):
        c[i][0] = 0
        for j in range(n):
            if weight[i]>flag[j]:
                c[i][j] = c[i-1][j]
            else:
                temp1 = price[i] + c[i-1][j-weight[i]]
                temp2 = c[i-1][j]
                c[i][j] = max(temp1,temp2)
            print c[i][j]
        print ("")
    return c

price = [0, 3000, 2000, 1500, 2000]
weight = [0, 4, 3, 1, 1]
flag = [0, 1, 2, 3, 4]

package_dp(price, weight, flag, 5)
