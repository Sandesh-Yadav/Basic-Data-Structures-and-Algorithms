class Search:
    def __init__(self,search):
        self.search = search

    @classmethod
    def list_input(cls,list):
        print("1.Input elements one by one")
        print("2.Input a complete a list")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            b = int(input("How many inputs? : "))
            for i in range(b):
                list.append(int(input("Enter the element : ")))
            return cls(list)
        elif choice == 2:
            list = eval(input("Enter the list : "))
            return cls(list)

    @staticmethod
    def BinarySearch(list, search, low = 0, high = 0):
        mid = int((high + low) / 2)
        if low > high:
            print("Number not found in the list")
        if search == list[mid]:
            print("The number found at position at:",mid + 1,"and index",mid)
        elif search < list[mid]:
            high = mid - 1
            return Search.BinarySearch(list, search, low, high)
        else:
            low = mid + 1
            return Search.BinarySearch(list, search, low, high)

    @staticmethod
    def LinearSearch(list, search):
        for i in range(len(list)):
            if search != list[i]:
                continue
            else:
                print("The number found at position at:",i + 1,"and index",i)

