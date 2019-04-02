def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """

    idx = []
    if x[0] > x[1]:
        idx.append(0)
    for i in range(len(x)-1):
        if i < 0:
            continue

        # `i` is a local maximum if the signal decreases before and after it
        if x[i-1] < x[i] and x[i+1] < x[i]:
            idx.append(i)
    if x[-1] > x[-2]:
        idx.append(len(x)-1)
    return list(set(idx))
