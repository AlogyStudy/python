#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djsite.settings')

    import django

    django.setup()

    from app import models

    book_obj = models.Book.objects.get(id=2)

    obj1 = models.Book.objects.filters(publisher__name='xxxx') # INNER JOIN 联表查询
    obj2 = models.Book.objects.all().values('title', 'publisher__name')

