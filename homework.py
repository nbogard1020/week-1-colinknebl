from collections.abc import Sized

class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, item):
        return item in self.__myTeam

    def __iter__(self):
        for member in self.__myTeam:
            yield member

def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print (len(classmates))

    print()
    print('John' in classmates) # True
    print('Pete' in classmates) # False

    print()
    for classmate in classmates:
        print(classmate) # John => Steve => Tim

    print()
    print('isInstance:', isinstance(
        classmates,
        Sized
    )) # True


main()

