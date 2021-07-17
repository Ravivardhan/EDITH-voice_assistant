from faker import Faker
faker=Faker()
def get_fakes():
    print(f'name:{faker.name()}')
    print(f'address:{faker.address()}')
    print(f'email:{faker.email()}')
    print(f'country:{faker.country()}')
    print(f'url:{faker.url()}')
    print(f'text:{faker.text()}')
