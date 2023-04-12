class Customer:
    def __init__(self, id:int, first_name:str, last_name:str, email:str, city:str, street:str, postal_code:str):
        if type(id) != int:
            raise TypeError('id')
        if id < 0:
            raise ValueError('id')
        self._id = id
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_city(city)
        self.set_street(street)
        self.set_postal_code(postal_code)

    def __str__(self) -> str:
        return '{fname} {lname}'.format(fname=self.get_first_name(), lname=self.get_last_name())

    def get_id(self) -> int:
        return self._id
    def get_first_name(self) -> str:
        return self._first_name
    def get_last_name(self) -> str:
        return self._last_name
    def get_email(self) -> str:
        return self._email
    def get_city(self) -> str:
        return self._city
    def get_street(self) -> str:
        return self._street
    def get_postal_code(self) -> str:
        return self._postal_code
    
    def set_first_name(self, fname:str):
        if type(fname) != str:
            raise TypeError
        if len(fname) > 32:
            raise ValueError
        self._first_name = fname
    def set_last_name(self, lname:str):
        if type(lname) != str:
            raise TypeError
        if len(lname) > 32:
            raise ValueError
        self._last_name = lname
    def set_email(self, email:str):
        if type(email) != str:
            raise TypeError
        if len(email) > 64:
            raise ValueError
        self._email = email
    def set_city(self, city:str):
        if type(city) != str:
            raise TypeError
        if len(city) > 64:
            raise ValueError
        self._city = city
    def set_street(self, street:str):
        if type(street) != str:
            raise TypeError
        if len(street) > 64:
            raise ValueError
        self._street = street
    def set_postal_code(self, pcode:str):
        if type(pcode) != str:
            raise TypeError
        if len(pcode) > 5:
            raise ValueError
        self._postal_code = pcode