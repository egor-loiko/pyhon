class Table:
    def __init__(self, mass):
        self.mass = mass

    def __str__(self):
        return str(self.mass)


class Truck:
    tables_list = []

    def __init__(self, load_capacity):
        self.load_capacity = load_capacity

    def get_load_capacity(self):
        return self.load_capacity

    def get_loaded_capacity(self):
        loaded_capacity = 0
        for i in range(len(self.tables_list)):
            loaded_capacity += self.tables_list[i].mass
        return loaded_capacity

    def get_rest_capacity(self):
        return self.get_load_capacity() - self.get_loaded_capacity()

    def get_list_of_tables(self):
        for i in range(len(self.tables_list)):
            print('Стол №' + str(i + 1) + ': ' + str(self.tables_list[i]) + ' кг')

    def add_item(self, item):
        if self.get_loaded_capacity() + item.mass <= self.load_capacity:
            self.tables_list.append(item)
            print('Стол массой ' + str(item.mass) + ' кг загружен в грузовик')
        else:
            print('Перегрузка!!! Стол массой ' + str(item.mass) + ' кг не может быть добавлен в грузовик')
            print('Перегрузка составляет ' + str(self.get_loaded_capacity() + item.mass - self.load_capacity) + ' кг\n')


table = []
for i in range(0, 5):
    mass = int(input('Введите массу ' + str(i + 1) + '-го стола: '))
    table.append(Table(mass))
    print('Масса ' + str(i + 1) + '-го стола = ' + str(mass) + ' кг')

truck_capacity = int(input('\nВведите грузоподъемность грузовика: '))
truck1 = Truck(truck_capacity)
print("Грузоподъемность грузовика: " + str(truck1.get_load_capacity()) + ' кг\n')

for i in range(0, 5):
    truck1.add_item(table[i])

print('\nСписок столов загруженных в грузовик:')
truck1.get_list_of_tables()

print("\nВ Грузовик загрузили " + str(truck1.get_loaded_capacity()) + ' кг')
print('В грузовике осталось вместимости на ' + str(truck1.get_rest_capacity()) + ' кг')
