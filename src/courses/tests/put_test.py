import requests

headers = {"Authorization": "Token 264c186949728895f5759937e3416f7ac79d2958"}

base_url_courses = "http://localhost:8000/api/v2/courses/"
base_url_ratings = "http://localhost:8000/api/v2/ratings/"

updated_course = {
    "title": "Testing the test code",
    "url": "https://www.justtestingthetestcode.com.br"
}

result = requests.put(url=f"{base_url_courses}6/", headers=headers, json=updated_course)

print(result.json())

print(result.status_code)

assert result.status_code == 200

assert result.json()["title"] == updated_course["title"]