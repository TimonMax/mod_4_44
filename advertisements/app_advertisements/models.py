from django.db import models

class Advertisement(models.Model):

    # товар
    # Строковое поле небольших размеров
    # 'заголовок' - verbose_name - название поля извне
    title = models.CharField('Заголовок', max_length=128)

    # Описание товара
    #Большое текстовое поле
    description = models.TextField('Описание')

    # Имя продавца + контакты
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    # Цена
    # Специальный тип данных с фиксированной запятой
    description = models.TextField('Описание')

    # Уместность торга
    # Логический тип, два значения
    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')

    # Дата публикации
    # Поле записывается при создании объявления
    created_at = models.DateTimeField(auto_now_add=True) 

    # Дата изменения
    # Поле записывается при обновлении объявления
    updated_at = models.DateTimeField(auto_now=True) 

    # Актуальность объявления

    # Количество товара


    # Возможность обмена

    # Адрес продажи/осмотра

    # Б/У товар или нет

    # Возможность взять в долг/рассрочку

    def __str__(self):
        return f"Advertisement(id={self.id}, title=Заголовок {self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'
