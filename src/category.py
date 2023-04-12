class Category:
    def __init__(self, id: int, name: str):
        if type(id) != int:
            raise TypeError
        if id < 0:
            raise ValueError
        self._id = id
        self.set_name(name)

    def __str__(self) -> str:
        return self._name

    def get_id(self) -> int:
        return self._id
    
    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        if type(name) != str:
            raise TypeError
        if len(name) > 32:
            raise ValueError
        self._name = name