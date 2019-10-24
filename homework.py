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
    print('John' in classmates)

    for classmate in classmates:
        print(classmate)

    print(isinstance(
        classmates,
        list
    ))


main()

