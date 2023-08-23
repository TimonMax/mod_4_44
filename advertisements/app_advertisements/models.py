from django.db import models
from django.contrib import admin
from django.utils.html import format_html

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

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_date = self.created_at.strftime("%H:%M:%S")
            return format_html(
                '<span style="color:green; font-weight:bold;"> Сегодня в {} </span>', 
                created_date
                )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='Дата изменения')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_date = self.updated_at.strftime("%H:%M:%S")
            return format_html(
                '<span style="color:red; font-weight:bold;"> Сегодня в {} </span>', 
                updated_date
                )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    def __str__(self):
        return f"Advertisement(id={self.id}, title=Заголовок {self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'
