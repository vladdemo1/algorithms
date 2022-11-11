"""
In this mod completed quick sort
"""
import random


class QuickSort:
    """
    This class contains main quick sort method
    """
    
    def __init__(self, mass) -> None:
        self.result = self.quick_sort(mass)


    def quick_sort(self, mass):
        """
        Main func about quick sort
        """

        if not mass:
            return mass

        pivot = mass[random.choice(range(0, len(mass)))]

        head = self.quick_sort([element for element in mass if element < pivot])
        tail = self.quick_sort([element for element in mass if element > pivot])
        return head + [element for element in mass if element == pivot] + tail


def main():
    mass = [213, 43, 57, 12, 4, 675, 2314, 140, 63]
    quick = QuickSort(mass)
    print(quick.result)


if __name__ == "__main__":
    main()
