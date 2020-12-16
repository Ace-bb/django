from django.test import TestCase

# Create your tests here.
import requests, pprint

response = requests.get('http://127.0.0.1:8087/teacher/types?action=get_all_teachers')
pprint.pprint(response.json())
from .models import Teachers

tea = Teachers.objects.values()
lis = list(tea)
print(lis)
from .models import Teachers

fil = {
    "action": "get_filter_teachers",
    "type": ["文学", "理学", "工学"]
}
# response = requests.get('http://127.0.0.1:8087/teacher/types?action=filter_teacher_type')
response = requests.post('http://127.0.0.1:8087/teacher/types', json=fil)
print("111")
pprint.pprint(response.json())
import requests, pprint

search_key = {
    "key_word": "文学"
}
response = requests.get('http://127.0.0.1:8087/teacher/search?key_word=文学')
pprint.pprint(response.json())

import requests, pprint

d = {
    "action": "get_teacher_detail_message",
    "id": "10002"
}
response = requests.post('http://127.0.0.1:8087/teacher/detail', json=d)
pprint.pprint(response.json())
