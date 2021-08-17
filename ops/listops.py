from typing import List

def main():
    a: List = [1, 2, 3, 4, 5]
    print(f"a original: {a}")
    end: int = len(a) - 1
    a[end] = float(5 / 2)
    print(f"a muted: {a}")
    
    # list comprehension
    b: List = [int(num * 10) if num < 3 else num for num in a]
    print(f"b: {b}")

    # short if expression
    print(int_cast(2))
    print(int_cast(6))    

def int_cast(x: int) -> int:
    return int(x * 10) if x < 5 else int(x)      

if __name__ == '__main__':
    main()