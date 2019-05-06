import random

ocean_color = (0, 125, 255)
coast_color = (0, 133, 255)
icecap_color = (180, 245, 255)
beach_color = (243, 248, 213)
grass_color = (27, 172, 1)
desert_color = (233, 238, 203)
tundra_color = (216, 255, 222)
forest_color = (40, 170, 10)
rforest_color = (11, 80, 23)
taiga_color = (149, 255, 167)
mountain_color = (164, 164, 164)
raw_elem = (0, 0, 0)

polar0 = (255, 255, 255)
cold1 = (200, 207, 240)
cold2 = (0, 240, 220)
tempe3 = (62, 200, 63)
tempe4 = (5, 200, 8)
warm5 = (200, 200, 3)
tropic6 = (170, 190, 3)
tropic7 = (230, 25, 3)
super_hot8 = (255, 0, 0)
top_heat9 = (50, 0, 0)
sun_heat10 = (0, 0, 0)

biomes = {'mar_lake': -5, 'mar_pol': -4, 'mar_temp': -3, 'mar_trop': -2, 'ice_cap': -1, 'coast': 0, 'beach': 1,
          'grassland': 2, 'desert': 3, 'forest': 4, 'rainforest': 5, 'taiga': 6, 'tundra': 7, 'mountain': 8,
          'pur_element': 9}


