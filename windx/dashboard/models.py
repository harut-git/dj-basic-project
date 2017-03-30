from django.contrib.auth.models import User
from django.db import models
import os

from django import forms


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title


class UserId(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.IntegerField()

    def __str__(self):
        return self.name + ' (' + str(self.user_id) + ')'


class Employee(models.Model):
    date = models.DateTimeField()
    entry_id = models.CharField(max_length=200)


class QueryForm(forms.Form):
    name = forms.CharField(label='Enter name', max_length=100)
    date = forms.DateField()
    checkbox = forms.CheckboxInput()





# emp1 = Employee(date="2017-10-17 10:10", entry_id="out122558")
# emp1.save()
# with open('dashboard/20171.txt', 'r') as outfile:
#     lines = outfile.readlines()
#     for i in range(len(lines)):
#         if lines[i].rstrip() == "*":
#             if lines[i + 1].rstrip() == '3' and lines[i + 2].rstrip() == '24':
#                 current_employee = Employee(
#                     date='2017-' + lines[i + 1].rstrip() + '-' + lines[i + 2].rstrip() + ' ' + lines[
#                         i + 3].rstrip() + ':' + lines[i + 4].rstrip(),
#                     entry_id=lines[i + 5].rstrip())
#                 current_employee.save()

#