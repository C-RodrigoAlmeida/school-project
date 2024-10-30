import requests

headers = {"Authorization": "Token 264c186949728895f5759937e3416f7ac79d2958"}

base_url_courses = "http://localhost:8000/api/v2/courses/"
base_url_ratings = "http://localhost:8000/api/v2/ratings/"

result = requests.delete(url=f"{base_url_courses}6/", headers=headers)

assert result.status_code == 204