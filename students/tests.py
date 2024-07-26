from django.test import TestCase
from django.urls import reverse
from .models import Student

class StudentTests(TestCase):

    def setUp(self):
        self.student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            date_of_birth="2000-01-01",
            enrollment_date="2022-09-01"
        )

    def test_student_list_view(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_student_detail_view(self):
        response = self.client.get(reverse('student_detail', args=[self.student.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")
        self.assertTemplateUsed(response, 'students/student_detail.html')

    def test_student_create_view(self):
        response = self.client.post(reverse('student_create'), {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane.doe@example.com',
            'date_of_birth': '2001-01-01',
            'enrollment_date': '2022-09-02'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Student.objects.last().first_name, 'Jane')

    def test_student_update_view(self):
        response = self.client.post(reverse('student_update', args=[self.student.pk]), {
            'first_name': 'Johnny',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'date_of_birth': '2000-01-01',
            'enrollment_date': '2022-09-01'
        })
        self.assertEqual(response.status_code, 302)
        self.student.refresh_from_db()
        self.assertEqual(self.student.first_name, 'Johnny')

    def test_student_delete_view(self):
        response = self.client.post(reverse('student_delete', args=[self.student.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Student.objects.count(), 0)
