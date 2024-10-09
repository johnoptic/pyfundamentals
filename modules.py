# Modules follow seperation of concerns. i.e a piece of code that is then imported into another file.
# Here we create a series of functions to be used in another file useModules.py
def iAmAModule():
    print('Hello World. I am a module that prints this statement!')

def iAmBaboon():
    print('I am Baboooon')

def baboonLoop():
    baboonSounds = ['ooh', 'ahh', 'cantona']
    for sounds in baboonSounds:
        print(sounds)


