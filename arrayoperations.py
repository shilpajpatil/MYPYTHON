
import array
def main():
    arr=array.array('i',[1,2,3])
    #----------------print array element------------------
    for i in range(0,3):
        print("array can be:",arr[i])

    #---------------adding element inside array---------------
    arr.append(4);
    arr.append(5);
    arr.append(6);
    arr.append(6)
    arr.append(4);

    print("after adding element inside array:",arr)

    #---------inserting element inside specific position insert(value,position)-----------------
    arr.insert(5,15)
    arr.insert(3,12)

    print("array after adding element at position:",arr)

    #-------to pop element from the array -----------------------------
    poped=arr.pop(6)   #poping element at given position 5
    print("poped element from array",poped)
    print("array after poping element",arr)

    # -----remove function used to remove first occurance of the value---------
    arr.remove(4)

    print("after removing a element given array:",arr)

    #----index function returns index of first occurance of the element---------
    index_return=arr.index(6)
    print("it returns index of first occrance of that argument",index_return)
    print("array after returning the index",arr)

    #----reversing an array use reverse function --------------
    arr.reverse()
    print("reversed array:",arr)





if __name__ == "__main__":
    main()