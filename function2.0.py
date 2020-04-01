

class Contact:
    def __init__(self, name, second_name, phone_number, chosen_number=False, *args, **kwargs):
        self.name = name
        self.second_name = second_name
        self.phone_number = phone_number
        self.chosen_number = chosen_number
        self.args = args
        self.kwargs = kwargs

        if not self.chosen_number:
            self.chosen_number = 'нет'
    
    def __str__(self):        
        contact = {'Имя': self.name,
                   'Фамиля': self.second_name,
                   'Телефон': self.phone_number,
                   'В избранных': self.chosen_number,
                   'Дополнительная информация': self.kwargs}

        contact_as_string = ''

        for key, value in contact.items():
            if key != 'Дополнительная информация':
                contact_as_string += f'{key}: {value}\n'
            else:
                contact_as_string += 'Дополнительная информация:\n'
                for k,v in value.items():
                    contact_as_string += f'\t{k}: {v}\n'
        
        return contact_as_string

# задание №1
jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
print(jhon)

