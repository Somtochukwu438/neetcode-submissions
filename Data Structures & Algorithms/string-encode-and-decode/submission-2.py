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
            start_e = j + 1
            end_e = start_e + length
            decode.append(s[start_e:end_e])
            i = end_e
        return decode

