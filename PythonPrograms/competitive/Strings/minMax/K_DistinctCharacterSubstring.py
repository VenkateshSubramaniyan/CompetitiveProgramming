from collections import defaultdict


def substring(inp_Str: str, k: int) -> int:
    window_sart = 0
    count_map = dict()
    max_length = 0
    for window_end in range(0, len(inp_Str)):
        # Move right pointer here
        curr_char = inp_Str[window_end]
        count_map[curr_char] = count_map.get(curr_char, 0) + 1
        while len(count_map) > k:
            # Move left pointer here
            left_char = inp_Str[window_sart]
            window_sart += 1
            count_map[left_char] = count_map.get(left_char, 0) - 1
            if (count_map[left_char] == 0):
                count_map.pop(left_char)
        max_length = max(max_length, window_end - window_sart + 1)

    return max_length


print(substring("ceotbojndncbhq", 1))

# print(substring("abcddefg",3))
