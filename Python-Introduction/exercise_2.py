human_years = int(input("human_years = "))
if human_years == 1:
    print([1, 15, 15])
elif human_years == 2:
    print([2, 24, 24])
else:
    print([human_years, 24 + 4 * (human_years - 2), 24 + 5 * (human_years - 2)])
