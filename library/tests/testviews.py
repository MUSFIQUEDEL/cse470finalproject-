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

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()


	def test_home_view_without_authentication(self):
		response = self.client.get(reverse('home_view'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/index.html')


	def test_home_view_with_authentication(self):
		self.user = User.objects.create(username='testuser')
		self.user.set_password('12345')
		self.user.save()
		self.logged=self.client.login(username='testuser', password='12345')

		response = self.client.get(reverse('home_view'))
		self.assertEquals(response.status_code,302)


	def test_admin_click_view_without_authentication(self):
		response = self.client.get(reverse('admin_click'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/adminclick.html')




	def test_admin_view_with_authentication(self):
		self.user = User.objects.create(username='testuser')
		self.user.set_password('12345')
		self.user.save()
		self.logged=self.client.login(username='testuser', password='12345')

		response = self.client.get(reverse('admin_click'))
		self.assertEquals(response.status_code,302)


	def test_student_click_view_without_authentication(self):
		response = self.client.get(reverse('student_click'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/studentclick.html')

	def test_student_view_with_authentication(self):
		self.user = User.objects.create(username='testuser')
		self.user.set_password('12345')
		self.user.save()
		self.logged=self.client.login(username='testuser', password='12345')

		response = self.client.get(reverse('student_click'))
		self.assertEquals(response.status_code,302)


	def test_admin_signup_view_get(self):
		response = self.client.get(reverse('admin_signup'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/adminsignup.html')


	def test_admin_signup_view_post(self):
		form =  AdminSigupForm(data={'first_name':'test_first_name','last_name':'test_last_name','username':'testusername','password':'testpass'})

		self.assertTrue(form.is_valid())



	def test_student_signup_view_get(self):
		response = self.client.get(reverse('student_signup'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/studentsignup.html')

	def test_student_signup_view_post(self):
		form1=StudentUserForm(data={
			'first_name':'test_firstname',
			'last_name':'test_lastname',
			'username':'testusername',
			'password':'testpass'})
		form2=StudentExtraForm(data={
    		'enrollment':'testenroll','branch':'testbranch'})
		self.assertTrue(form1.is_valid())
		self.assertTrue(form2.is_valid())



	def test_admin_login_get(self):
		response = self.client.get(reverse('adminlogin'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/adminlogin.html')

	def test_student_login_get(self):
		response = self.client.get(reverse('studentlogin'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/studentlogin.html')



	def test_student_logout_view_get(self):
		response = self.client.get(reverse('logout_view'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/index.html')



	def test_admin_after_login_get(self):
		self.user = User.objects.create(username='testuser')
		

		self.user.set_password('12345')
		self.user.save()
		

		self.logged=self.client.login(username='testuser', password='12345')
		Group.objects.create(name='ADMIN')
		mygroup=Group.objects.get(name='ADMIN')
		self.user.groups.add(mygroup)

		response = self.client.get(reverse('afterlogin'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/adminafterlogin.html')



	def test_student_after_login_get(self):
		self.user = User.objects.create(username='testuser',is_superuser=False,is_staff=False)
		self.user.set_password('12345')
		self.user.save()
		self.logged=self.client.login(username='testuser', password='12345')

		response = self.client.get(reverse('afterlogin'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/studentafterlogin.html')


	def test_addbook_view_get(self):
		self.user = User.objects.create(username='testuser')
		self.user.set_password('12345')
		self.user.save()
		
		self.logged=self.client.login(username='testuser', password='12345')
		Group.objects.create(name='ADMIN')
		mygroup=Group.objects.get(name='ADMIN')
		self.user.groups.add(mygroup)
		response = self.client.get(reverse('addbook'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/addbook.html')


	def test_viewbook_view_get(self):
		self.user = User.objects.create(username='testuser')
		self.user.set_password('12345')
		self.user.save()
		
		self.logged=self.client.login(username='testuser', password='12345')
		Group.objects.create(name='ADMIN')
		mygroup=Group.objects.get(name='ADMIN')
		self.user.groups.add(mygroup)
		response = self.client.get(reverse('viewbook'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/viewbook.html')


	def test_issuebook_view_get(self):
		self.user = User.objects.create(username='testuser')
		self.user.set_password('12345')
		self.user.save()
		
		self.logged=self.client.login(username='testuser', password='12345')
		Group.objects.create(name='ADMIN')
		mygroup=Group.objects.get(name='ADMIN')
		self.user.groups.add(mygroup)
		response = self.client.get(reverse('issuebook'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/issuebook.html')



	def test_issuebook_view_post(self):
		self.user = User.objects.create(username='testuser')
		self.user.set_password('12345')
		self.user.save()
		
		self.logged=self.client.login(username='testuser', password='12345')
		Group.objects.create(name='ADMIN')
		mygroup=Group.objects.get(name='ADMIN')
		self.user.groups.add(mygroup)
		std=StudentExtra.objects.create(user=self.user,enrollment='testenroll',branch='testbranch')
		book_inst=Book.objects.create(name='testbook',isbn=1234,author='testauthor',category='Education')
		form=IssuedBookForm(data={
			'isbn2':book_inst,
			'enrollment2':std

			})
		

		self.assertTrue(form.is_valid())



	def test_issuedbook_view_post(self):
		self.user = User.objects.create(username='testuser')
		self.user.set_password('12345')
		self.user.save()
		
		self.logged=self.client.login(username='testuser', password='12345')
		Group.objects.create(name='ADMIN')
		mygroup=Group.objects.get(name='ADMIN')
		self.user.groups.add(mygroup)
		IssuedBook.objects.create(enrollment='testenroll',isbn=2334,issuedate='2021-05-18',expirydate='2021-06-18')
		std=StudentExtra.objects.create(user=self.user,enrollment='testenroll',branch='testbranch')
		book_inst=Book.objects.create(name='testbook',isbn=1234,author='testauthor',category='Education')
		
		response = self.client.get(reverse('issuedbook'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/viewissuedbook.html')



	def test_studentview_view_get(self):
		self.user = User.objects.create(username='testuser')
		self.user.set_password('12345')
		self.user.save()
		
		self.logged=self.client.login(username='testuser', password='12345')
		Group.objects.create(name='ADMIN')
		mygroup=Group.objects.get(name='ADMIN')
		self.user.groups.add(mygroup)
		IssuedBook.objects.create(enrollment='testenroll',isbn=2334,issuedate='2021-05-18',expirydate='2021-06-18')
		std=StudentExtra.objects.create(user=self.user,enrollment='testenroll',branch='testbranch')
		book_inst=Book.objects.create(name='testbook',isbn=1234,author='testauthor',category='Education')
		
		response = self.client.get(reverse('viewstudent'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/viewstudent.html')


	def test_issued_book_by_student_view_get(self):
		self.user = User.objects.create(username='testuser')
		self.user.set_password('12345')
		self.user.save()
		
		self.logged=self.client.login(username='testuser', password='12345')
		IssuedBook.objects.create(enrollment='testenroll',isbn=2334,issuedate='2021-05-18',expirydate='2021-06-18')
		std=StudentExtra.objects.create(user=self.user,enrollment='testenroll',branch='testbranch')
		book_inst=Book.objects.create(name='testbook',isbn=1234,author='testauthor',category='Education')
		
		response = self.client.get(reverse('issuedbystudent'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/viewissuedbookbystudent.html')


	def test_aboutus_view_get(self):
		response = self.client.get(reverse('aboutus'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/aboutus.html')


	def test_contactus_view_get(self):
		response = self.client.get(reverse('contactus'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'library/contactus.html')

	def test_contactus_view_post(self):

		form=ContactusForm(data={
			'Name':'testname',
			'Email':'test@testmail.com',
			'Message':'test message here'
			})


		self.assertTrue(form.is_valid())