def longestEqualSubarray(nums: List[int], k: int) -> int:
    n = len(nums)
    room = k

    freq = dict()
    freq[nums[0]] = 1
    max_freq = 1

    last_num = nums[0]

    l, r = 0, 1
    while r < n:
        next_num = nums[r]
        if next_num in freq and freq[next_num] == max_freq:
            print("Extend Window")
            freq[next_num] += 1
            max_freq = max(max_freq, freq[next_num])
            r += 1
        elif (next_num not in freq or freq[next_num] != max_freq) and 0 < room:
            print("Use Room")
            room -= 1
            freq[next_num] = freq.get(next_num, 0) + 1
            r += 1
        else:
            print("Move Window")
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                freq.pop(nums[l])
            freq[next_num] = freq.get(next_num, 0) + 1
            l += 1
            r += 1

        print(l, r, nums[l:r], freq)

    return max_freq
