from utils import user


def main():
    tom = user.Person("Tom")
    tom.age = 37
    tom.display_info()  # Name: Tom  Age: 37

    bob = user.Person("Bob")
    bob.age = 41
    bob.display_info()  # Name: Bob  Age: 41


if __name__ == '__main__':
    main()

