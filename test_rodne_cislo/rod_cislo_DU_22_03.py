def isvalid_rc(rc):  #rc is string

    #condition 1 length
    if len(rc)!=10:
        return False, 'condition broken: incorrect length'

    # condition 2 integers
    try:
        for i in range(len(rc)):
            int(rc[i])
    except ValueError:
        return False, 'condition broken: not integers'

    # condition 3 month format
    if not (int(rc[2:4]) in range(1,13) or int(rc[2:4]) in range(51,63)):
        return False, 'condition broken: month format'

    # condition 4 day format
    if not (
            (int(rc[4:6]) in range(1,31)
        and (int(rc[2:4]) in [4,6,9,11] or int(rc[2:4]) in [54,56,59,61]))
        or (int(rc[4:6]) in range(1,32)
        and (int(rc[2:4]) in [1,3,5,7,8,10,12] or int(rc[2:4]) in [51,53,55,57,58,60,62]))
        or (((int(rc[4:6]) in range(1,29) and int(rc[0:2])%4!=0) or (int(rc[4:6]) in range(1,30) and int(rc[0:2])%4==0))
        and (int(rc[2:4])==2 or int(rc[2:4])==52))
    ):
        return False, 'condition broken: day format'

    # condition 5 divisibility by 11
    if int(rc) % 11 != 0:
        return False, 'condition broken: divisibility by 11'

    #no condition broken
    return True

for i in range(8351010000,8351010030):
    print(isvalid_rc(str(i)), str(i))

#print(isvalid_rc('...))

#8301010003 platne
#8301010014 platne
#8301010025 platne
#8351010008 platne
