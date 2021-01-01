# STAGE 1
class Calculator:
    def __init__(self, nums):
        self.nums = nums

    def addition(self):
        return self.nums[0] + self.nums[1]


my_calc = Calculator([int(x) for x in input().split()])
print(my_calc.addition())
