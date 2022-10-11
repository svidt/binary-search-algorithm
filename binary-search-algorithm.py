import random

class style:
   BOLD = '\033[1m'
   END = '\033[0m'

def binary_search(list, target):
    start = 0
    end = len(list) - 1
    while(start <= end):
        center = (start + end) // 2
        if(list[center] > target):
            end = center -1
        elif(list[center] < target):
            start = center + 1
        else:
            return center
    return None

list = random.sample(range(0, 100), 50)
list.sort()

print(style.BOLD + "\nBinary Search Algorithm\n" + style.END + "50 random numbers in incremental order.\n\n", list)

while True:
    try:
        target = int(input("\nPick a number between 0 - 100: "))
        if target > 100:
            print("Too large a number")
            continue
        elif target < 0:
            print("Too small a number")
            continue
        else:
            print("The index for", target, "is", style.BOLD, binary_search(list, target), style.END)
            continue
    except:
        print("Try again..")
        continue
