def median():
    lst = [1, 2, 3, 4, 5]
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        med = (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        med = lst[n//2]
    return med

def main():
    print("This median is", median())
if __name__=="__main__":
    main()