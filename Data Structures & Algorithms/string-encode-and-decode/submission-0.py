class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for s in strs:
            encode.append(f"{len(s)}#{s}")
        return "".join(encode)

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            start_str = j + 1
            end_str = start_str + length

            decode.append(s[start_str:end_str])
            i = end_str
        return decode
