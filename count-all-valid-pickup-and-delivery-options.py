class Solution:
    def countOrders(self, n: int) -> int:
        def factorial(num):
            if num == 1:
                return 1
            val= ((num % (pow(10, 9) + 7)) * factorial(num - 1)) % (pow(10, 9) + 7)
            return val 

        denominator = pow(2, n)
        inv = pow(denominator, pow(10, 9) + 5, (pow(10, 9) + 7))
        print(inv)
        ans = (factorial(2 * n) * inv) % (pow(10, 9) + 7)
        return ans