from django.test import TestCase,Client
from django.urls import reverse,resolve
from library.models import *
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.contrib.auth.models import User
import json
from django.core.files import File
from library.forms import *
from django.contrib.auth.models import Group



class TestModels(TestCase):

	def setUp(self):
		self.user = User.objects.create(username='testuser')
		self.user.set_password('12345')
		self.user.save()
		self.logged=self.client.login(username='testuser', password='12345')



	def test_student_extra_model(self):
		std_ins=StudentExtra.objects.create(user=self.user,enrollment='testenrollment',branch='testbranch')

		self.assertEquals(std_ins.enrollment,'testenrollment')

		std_ins.delete()

		self.assertEquals(StudentExtra.objects.all().count(),0)




	def test_book_model(self):
		bookinst= Book.objects.create(name='testbook',isbn=1234,author='testauthor')

		self.assertEquals(bookinst.name,'testbook')

		bookinst.delete()

		self.assertEquals(Book.objects.all().count(),0)



	def test_issuedbook_model(self):
		issue_ins= IssuedBook.objects.create(enrollment='testenroll',isbn='testisbn',issuedate='2021-05-18',expirydate='2021-05-20')

		self.assertEquals(issue_ins.enrollment,'testenroll')

		issue_ins.delete()

		self.assertEquals(IssuedBook.objects.all().count(),0)



