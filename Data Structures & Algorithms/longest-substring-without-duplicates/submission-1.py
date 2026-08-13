class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_map:
                # update left pos
                # left need to point to the place which is current right pointer pos, to update the left pointer
                left = max(left, char_map[s[right]] + 1)

            # then add this value into char_map anyways
            char_map[s[right]] = right
            # then update the max length
            max_len = max(max_len, right - left + 1)

        return max_len