class Solution:
    def reverseWords(self, s: str) -> str:
        string_list = s.split()
        left_pointer, right_pointer = 0, len(string_list) - 1
        while left_pointer <= right_pointer:
            string_list[left_pointer], string_list[right_pointer] = string_list[right_pointer], string_list[left_pointer]
            left_pointer += 1
            right_pointer -= 1
        return ' '.join(string_list)