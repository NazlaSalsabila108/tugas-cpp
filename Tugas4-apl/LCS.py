def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])


    index = L[m][n]
    lcs_str = [''] * index
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(lcs_str)

if __name__ == "__main__":
    str1 = input("Masukkan string pertama: ")
    str2 = input("Masukkan string kedua: ")
    hasil = lcs(str1, str2)
    print(f"LCS dari '{str1}' dan '{str2}' adalah: '{hasil}'")
    print(f"Panjang LCS: {len(hasil)}")