class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_length = 0

        # path_length[depth] = total length of path up to this depth
        # depth 0 means root-level file or directory
        path_length = {0: 0}

        for line in input.split("\n"):
            depth = line.count("\t")
            name = line.lstrip("\t")

            # Current absolute path length:
            # parent path length + "/" + current name
            current_length = path_length[depth] + len(name)

            if "." in name:
                max_length = max(max_length, current_length)
            else:
                # Add 1 for the "/" after this directory
                path_length[depth + 1] = current_length + 1

        return max_length