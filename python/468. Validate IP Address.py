class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            return self.validateIPv4(queryIP)

        if ":" in queryIP:
            return self.validateIPv6(queryIP)

        return "Neither"

    def validateIPv4(self, ip: str) -> str:
        parts = ip.split(".")

        if len(parts) != 4:
            return "Neither"

        for part in parts:
            # Empty part is invalid
            if not part:
                return "Neither"

            # Must contain only digits
            if not part.isdigit():
                return "Neither"

            # Leading zeros are invalid unless the part is exactly "0"
            if len(part) > 1 and part[0] == "0":
                return "Neither"

            # Must be between 0 and 255
            if int(part) > 255:
                return "Neither"

        return "IPv4"

    def validateIPv6(self, ip: str) -> str:
        parts = ip.split(":")

        if len(parts) != 8:
            return "Neither"

        valid_chars = set("0123456789abcdefABCDEF")

        for part in parts:
            # Each group must have length 1 to 4
            if len(part) == 0 or len(part) > 4:
                return "Neither"

            # Must contain only hexadecimal characters
            for ch in part:
                if ch not in valid_chars:
                    return "Neither"

        return "IPv6"