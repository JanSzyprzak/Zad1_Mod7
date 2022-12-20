
from faker import Faker

class BaseContact:
    def __init__(self, name, surname, phone_private, mail_adress):
        self.name = name
        self.surname = surname
        self.phone_private = phone_private
        self.mail_adress = mail_adress

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.mail_adress}'

    def contact(self):       
        return f'Wybieram numer {self.phone_private} i dzwonię do {self.name} {self.surname}'

    @property
    def label_length(self):     
        label = sum([len(self.name), len(self.surname), 1])
        return label



class BusinessContact(BaseContact):
    def __init__(self, company, position, phone_business, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.phone_business = phone_business

    def contact(self):       
        return f'Wybieram numer {self.phone_business} i dzwonię do {self.name} {self.surname}'

    @property
    def label_length(self):     
        return super().label_length


fake = Faker() 
def create_contacts(type = 'private', number = 10):
    if type == 'private':
        return [BaseContact(name = fake.first_name(), surname = fake.last_name(), phone_private = fake.phone_number(), mail_adress = fake.email()) for i in range(number)]

    else:
        return [BusinessContact(name = fake.first_name(), surname = fake.last_name(), phone_private = fake.phone_number(), mail_adress = fake.email(), company = fake.company(), position = fake.job(), phone_business = fake.phone_number()) for i in range(number)]


visit_cards_private = create_contacts('private', 5)
visit_cards_business = create_contacts('business', 5)


for i in visit_cards_private:
    print(i)

print()
for i in visit_cards_business:
    print(i)

print()
print(BaseContact.contact(visit_cards_private[0]))
print(visit_cards_private[0].label_length)
print()
print(BusinessContact.contact(visit_cards_business[0]))
print(visit_cards_business[0].label_length)
print()

































