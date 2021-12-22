class Sum:
    def __init__(self, number, desired_sum):
        self.number = number
        self.desired_sum = desired_sum

    def find_two_sum(self):
        for n in self.number:
            for i in self.number[self.number.index(n)+1:]:
                if n + i == self.desired_sum:
                    return (self.number.index(n), self.number.index(i))
                    break
                    return None

numbers = Sum(number=[2, 4, 6, 8, 10],desired_sum=12)
print(numbers.find_two_sum())