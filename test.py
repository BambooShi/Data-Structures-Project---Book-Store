def insertionSort(arr, secArr):
   for i in range(1, len(arr)):
      key = arr[i]
      key2 = secArr[i]
      # Move elements of arr[0..i-1], that are greater than key,
      # to one position ahead of their current position
      j = i-1
    #   print("key: " + str(key) + "\narr[j]: " + str(arr[j]))

      while j >=0 and key < arr[j] :
         arr[j+1] = arr[j]
         secArr[j+1] = secArr[j]
         j -= 1
      arr[j+1] = key
      secArr[j+1] = key2

def insertionSort2(arr, secArr):
   for i in range(1, len(arr)):
      key = arr[i]
      key2 = secArr[i]
      exit = False
      # Move elements of arr[0..i-1], that are greater than key,
      # to one position ahead of their current position
      j = i-1
      while j >=0 or exit == False:
        print(j)
        if key == arr[j]:
            # print("key: " + str(key) + "\narr[j]: " + str(arr[j]))
            if key2 < secArr[j]:
                # print("key2: " + str(key2) + "\nsecArr[j]: " + str(secArr[j]))
                arr[j+1] = arr[j]
                secArr[j+1] = secArr[j]
            j -= 1 
        elif key < arr[j]:
            # print("hi key: " + str(key) + "\narr[j]: " + str(arr[j]))
            arr[j+1] = arr[j]
            secArr[j+1] = secArr[j]
            j -= 1 
        else:
            # print(arr) 
            arr[j+1] = key
            secArr[j+1] = key2
            j -= 1 
            if (i - j) > 1:
                exit = True

def insertionSort3(arr, secArr):
   for i in range(1, len(arr)):
      key = arr[i]
      key2 = secArr[i]
      # Move elements of arr[0..i-1], that are greater than key,
      # to one position ahead of their current position
      j = i-1
    #   print("key: " + str(key) + "\narr[j]: " + str(arr[j]))
      if key == arr[j]:
         while j >= 0 and key2 < secArr[j]:
            secArr[j+1] = secArr[j]
            arr[j+1] = arr[j]
            j -= 1

      while j >=0 and key < arr[j] :
         arr[j+1] = arr[j]
         secArr[j+1] = secArr[j]
         j -= 1
      arr[j+1] = key
      secArr[j+1] = key2

arr = [1, 4, 2, 10, 10, 2]
secArr = ["a", "h", "t", "z", "f", "r"]

insertionSort2(arr, secArr)

# print(arr)
# print(secArr)

# insertionSort(arr, secArr)

print(arr)
print(secArr)