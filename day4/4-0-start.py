import random
from sre_constants import BRANCH
import lanny

# two_digit_int = random.randint(11, 14)
# print(two_digit_int)

# multi_digit_float_ = random.random()
# print(multi_digit_float_)

bank_name = lanny.bank
bank_branch = lanny.branch
bank_balance = lanny.balance

print(f"My {bank_name} in {bank_branch} has {bank_balance} only.")

print(lanny.branch)