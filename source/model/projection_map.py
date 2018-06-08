class Seat:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.current = '.'

    def taken(self):
        self.current = 'X'

    def __str__(self):
        return self.current

    def __repr__(self):
        return self.__str__


class ProjectionMap:
    def __init__(self):
        self.map = self.draw_hall()

    def print_hall(self):
        print(' ', end=' ')
        for i in range(1, 11):
            print(i, end=' ')
        print()
        for i, value in enumerate(self.map):
            print(i + 1, end=' ')
            for sub_item in value:
                print(sub_item, end=' ')
            print()

    def draw_hall(self):
        self.map = []
        for i in range(10):
            sub_row = []
            for j in range(10):
                sub_row.append(Seat(i, j))
            self.map.append(sub_row)
        return self.map

    def reserve_seat(self, row, column):
        self.map[row - 1][column - 1].taken()
