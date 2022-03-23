
arr = [1, 2, 4, 7, 8, 3]


for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i] == arr[j]):
            print("Ima duplikate")
