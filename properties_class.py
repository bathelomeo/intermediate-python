class Presenter():
    def __init__(self, name):
        # Constructor
        self.name = name

    @property
    def name(self):
        print('In the getter')
        return self.__name
    
    @name.setter
    def name(self, value):
        print('In the setter')
        # cool validation here
        self.__name = value

presenter = Presenter('Joe')
presenter.name = 'Arthurjoe'
print(presenter.name)
    
