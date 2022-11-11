"""
In this mod completed binary search
"""

class Binary:
    """
    This class contains main binary search method
    """
    
    def __init__(self, mass, item) -> None:
        self._mass = mass
        self._item = item

    def binary_search(self):
        """
        Main func binary search
        """
        
        low = 0
        high = len(self._mass) - 1

        while low <= high:
            mid = round((low + high) / 2)
            guess = self._mass[mid]

            if guess == self._item:
                return mid

            if guess > self._item:
                high = mid - 1
            else:
                low = mid + 1
        return None


def main():
    mass = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    binary = Binary(mass=mass, item=21)
    print(binary.binary_search())


if __name__ == "__main__":
    main()
