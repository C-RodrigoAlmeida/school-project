import requests

headers = {"Authorization": "Token 264c186949728895f5759937e3416f7ac79d2958"}

base_url_courses = "http://localhost:8000/api/v2/courses/"
base_url_ratings = "http://localhost:8000/api/v2/ratings/"

new_course = {
    "title": "Testing insert",
    "url": "https://www.justtesting.com.br"
}

result = requests.post(url=base_url_courses, headers=headers, data=new_course)

assert result.status_code == 201

assert result.json()["title"] == new_course["title"]