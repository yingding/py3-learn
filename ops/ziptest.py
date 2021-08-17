from typing import List, Tuple

def main():
    a: List = [1, 3, 5, 7]
    b: List = [2, 4, 6, 8]

    zipped_list: List = list(zip(a, b))
    print(zipped_list)

    unzipped_list: List = list(zip(*zipped_list))
    print(unzipped_list)
    
    # tuple are immutable
    print(type(unzipped_list[0]))
    l_2: Tuple = unzipped_list[1]
    print(f"{l_2}, {len(l_2)}")

    # can not change the element of l_2
    print(f"first element of l_2 is: {l_2[0]}")
   
    # tuple type is not mutable  
    try:
        l_2[0] = 6
    except TypeError as err:
        print(err)
    # except (TypeError, Exception): 
    #    # catch a list of exception and print your own
    #    print("Two errors ocurred")
        


if __name__ == '__main__':
    main()