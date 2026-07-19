class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip = address.replace(".","[.]")
        return ip
        