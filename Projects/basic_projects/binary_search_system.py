arr = [0,1,4,8,16,32]
start = 0
end = len(arr)-1
target = int(input("Please Search Your Value: "))
found = False

while (start<=end):
    mid = int((start+end)/2)
    if arr[mid] == target:
        print("done", mid)
        found = True
        break
    elif arr[mid] < target:
        start = mid+1

    else :
        end = mid - 1
if found == False:
    print("Value does't exist in array")