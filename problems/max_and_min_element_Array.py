class Pair:
    def __init__(self):
        self.min = 0
        self.max = 0

def getMinMaxElement(arr: list, n: int) -> Pair:
    minmax = Pair()

    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax

    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax


arr = list(map(int, input().split()))
minmax = getMinMaxElement(arr, len(arr))
print("Maximum Element:", minmax.max)
print("Minimum Element:",minmax.min)
