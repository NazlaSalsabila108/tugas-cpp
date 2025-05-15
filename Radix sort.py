def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  
    count = [0] * 10  

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    
    max1 = max(arr)

    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

if __name__ == "__main__":
    data = [170, 245, 735, 190, 802, 294, 132, 606]
    print("Data sebelum diurutkan:", data)
    radix_sort(data)
    print("Data setelah diurutkan:", data)