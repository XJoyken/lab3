def spy_game(nums):
    check1 = False
    check2 = False
    check3 = False

    for num in nums:
        if num == 0 and not check1:
            check1 = True
        elif num == 0 and check1 and not check2:
            check2 = True
        elif num == 7 and check1 and check2:
            check3 = True

    if(check1 and check2 and check3):
        print(True)
    else:
        print(False)
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])
spy_game([0, 1, 2, 3, 4, 5, 6, 7, 0])
spy_game([0, 1, 2, 3, 4, 5, 6, 0, 7])
spy_game([0, 1, 0, 2, 7])