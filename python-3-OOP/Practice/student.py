
# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")
# def get_name():
#     return input("Name: ")
# def get_house():
#     return input("House: ")
# if __name__ == "__main__":
#     main()

# def main():
#     name, house = get_student()
#     name = 'Alexa'
#     print(f"{name} from {house}")
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]
# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)
# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]
# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")
# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student
# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}
# if __name__ == "__main__":
#     main()

# class Student:
#     ...
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
# def get_student():
#     student = Student()
#     ss = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     student.A = input("A: ")
#     ss.name = 'ABC'
#     return student
# if __name__ == "__main__":
#     main()

# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house)
#     return student
# if __name__ == "__main__":
#     main()

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)
# if __name__ == "__main__":
#     main()

# class Student:
#     def __init__(self, name, house, patronus):
#         """RETURNS NONE"""
#         if not name:
#             raise ValueError("Missing name")
#         # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#         self.patronus = patronus

#     def __str__(self):
#         """RETURNS STR"""
#         return f"{self.name} from {self.house}"
# def main():
#     student = get_student()
#     print(student)
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus)
# if __name__ == "__main__":
#     main()

# class Student:
#     def __init__(self, name, house, patronus=None):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
#             raise ValueError("Invalid patronus")
#         self.name = name
#         self.house = house
#         self.patronus = patronus
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "🐴"
#             case "Otter":
#                 return "🦦"
#             case "Jack Russell terrier":
#                 return "🐶"
#             case _:
#                 return "🪄"
# def main():
#     student = get_student()
#     print("Expecto Patronum!")
#     print(student.charm())
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ") or None
#     return Student(name, house, patronus)
# if __name__ == "__main__":
#     main()

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Invalid name")
#         self.name = name
#         self.house = house
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     # Getter for house
#     @property
#     def house(self):
#         return self._house
#     # Setter for house
#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house

# def main():
#     student = get_student()
#     print(student)
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)
# if __name__ == "__main__":
#     main()


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()