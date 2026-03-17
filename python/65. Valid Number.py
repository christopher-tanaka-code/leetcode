class Solution:
    def isNumber(self, s: str) -> bool:
        def is_integer(x):
            if not x:
                return False
            if x[0] in '+-':
                x = x[1:]
            return x.isdigit()

        def is_decimal(x):
            if not x:
                return False
            if x[0] in '+-':
                x = x[1:]

            if '.' not in x:
                return False

            left, right = x.split('.', 1)

            # cases:
            # "123." -> left digits
            # ".123" -> right digits
            # "123.456" -> both sides
            if left and not left.isdigit():
                return False
            if right and not right.isdigit():
                return False

            return left != "" or right != ""

        # split exponent
        if 'e' in s or 'E' in s:
            parts = s.split('e') if 'e' in s else s.split('E')
            if len(parts) != 2:
                return False

            base, exp = parts
            return (is_integer(base) or is_decimal(base)) and is_integer(exp)

        # no exponent
        return is_integer(s) or is_decimal(s)