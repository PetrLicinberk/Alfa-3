import datetime

class Input:
    def __init__(self, text:str):
        self._text = text

    def get_value(self):
        raise NotImplemented
    
class StringInput(Input):
    def __init__(self, text:str, min_length:int, max_length:int):
        super().__init__(text)
        self._min_len = min_length
        self._max_len = max_length

    def get_value(self):
        value = None
        while value is None:
            print(self._text, end=': ')
            value = input()
            if len(value) < self._min_len or len(value) > self._max_len:
                print('Musite zadat {min} - {max} znaku'.format(min=self._min_len, max=self._max_len))
                value = None
        return value
    
class IntInnput(Input):
    def __init__(self, text: str, min: int, max: int):
        super().__init__(text)
        self._min = min
        self._max = max

    def get_value(self):
        value = None
        while value is None:
            print(self._text, end=': ')
            value = input()
            try:
                value = int(value)
                if value < self._min or value > self._max:
                    print('Musite zadat cislo v rozsahu {min} - {max}.'.format(min=self._min, max=self._max))
                    value = None
            except:
                print('Musite zadat cislo.')
                value = None
        return value
    
class SelectInput(IntInnput):
    def __init__(self, text: str, options: list, get_value):
        super().__init__(text, 1, len(options))
        self._options = options
        self._get_value = get_value
    
    def get_value(self):
        print('Moznosti: ')
        for i in range(len(self._options)):
            print('\t{num}) {opt}'.format(num=i + 1, opt=str(self._get_value(self._options[i]))))
        value = super().get_value()
        return self._options[value - 1]
    
class FloatInput(Input):
    def __init__(self, text: str, min:float, max:float):
        super().__init__(text)
        self._min = min
        self._max = max

    def get_value(self):
        value = None
        while value is None:
            print(self._text, end=': ')
            value = input()
            try:
                value = float(value)
                if value < self._min or value > self._max:
                    print('Musite zadat cislo v rozsahu {min} - {max}.'.format(min=self._min, max=self._max))
                    value = None
            except:
                print('Musite zadat cislo.')
                value = None
        return value
    
class BoolInput(Input):
    def __init__(self, text: str):
        super().__init__(text)

    def get_value(self):
        value = None
        while value is None:
            print(self._text, end=': ')
            value = input().lower()
            if value == 'true':
                value = True
            elif value == 'false':
                value = False
            else:
                print('Zadejte True nebo False.')
                value = None
        return value
    
class DatetimeInput(Input):
    def __init__(self, text: str):
        super().__init__(text)

    def get_value(self):
        value = None
        while value is None:
            print(self._text, end=': ')
            value = input()
            try:
                value = datetime.datetime.strptime(value, '%d-%m-%Y %H:%M:%S')
            except:
                print('Zadejte datum ve tvaru den-mesic-rok hodiny:minuty:sekundy')
                value = None
        return value

class Form:
    def __init__(self, name:str) -> None:
        self._name = name
        self._inputs:list[Input] = []

    def run(self):
        print('{name}:'.format(name=self._name))
        values = []
        for input in self._inputs:
            values.append(input.get_value())
        return values
    
    def add_input(self, input:Input):
        self._inputs.append(input)