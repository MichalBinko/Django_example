from django.test import TestCase
#import tasks_app.models
from  tasks_app.models import Task
from parameterized import parameterized
# Create your tests here.

class URLTests(TestCase):
    @parameterized.expand([
        ["/login/?login=/"],
        ["/login/"],
        ["/register/"]
        ])
    
    def test_testhomepage(self, address):
        self.address = address
        response = self.client.get(self.address)
        self.assertEqual(response.status_code, 200)

class TestAppModels(TestCase):
    def test_model_title(self):
        title = Task.objects.create(title = "test title create")
        #content = Task.objects.create(content = "this is content")
        self.assertEqual(str(title), "test title create")
    

    def test_model_description(self):
        description = Task.objects.create(description = "this is description")
        self.assertEqual(False, False)

