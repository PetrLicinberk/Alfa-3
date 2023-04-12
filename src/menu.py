class Menu:
    def __init__(self, name:str):
        self._name = name
        self._options:list[Option] = []
        self.input_message:str = ''

    def __str__(self) -> str:
        string = '{name}:'.format(name=self._name)
        for i in range(len(self._options)):
            string += '\n{num}) {text}'.format(num=i + 1, text=self._options[i]._text)
        return string

    def add_opt(self, text:str, action):
        self._options.append(Option(text, action))

    def user_input(self):
        opt_number = None
        while opt_number is None:
            print(self.input_message, end='')
            opt_number = input()
            try:
                opt_number = int(opt_number)
            except:
                opt_number = None
            if opt_number is None:
                print('Musite zadat cislo.')
                continue
            if opt_number < 1 or opt_number > len(self._options):
                print('Cislo musi byt v rozsahu 1 - {max}'.format(max=len(self._options)))
                opt_number = None
        self._options[opt_number - 1]._action()

class Option:
    def __init__(self, text:str, action):
        self._text:str = text
        self._action = action