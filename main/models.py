from django.db import models
from multiselectfield import MultiSelectField


class Clothing(models.Model):
    CLOTHING_CHOICES = [    ('Pants', 'Брюки'),    ('Jacket', 'Куртка'),    ('T-shirt', 'Футболка'),    ('Shirt', 'Рубашка'),    ('Jeans', 'Джинсы'),    ('Suit', 'Костюм'),    ('Sweater', 'Свитер'),    ('Blazer', 'Пиджак'),    ('Coat', 'Пальто'),    ('Shorts', 'Шорты'),           ('Hoodie', 'Худи'),    ('Sweatpants', 'Спортивные брюки'),    ('Sweatshirt', 'Свитшот'),    ('Vest', 'Жилет'),    ('Cardigan', 'Кардиган'),    ('Parka', 'Парка'),    ('Windbreaker', 'Ветровка'),    ('Polo shirt', 'Поло'),    ('Tank top', 'Майка без рукавов'),    ('Leather jacket', 'Кожаная куртка'),    ('Raincoat', 'Дождевик'),    ('Trench coat', 'Плащ'),    ('Swim trunks', 'Плавки'),    ('Joggers', 'Джоггеры')]

    COLOR_CHOICES = [
        ('Красный', 'Красный'),
        ('Синий', 'Синий'),
        ('Зеленый', 'Зеленый'),
        ('Желтый', 'Желтый'),
        ('Черный', 'Черный'),
        ('Белый', 'Белый'),
        ('Оранжевый', 'Оранжевый'),
        ('Фиолетовый', 'Фиолетовый'),
        ('Розовый', 'Розовый'),
        ('Коричневый', 'Коричневый'),
        ('Серый', 'Серый'),
        ('Золотой', 'Золотой'),
        ('Серебряный', 'Серебряный'),
        ('Бежевый', 'Бежевый'),
        ('Бирюзовый', 'Бирюзовый'),
        # и другие цвета, которые вы хотите использовать
    ]

    SIZE_CHOICES=[
         ('S(42-44)', 'S(42-44)'), 
         ('M(44–46)', 'M(44–46)'),
        ('L(48–50)', 'L(48–50)'),
        ('XL(50–52)', 'XL(50–52)'), 
        ('XXL(54–56)', 'XXL(54–56)'),
        ('XXXL(56–58)', 'XXXL(56–58)'),
    ]
    NO_STOCK = ('Нет в наличии', 'Нет в наличии')
    name = models.CharField(max_length=2550, choices=CLOTHING_CHOICES)
    image = models.ImageField(upload_to='test1/clothing')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    size = MultiSelectField(max_length=200,choices=SIZE_CHOICES + [NO_STOCK])
    price = models.DecimalField(max_digits=150, decimal_places=2)
    def __str__(self):
        return self.name
    


class Shoes(models.Model):
    SHOE_CHOICES = [
        ('Кеды', 'Кеды'),
        ('Ботинки', 'Ботинки'),
        ('Лоферы', 'Лоферы'),
        ('Мокасины', 'Мокасины'),
        ('Оксфорды', 'Оксфорды'),
        ('Дерби', 'Дерби'),
        ('Эспадрильи', 'Эспадрильи'),
        ('Кроссовки', 'Кроссовки'),
        # и другие типы обуви, которые вы хотите использовать
    ]
    COLOR_CHOICES = [
        ('Красный', 'Красный'),
        ('Синий', 'Синий'),
        ('Зеленый', 'Зеленый'),
        ('Желтый', 'Желтый'),
        ('Черный', 'Черный'),
        ('Белый', 'Белый'),
        ('Оранжевый', 'Оранжевый'),
        ('Фиолетовый', 'Фиолетовый'),
        ('Розовый', 'Розовый'),
        ('Коричневый', 'Коричневый'),
        ('Серый', 'Серый'),
        ('Золотой', 'Золотой'),
        ('Серебряный', 'Серебряный'),
        ('Бежевый', 'Бежевый'),
        ('Бирюзовый', 'Бирюзовый'),
        # и другие цвета, которые вы хотите использовать
    ]
    SIZE_CHOICES=[
        ('38', '38'),
        ('39', '39'),
        ('40', '40'), 
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'), 
        ('45', '45'),
        ('46', '46'),
        ('47', '47'),
        ('48', '48')
    ]
    NO_STOCK = ('Нет в наличии', 'Нет в наличии')
    name = models.CharField(max_length=2550, choices=SHOE_CHOICES)
    image = models.ImageField(upload_to='test1/shoes')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    size = MultiSelectField(max_length=200,choices=SIZE_CHOICES + [NO_STOCK])
    price = models.DecimalField(max_digits=150, decimal_places=2)

    def __str__(self):
        return self.name

class Аccessories(models.Model):
    АCCESS_CHOICES = [
        ('Шарф', 'Шарф'),
        ('Перчатки', 'Перчатки'),
        ('Ремень', 'Ремень'),
        ('Кошелек', 'Кошелек'),
        ('Браслет', 'Браслет'),
        ('Часы', 'Часы'),
        ('Очки', 'Очки'),
        # и другие типы обуви, которые вы хотите использовать
    ]
    COLOR_CHOICES = [
        ('Красный', 'Красный'),
        ('Синий', 'Синий'),
        ('Зеленый', 'Зеленый'),
        ('Желтый', 'Желтый'),
        ('Черный', 'Черный'),
        ('Белый', 'Белый'),
        ('Оранжевый', 'Оранжевый'),
        ('Фиолетовый', 'Фиолетовый'),
        ('Розовый', 'Розовый'),
        ('Коричневый', 'Коричневый'),
        ('Серый', 'Серый'),
        ('Золотой', 'Золотой'),
        ('Серебряный', 'Серебряный'),
        ('Бежевый', 'Бежевый'),
        ('Бирюзовый', 'Бирюзовый'),
        # и другие цвета, которые вы хотите использовать
    ]
    NO_STOCK = ('Нет в наличии', 'Нет в наличии')
    name = models.CharField(max_length=2550, choices= АCCESS_CHOICES)
    image = models.ImageField(upload_to='test1/access')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES  + [NO_STOCK])
    price = models.DecimalField(max_digits=150, decimal_places=2)

    def __str__(self):
        return self.name