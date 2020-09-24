import math
def palindrome(x):
    if x< 0 :
        return False
    num_digits = math. floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x *10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
        return True


print(palindrome(121))
