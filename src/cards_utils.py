def is_straight(li):

    # drop duplicated and sort
    li = list(set(li))
    li = sorted(li)

    # if not at least 5 diff items
    if not len(li) >= 5:
        return -1

    # compute each 5 following numbers possible
    LI_li = []

    for i, _ in enumerate(li):
        sub_li = li[i : i + 5]
        if len(sub_li) == 5:
            # print(sub_li)
            LI_li.append(sub_li)

    # for each of this 5 number foolowing combinaison possible
    Li_lo = list()
    for lo in LI_li:

        # compute if val[i]+1 ==  val[i+1]
        lu = [lo[i] + 1 == lo[i + 1] for i, v in enumerate(lo[:-1])]

        # add the sum of this True / False
        Li_lo.append((lo, sum(lu)))

    # for each pair (5 number follonig possible , sum (val[i]+1 == val[i]+1))
    # select the number max of the list IF there is sum >= 4
    Li_lo = [max(i) for i, j in Li_lo if j >= 4]

    # if list empty => no straight
    if not len(Li_lo):
        return -1

    # if  multiple straights possible in the initial list return the max value of all straithgs posible
    return max(Li_lo)


if __name__ == "__main__":

    print(is_straight([1, 3, 5, 7, 9, 10, 11, 13, 15]))  # FALSE

    print(is_straight([1, 2, 3]))  # FALSE

    print(is_straight([1, 2, 3, 4, 5, 6, 7]))  # TRUE

    print(is_straight([1, 1, 3, 3, 4, 5, 6, 7, 9, 12]))  # TRUE

    print(is_straight([1, 2, 3, 4, 5]))  # TRUE
