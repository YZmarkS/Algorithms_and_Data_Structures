def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    def char_to_int(digit: str) -> int:
        return ord(digit) - ord('0')

    def multiply_digit(num: str, digit: int) -> str:
        result = ""
        carry = 0
        for i in range(len(num) - 1, -1, -1):
            c = num[i]
            d = char_to_int(c)
            prod = d * digit + carry
            ones = prod % 10
            carry = prod // 10
            result = str(ones) + result
        if carry > 0:
            result = str(carry) + result
        return result

    def add(bot: str, top: str) -> str:
        if top == "":
            return bot
        result = ""
        carry = 0
        for i in range(-1, - len(top) - 1, -1):
            cb, ct = bot[i], top[i]
            db, dt = char_to_int(cb), char_to_int(ct)
            sum_ = db + dt + carry
            ones = sum_ % 10
            carry = sum_ // 10
            result = str(ones) + result
        if carry > 0:
            result = str(carry) + result
        return result

    result = ""
    for i in range(-1, -len(num2) - 1, -1):
        c = num2[i]
        d = char_to_int(c)
        bot = multiply_digit(num1, d) + ("0" * (abs(i) - 1))
        padded_result = "0" * (len(bot) - len(result)) + result
        result = add(bot, padded_result)

    return result
