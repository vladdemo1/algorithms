"""
In this mod completed selection sort
"""

class SelectionSort:
    """
    This class contains main selection sort method
    """
    
    def __init__(self, mass) -> None:
        self._mass = mass

    @staticmethod
    def _find_smallest(mass):
        smallest = mass[0]
        smallest_index = 0
        for index in range(1, len(mass)):
            if mass[index] < smallest:
                smallest = mass[index]
                smallest_index = index
        return smallest_index

    def selection_sort(self):
        """
        Main func selection sort
        """
        new_arr = []
        for _ in range(len(self._mass)):
            smallest = self._find_smallest(self._mass)
            new_arr.append(self._mass.pop(smallest))
        return new_arr


def main():
    mass = [1, 24, 5, 2, 100, 14, 2, 55, 69]
    sort = SelectionSort(mass=mass)
    print(sort.selection_sort())


if __name__ == '__main__':
    main()
