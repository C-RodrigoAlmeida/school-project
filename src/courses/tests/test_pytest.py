import requests

class CourseTest:
    headers = {"Authorization": "Token 264c186949728895f5759937e3416f7ac79d2958"}
    url = "http://127.0.0.1:8000/api/v2/courses"

    def test_get_courses(self):
        assert requests.get(url=self.url, headers=self.headers).status_code == 200

    def test_get_course(self):

        assert requests.get(url=f"{self.url}6/", headers=self.headers) == 200

    def test_post_courses(self):
        data = {
            "title": "test master",
            "url": "https://www.testmaster.com"
        }
        assert requests.post(url=self.url, headers=self.headers, data=data) == 201

    def test_put_course(self):
        data = {
            "title": "test master up",
            "url": "https://www.testmasterup.com"
        }
        assert requests.post(url=f"{self.url}6/", headers=self.headers, json=data) == 200
    
    def test_delete_course(self):
        assert requests.delete(url=f"{self.url}6/", headers=self.headers)