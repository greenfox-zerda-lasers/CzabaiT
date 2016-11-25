
class Maps:
    def __init__(self):
        self.num_of_rows = 11
        self.num_of_columns = 10

    def available_tile_lister(self, actual_level):
        availables = []
        for i in range(self.num_of_rows):
            for j in range(self.num_of_columns):
                if actual_level[i][j] == '_':
                    availables.append([i, j])
        return availables

class FirstMap(Maps):
    def __init__(self):
        super().__init__()
        self.level_map = [
            ['_', '_', '_', 'W', '_', 'W', '_', '_', '_', '_'],
            ['_', '_', '_', 'W', '_', 'W', '_', 'W', 'W', '_'],
            ['_', 'W', 'W', 'W', '_', 'W', '_', 'W', 'W', '_'],
            ['_', '_', '_', '_', '_', 'W', '_', '_', '_', '_'],
            ['W', 'W', 'W', 'W', '_', 'W', 'W', 'W', 'W', '_'],
            ['_', '_', 'W', 'W', '_', '_', '_', '_', 'W', '_'],
            ['_', '_', 'W', 'W', '_', 'W', 'W', '_', 'W', '_'],
            ['_', '_', '_', '_', '_', 'W', 'W', '_', 'W', '_'],
            ['_', 'W', 'W', 'W', '_', '_', '_', '_', 'W', '_'],
            ['_', '_', '_', 'W', '_', 'W', 'W', '_', 'W', '_'],
            ['_', 'W', '_', 'W', '_', 'W', '_', '_', '_', '_']
        ]

        self.level_availables = self.available_tile_lister(self.level_map)

class SecondMap(Maps):
    def __init__(self):
        super().__init__()
        self.level_map = [
            ['_', '_', '_', 'W', '_', 'W', '_', '_', '_', '_'],
            ['_', 'W', '_', '_', '_', 'W', '_', 'W', 'W', '_'],
            ['_', 'W', 'W', 'W', '_', 'W', '_', 'W', '_', '_'],
            ['_', '_', '_', '_', '_', 'W', '_', 'W', '_', '_'],
            ['W', 'W', 'W', 'W', '_', '_', '_', 'W', 'W', '_'],
            ['_', '_', 'W', 'W', '_', 'W', '_', '_', 'W', '_'],
            ['_', '_', 'W', 'W', '_', 'W', 'W', '_', 'W', '_'],
            ['_', '_', '_', '_', '_', 'W', 'W', '_', 'W', '_'],
            ['_', 'W', 'W', 'W', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', 'W', '_', 'W', 'W', 'W', 'W', '_'],
            ['_', 'W', '_', 'W', '_', '_', '_', '_', '_', '_']
        ]

        self.level_availables = self.available_tile_lister(self.level_map)

class ThirdMap(Maps):
    def __init__(self):
        super().__init__()
        self.level_map = [
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', 'W', 'W', 'W', '_', 'W', 'W', '_'],
            ['_', 'W', 'W', 'W', '_', '_', '_', '_', 'W', '_'],
            ['_', '_', '_', 'W', '_', 'W', '_', '_', '_', '_'],
            ['W', 'W', 'W', 'W', '_', 'W', 'W', '_', 'W', '_'],
            ['_', '_', '_', '_', '_', 'W', '_', '_', 'W', '_'],
            ['_', '_', 'W', 'W', 'W', 'W', 'W', '_', 'W', '_'],
            ['_', '_', '_', '_', '_', 'W', 'W', 'W', 'W', '_'],
            ['_', 'W', 'W', 'W', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', 'W', '_', 'W', 'W', '_', 'W', '_'],
            ['_', 'W', '_', '_', '_', '_', '_', '_', 'W', '_']
        ]

        self.level_availables = self.available_tile_lister(self.level_map)