# noinspection PyAttributeOutsideInit
class Board:
    def __init__(self):
        self.columns = 30
        self.rows = 30
        self.lock = False

        self.board_array = []
        self.prev_spots = []
        self.obsession = 0
        self.iteration = 0
        self.stage_note = 'Initializing...'
        self.ele_map = []
        self.heat_map = []
        self.environ_map = []
        self.fertil_map = []

    def generate(self):
        self.lock = True
        self.board_array = []
        self.prev_spots = []
        self.stage_note = 'Pouring the waters into the world...'
        for _ in range(0, self.rows):
            row = []
            for _ in range(0, self.columns):
                row.append('_')
            self.board_array.append(row)

        genertime = int((self.rows + self.columns) * 10 + (self.rows + self.columns) * 1.5 ** (5 * (self.rows + self.columns - 5)/(2.1 * (self.rows + self.columns))))
        print(genertime)

        self.stage_note = 'Raising the lands from the oceans...'
        for a in range(0, genertime):
            self.iterate(a)
            self.ele_map = self.board_array
            if a == 40:
                self.stage_note = 'Expansionizing...'

        self.stage_note = "Raising the continental shelves..."
        for y in range(0, self.rows):
            for x in range(0, self.columns):
                landlik = 0
                if self.board_array[y][x] == '_':
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            try:
                                if self.board_array[y + j][x + i] != '_' and self.board_array[y + j][x + i] != '-':
                                    landlik += 1
                                    self.board_array[y][x] = '-'
                            except IndexError:
                                pass
                    if (landlik > random.randint(2, 5) and random.randint(0, 100) < random.randint(84, 95)) or\
                            random.randint(0, 50000) < 15:
                        self.board_array[y][x] = str(random.choice([1, 1, 1, 2, 1, 1, 2, 1, 1, 1]))
                    if landlik == 8:
                        self.board_array[y][x] = '-'

                self.ele_map = self.board_array

        abi = ''
        for row in self.board_array:
            for tile in row:
                abi += tile
            abi += '\n'

        print(abi)
        self.review()

        self.ele_map = self.board_array
        self.board_array = []

        self.stage_note = 'Placing the sun in the sky...'
        for y in range(0, self.rows):
            row = []
            for x in range(0, self.columns):
                distance = abs(self.rows / 2 - y) / self.rows
                if self.ele_map[y][x] == '_':
                    albedo = 1
                elif self.ele_map[y][x] == '-':
                    albedo = 1.2
                else:
                    albedo = 1.5 * 2.5 * int(self.ele_map[y][x])

                temp = int(-12 * distance + 5 + 2 / albedo)

                if temp > 10:
                    temp = 10
                row.append(str(temp))

            self.board_array.append(row)

        abi = ''
        for row in self.board_array:
            for tile in row:
                abi += '{}'.format(tile)
            abi += '\n'

        print(abi)

        self.heat_map = self.board_array
        self.board_array = []

        self.stage_note = 'Starting ecosystems...'
        for y in range(0, self.rows):
            row = []
            for x in range(0, self.columns):
                bi = 2
                if self.ele_map[y][x] == '-':
                    if self.heat_map[y][x] == '0' and random.randint(0, int(abs(self.rows / 2 - y) / self.rows)) > 0.3:
                        bi = 'i'
                    else:
                        bi = biomes['coast']
                elif self.ele_map[y][x] == '1':
                    try:
                        if (self.ele_map[y + 1][x] == '-' or self.ele_map[y - 1][x] == '-' or
                            self.ele_map[y][x + 1] == '-' or self.ele_map[y][x - 1] == '-') and\
                                random.randint(0, 50) > 7 and self.heat_map[y][x] != '0':
                            bi = biomes['beach']
                        else:
                            if random.randint(0, 10) < 8:
                                if self.heat_map[y][x] == '0':
                                    bi = biomes['tundra']
                                else:
                                    bi = biomes['grassland']
                            else:
                                if int(self.heat_map[y][x]) < random.choice([1, 2]):
                                    bi = biomes['taiga']
                                else:
                                    bi = biomes['forest']
                    except IndexError:
                        pass
                elif self.ele_map[y][x] == '2':
                    if random.randint(0, 100) < 55:
                        if self.heat_map[y][x] == '0':
                            bi = biomes['tundra']
                        elif int(self.heat_map[y][x]) > 3 and random.randint(0, 500) < 110:
                            bi = biomes['desert']
                        else:
                            bi = biomes['grassland']
                    else:
                        if int(self.heat_map[y][x]) < random.choice([1, 2]):
                            bi = biomes['taiga']
                        elif int(self.heat_map[y][x]) > random.choice([3, 4, 4, 4, 5]):
                            bi = biomes['rainforest']
                        else:
                            bi = biomes['forest']
                else:
                    if self.ele_map[y][x] == '_':
                        bi = '-'
                    else:
                        bi = biomes['mountain']

                if random.randint(0, 500) < 5 and self.ele_map[y][x] != '_' and '-':
                    bi = biomes['pur_element']

                row.append(bi)
            self.board_array.append(row)

        abi = ''
        for row in self.board_array:
            for tile in row:
                abi += '{}'.format(tile)
            abi += '\n'

        print(abi)

        self.stage_note = 'Adding fertilizer...'
        self.environ_map = self.board_array
        self.board_array = []

        for y in range(0, self.rows):
            row = []
            for x in range(0, self.columns):
                if self.environ_map[y][x] == 0:
                    fertbio = 0.1
                elif self.environ_map[y][x] == 3 or 1 or 6:
                    fertbio = 0.7
                elif self.environ_map[y][x] == 8 or 6 or 7:
                    fertbio = 1.2
                elif self.environ_map[y][x] == 5:
                    fertbio = 1.5
                elif self.environ_map[y][x] == 4:
                    fertbio = 1.7
                elif self.environ_map[y][x] == 2:
                    fertbio = 2.1
                elif self.environ_map[y][x] == '-':
                    fertbio = 0
                else:
                    fertbio = 1.6

                fertbio += random.randint(0, 10) / 10

                if self.environ_map[y][x] == '-':
                    fertbio = 0.05

                fertbio = int(fertbio * (2.55 + random.randint(0, 12) / 17))

                row.append(fertbio)
            self.board_array.append(row)

        abi = ''
        for row in self.board_array:
            for tile in row:
                abi += '{}'.format(tile)
            abi += '\n'

        print(abi)

        self.fertil_map = self.board_array
        self.board_array = []

        self.lock = False

    def iterate(self, iteration):
        self.spot = [random.randint(0, self.columns), random.randint(0, self.rows)]
        self.acceptability = 0
        self.obsession = 0
        self.iteration = iteration

        while self.acceptability < 1 / 2 * iteration * (50 / (self.rows + self.columns)) and self.obsession < 500:
            self.acceptability = 0
            self.obsession += 1

            for s in self.prev_spots:
                if self.spot[0] == s[0] and self.spot[1] == s[1]:
                    self.acceptability -= 5
                if s[0] - 2 < self.spot[0] < s[0] + 2 and s[1] - 2 < self.spot[1] < s[1] + 2:
                    self.acceptability += 3

            self.spot = [random.randint(0, self.columns), random.randint(0, self.rows)]

            if self.obsession == 500:
                self.guide = random.choice(self.prev_spots)

                try:
                    self.spot = [self.guide[0] + random.choice([-1, 0, 1]), self.guide[1] + random.choice([-1, 0, 1])]

                    if self.spot[0] > self.columns - 1:
                        self.spot[0] = self.columns - 1
                    elif self.spot[0] < 0:
                        self.spot[0] = 0
                    if self.spot[1] > self.rows - 1:
                        self.spot[1] = self.rows - 1
                    elif self.spot[1] < 0:
                        self.spot[1] = 0

                except IndexError:
                    self.spot = [self.guide[0], self.guide[1]]

        print(self.spot, iteration + 1)
        spot = self.spot

        if self.board_array[spot[1] - 1][spot[0] - 1] == '1':
            self.board_array[spot[1] - 1][spot[0] - 1] = '2'
        elif self.board_array[spot[1] - 1][spot[0] - 1] == '2' and random.randint(0, 50) < random.randint(5, 21):
            self.board_array[spot[1] - 1][spot[0] - 1] = '3'
        elif self.board_array[spot[1] - 1][spot[0] - 1] == '3' and random.randint(0, 50) > random.randint(1, 5):
            pass
        else:
            self.board_array[spot[1] - 1][spot[0] - 1] = '1'

        self.prev_spots.append(spot)

    def review(self):
        total_land = 0
        total_sea = 0
        num_mountains = 0
        num_hills = 0
        # num_cities = 0

        for row in self.board_array:
            for tile in row:
                if tile != '_' and tile != '-':
                    total_land += 1

                    if tile == '2':
                        num_hills += 1
                    elif tile == '3':
                        num_mountains += 1
                else:
                    total_sea += 1

        print(total_land, total_sea, '{}%'.format(int(100 * total_land / (self.rows * self.columns))), num_hills,
              num_mountains)

    def output(self, list):
        if list == 'ele':
            list = self.ele_map
        elif list == 'hot':
            list = self.heat_map
        elif list == 'bio':
            list = self.environ_map
        elif list == 'fer':
            list = self.fertil_map

        abi = ''
        for row in list:
            for tile in row:
                abi += tile
            abi += '\n'

        return abi


if __name__ == '__main__':
    b = Board()
    b.generate()