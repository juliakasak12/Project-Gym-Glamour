from faker import Faker

class BuyingHat:
    search = "czapka zimowa"
    fake = Faker(locale='pl')
    email = fake.email()
    name = fake.first_name()
    last_name = fake.last_name()
    phone = fake.phone_number()
    address = fake.street_address()
    postcode = fake.postcode()
    city = fake.city()
