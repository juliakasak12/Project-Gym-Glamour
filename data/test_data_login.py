from faker import Faker

class InvalidLogin:
    email = "tester_alk"
    password = "haslo"
class InvalidPassword:
    email = "testeralk8@gmail.com"
    password = "ala123"
class RandomData:
    fake = Faker(locale='pl')
    email = fake.email()
    password = fake.password()
class ValidData:
    email = "testeralk8@gmail.com"
    password = "Testeralk@88"