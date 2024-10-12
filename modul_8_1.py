def add_everything_up(a, b):
    try:
        if type(a) == float or type(b) == float:
            if isinstance(a, float):
                aa = str(a)
                s_aa = int(len(aa) - aa.index('.') - 1)
                s_m = s_aa
            if isinstance(b, float):
                bb = str(b)
                s_bb = int(len(bb) - bb.index('.') - 1)
                s_m = s_bb
            if isinstance(a, float) and isinstance(b, float):
                s_m = max(s_aa, s_bb)

            sum_ = round((a + b), s_m)
            # print(a, b)
        else:
            sum_ = a + b
        return sum_
    except:
        sum_ = str(a) + str(b)
        return sum_

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('строка 1', 'строка 2'))
