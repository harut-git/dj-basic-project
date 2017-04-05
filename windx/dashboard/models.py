from django.contrib.auth.models import User
from django.db import models
import os
import re

from django import forms


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Employee(models.Model):
    day = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    hour = models.CharField(max_length=100)
    minute = models.CharField(max_length=100)
    entry_id = models.CharField(max_length=200)
    action = models.CharField(max_length=100)


class UserId(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' (' + str(self.user_id) + ')'


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
#             if lines[i + 1].rstrip() == '3':
#                 r = re.compile("([a-zA-Z]+)([0-9]+)")
#                 m = r.match(lines[i + 5].rstrip())
#                 action = m.group(1)
#                 clear_id = m.group(2)
#                 current_employee = Employee(
#                     month=lines[i + 1].rstrip(),
#                     day=lines[i + 2].rstrip(),
#                     hour=lines[i + 3].rstrip(),
#                     minute=lines[i + 4].rstrip(),
#                     entry_id=clear_id,
#                     action=action
#                 )
#                 current_employee.save()
