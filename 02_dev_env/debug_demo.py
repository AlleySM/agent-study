def cal_total(price, rate):
    total = 0;
    for p in price:
        total += p
    return total * rate

nums = [10, 20, 30, "40"]
print(cal_total(nums, 1.1))