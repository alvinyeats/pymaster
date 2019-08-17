
def make_average():
    series = []

    def average(new_val):
        series.append(new_val)
        total = sum(series)
        return total/len(series)

    return average

avg = make_average()
print(avg(1))
print(avg(2))
print(avg(4))
print(series)