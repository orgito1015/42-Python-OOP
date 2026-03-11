def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def helper(day, n):
        if day > n:
            print("Harvest time!")
            return
        print("Day", day)
        helper(day + 1, n)
    helper(1, n)
