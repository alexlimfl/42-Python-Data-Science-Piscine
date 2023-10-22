def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Takes in *args a quantity of unknown number
    and make the Mean, Median, Quartile (25% and 75%),
    Standard Deviation and Variance according to the
    **kwargs.
    """
    nb = list(args)
    kw = [kwargs[v] for v in kwargs]
    for v in kw:
        try:
            if v == 'mean':
                print(f"mean : {sum(nb) / len(nb)}")
            if v == 'median':
                snb = sorted(nb)
                if len(snb) % 2 == 0:
                    mid1 = snb[(len(snb) // 2) - 1]
                    mid2 = snb[len(snb) // 2]
                    median = (mid1 + mid2) / 2
                else:
                    median = snb[len(snb) // 2]
                print(f"median : {median}")
            if v == 'quartile':
                snb = sorted(nb)
                if len(snb) % 2 == 0:
                    left = snb[:len(snb) // 2]
                    right = snb[len(snb) // 2:]
                    if len(left) % 2 == 0:
                        mid1 = left[(len(left) // 2) - 1]
                        mid2 = left[len(left) // 2]
                        q1 = (mid1 + mid2) / 2
                    else:
                        q1 = left[len(left) // 2]
                    if len(right) % 2 == 0:
                        mid1 = right[(len(right) // 2) - 1]
                        mid2 = right[len(right) // 2]
                        q3 = (mid1 + mid2) / 2
                    else:
                        q3 = right[len(right) // 2]
                else:
                    q1 = snb[len(snb) // 3]
                    q3 = snb[2 * len(snb) // 3]
                print(f"quartile : [{float(q1)}, {float(q3)}]")
            if v == 'std':
                mean = sum(nb) / len(nb)
                squared_diff = [(x - mean) ** 2 for x in nb]
                mean_squared_diff = sum(squared_diff) / len(nb)
                standard_deviation = mean_squared_diff ** 0.5
                print(f"std : {standard_deviation}")
            if v == 'var':
                mean = sum(nb) / len(nb)
                squared_diff = [(x - mean) ** 2 for x in nb]
                mean_squared_diff = sum(squared_diff) / len(nb)
                print(f"var : {mean_squared_diff}")
        except Exception:
            print("ERROR")
