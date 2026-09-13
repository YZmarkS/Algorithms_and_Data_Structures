def letterCombinations(digits: str) -> List[str]:
    if digits == "":
        return []

    mapping = { 2: ["a", "b", "c"], \
                3: ["d", "e", "f"], \
                4: ["g", "h", "i"], \
                5: ["j", "k", "l"], \
                6: ["m", "n", "o"], \
                7: ["p", "q", "r", "s"], \
                8: ["t", "u", "v"], \
                9: ["w", "x", "y", "z"] }

    result = [""]

    for digitChar in digits:
        digit = int(digitChar)
        mapped = list(map(lambda char : list(map(lambda s : s + char, result)), mapping[digit]))
        result = [ s for indiviual_mapped in mapped for s in indiviual_mapped ]

    return result
