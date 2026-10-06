class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for i in strs:
            encode.append(f"{len(i)}#{i}")
        return "".join(encode)

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start_e = j + 1
            end_str = start_e + length
            i = end_str
            decode.append(s[start_e:end_str])
        return decode



5#Hello