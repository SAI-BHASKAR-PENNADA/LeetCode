class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(reversed(list(map(lambda s : s.strip(), s.strip().split(" ")))))

        arr = s.strip().split()
        for i in range(0, len(arr)):
            arr[i] = arr[i].strip()
        return " ".join(reversed(arr))
