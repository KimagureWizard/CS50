class Jar:
    def __init__(self, capacity=12):
        self.size = 0
        self.capacity = capacity

    def __str__(self):
        cookies = "🍪" * self.size
        return cookies

    def deposit(self, n):
        self._size += n
        if self.size > self.capacity:
            raise ValueError

    def withdraw(self, n):
        self._size -= n
        if self.size < 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError
        self._size = size


def main():
    capacity = int(input("Capacity: "))
    jar = Jar(capacity)
    print(str(jar))


if __name__ == "__main__":
    main()