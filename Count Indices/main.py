from typing import List

def countIndices(self, n: int, arr: List[int]) -> int:
    brr = sorted(arr)
    return sum(a != b for a, b in zip(arr, brr))