def reversed_concatenate(s,i):
    s = s[::-1]
    return s*i

#################################

def sorting(s):
    upper = ""
    lower = ""
    for i in s:
        if(i == " "):
            continue
        if(i.isupper()):
            upper = upper + i
        else:
            lower = lower + i
    return upper+lower

#################################

def reordering(s1,s2):

    if (len(s2) != len(s2)):
        return False 
    list1 = [i for i in s1]
    list2 = [i for i in s2]
    if (list1.sort() == list2.sort()):
        return True
    return False

#################################

def highestNum(l):
    highestNum = None
    highestIndex= None
    for i in range (0,len(l)):
        if lowestNum == None:
            highestNum = l[i]
            highestIndex = i
        if(l[i] > highestNum):
            highestNum = l[i]
            highestIndex = i
    return f"the highest value in the list is {highestNum} at index {highestIndex}"


def lowestNum(l):
    lowestNum= None
    lowestIndex = None
    for i in range (0,len(l)):
        if lowestNum == None:
            lowestNum = l[i]
            lowestIndex = i
        if(l[i]< lowestNum):
            lowestNum = l[i]
            lowestIndex = i
    return f"the lowest value in the list is {lowestNum} at index {lowestIndex}"

#################################
        
def countDigits(n):
    def countDigitsInner(n,counter):
        if n == 0:
            return counter
        counter = counter + 1
        return countDigitsInner(n//10,counter)
    return countDigitsInner(n,0)

#################################

def list_jumps(jumps):
    index = 0
    visitedTable = len(list_jumps) * [False]
    while(index < len(list_jumps)):
        if visitedTable[index]:
            return "cycle"
        visitedTable[index] = True 
        index = index + list_jumps[index]
    return "out of bounds"

##################################

def track_receipt(items):
     totalAmmount = 0
     print("Receipt:")
     for item in items:
         barcode, name, quantity, price = item
         sumOfitem = total_cost(quantity, price)
         print(f"{name} x {quantity} = {sumOfitem:.2f}")
         totalAmount += sumOfitem
     print("Total: {:.2f}".format(totalAmount))
     print()

def total_cost(quantity, price): 
     return quantity * price

def PosSystem():
     while True:
         input_receipt = input("Do you want to start a new receipt: ")
         if input_receipt == "no":
             break
         elif input_receipt == "yes":
             items = []
             while True:
                 barcode = input("Enter the item barcode (or 'no' to finish the receipt): ")
                 if barcode == "no":
                     break
                 name = input("Enter the item name: ")
                 quantity = int(input("Enter the quantity purchased: "))
                 price = float(input("Enter the unit price: "))
                 items.append((barcode, name, quantity, price))

             track_receipt(items)

PosSystem()


        




    
    


