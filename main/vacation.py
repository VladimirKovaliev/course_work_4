class Vacation:
    '''Класс для создания и сравнения вакансий по payment'''
    def __init__(self, id, vacation_name, link, payment, experience, snippet):
        self.__id = id
        self.__vacation_name = vacation_name
        self.__link = link
        self.__payment = payment
        self.__experience = experience
        self.__snippet = snippet

    @property
    def id(self):
        return self.__id
    @property
    def vacation_name(self):
        return self.__vacation_name
    @property
    def payment(self):
        return self.__payment
    @property
    def snippet(self):
        return self.__snippet

    def __eq__(self, other):
        return self.payment == other
    def __gt__(self, other):
        return self.payment > other
    def __add__(self, other):
        return self.payment + other
    def __le__(self, other):
        return self.payment < other
    def __str__(self):
        return (f'{self.__id},'
                f'{self.__link},'
                f'{self.__vacation_name},'
                f'{self.__snippet},'
                f'{self.__payment},'
                f'{self.__experience},')