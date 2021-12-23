class Presenter():
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(self.name)

presenter = Presenter('Joe')
presenter.name = 'ArthurJoe'
presenter.say_hello()