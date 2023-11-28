class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result_string = ""
        for char1, char2 in zip(word1, word2):
            result_string += char1 + char2

        if len(word1) > len(word2):
            remaining_chars = word1[len(word2):]
            result_string += remaining_chars
        if len(word1) < len(word2):
            remaining_chars = word2[len(word1):]
            result_string += remaining_chars
        return result_string
