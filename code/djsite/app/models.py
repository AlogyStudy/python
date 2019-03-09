# from django.db import models

# # Create your models here.

# class User(models.Model):
#     id = models.AutoField(primary_key=True) # id 主键
#     email = models.CharField(max_length=32) # varchar(32)
#     pwd = models.CharField(max_length=32) # varchar(32)

# # 出版社
# class Press(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=32)

# class Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=30)
#     press = models.ForeignKey(to='Press', on_delete=models.CASCADE) # 外键， 关联Press表

# class Author(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=32)
#     books = models.ManyToManyField(to='Book') # Django包含多对多字段

# # class AuthorToBook(models.Model):
# #     id = models.AutoField(primary_key=True)
# #     author = models.ForeignKey(to='Author', on_delete=models.CASCADE)
# #     book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
