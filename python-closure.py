def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)

for i in range(1, 11):
    print("{x} X {y} = {z}".format(x=3,y=i,z=times3(i)))
