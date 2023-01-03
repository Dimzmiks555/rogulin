from django.db import models
from datetime import date

# Create your models here.



# Работник
class Employee(models.Model):
    sur_name = models.CharField('Фамилия', max_length=255, default='')
    first_name = models.CharField('Имя', max_length=255, default='')
    last_name = models.CharField('Отчество', max_length=255, default='')
    passport_number = models.CharField('Серия и номер паспорта', max_length=255, default='')
    passport_date = models.DateField('Дата выдачи', default=date.today)
    passport_given_by = models.CharField('Выдан (кем?)', max_length=255, default='')
    passport_filial_code = models.CharField('Код подразделения', max_length=20, default='')
    passport_address = models.CharField('Адрес прописки', max_length=255, default='')
    driving_license = models.CharField('Номер водительского удостоверения', max_length=255, default='')
    phone = models.CharField('Номер телефона', max_length=255, default='')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self) :
        return f'{self.sur_name} {self.first_name} {self.last_name}'

    
    def fio(self) :
        return f'{self.sur_name} {self.first_name} {self.last_name}'




# Транспорт
class Transport(models.Model):
    name = models.CharField('Название', max_length=255, default='')
    model = models.CharField('Модель', max_length=255, default='')
    reg_number = models.CharField('Регистрационный номер', max_length=20)
    mileage = models.IntegerField('Пробег', default=0)
    driver = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Закрепленный водитель', default=None)
    sts_number = models.CharField('Номер СТС', max_length=100, default='')
    pts_number = models.CharField('Номер ПТС', max_length=100, default='')
    vin = models.CharField('VIN-Номер', max_length=100, default='')

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'



    
    def __str__(self) :
        return f'Транспорт {self.reg_number}'

# Город
class City(models.Model):
    name = models.CharField('Название', max_length=255, default='')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    
    def __str__(self) :
        return f'Город {self.name}'

# Врач
class Doctor(models.Model):
    sur_name = models.CharField('Фамилия', max_length=255, default='')
    first_name = models.CharField('Имя', max_length=255, default='')
    last_name = models.CharField('Отчество', max_length=255, default='')

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врач'

    def fio(self):
        return f'{self.sur_name} {self.first_name} {self.last_name}'

        
    def short_fio(self):
        return f'{self.sur_name} {self.first_name[:1]}. {self.last_name[:1]}.'
    
    def __str__(self):
        return f'Врач {self.fio()}'


# Механик
class Engineer(models.Model):
    sur_name = models.CharField('Фамилия', max_length=255, default='')
    first_name = models.CharField('Имя', max_length=255, default='')
    last_name = models.CharField('Отчество', max_length=255, default='')

    class Meta:
        verbose_name = 'Механик'
        verbose_name_plural = 'Механик'

    def fio(self):
        return f'{self.sur_name} {self.first_name} {self.last_name}'

        
    def short_fio(self):
        return f'{self.sur_name} {self.first_name[:1]}. {self.last_name[:1]}.'
    
    def __str__(self):
        return f'Механик {self.fio()}'


# Прицеп
class Trailer(models.Model):
    name = models.CharField('Название', max_length=255, default='')
    reg_number = models.CharField('Регистрационный номер', max_length=255, default='')

    class Meta:
        verbose_name = 'Прицеп'
        verbose_name_plural = 'Прицепы'

    
    def __str__(self) :
        return f'Прицеп {self.name}/{self.reg_number}'


# Организация
class Company(models.Model):
    fio = models.CharField('ФИО', max_length=255, default='', help_text='Обязательно вводить через пробел!')
    inn = models.CharField('ИНН', max_length=255, default='')
    ogrn = models.CharField('ОГРН', max_length=255, default='')
    address = models.CharField('Юридический адрес', max_length=255, default='')
    phone = models.CharField('Номер телефона', max_length=255, default='')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


    def short_fio(self):
        sur_name = '' 
        first_name = '' 
        last_name = ''

        if len(self.fio.split(' ')) > 2:
             sur_name, first_name, last_name = self.fio.split(' ')


        return f'{sur_name} {first_name[:1]}. {last_name[:1]}.'

    
    def __str__(self) :
        return f'Организация {self.fio}'
