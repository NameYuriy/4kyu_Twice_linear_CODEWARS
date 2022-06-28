def dbl_linear(n):
    res_list, i, j = [1], 0, 0
    while len(res_list)<=n:
        y= 2 * res_list[i] + 1
        z = 3 * res_list[j] + 1
        if y > z:
            res_list.append(z)
            j += 1
        elif y < z:
            res_list.append(y)
            i += 1
        else:
            res_list.append(y)
            i += 1
            j += 1
    return res_list[n]
