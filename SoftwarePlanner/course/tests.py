from django.test import SimpleTestCase, TestCase
from requests import get

from tool.document import fix_images, text_to_html
from tool.files import line_count, recursive_files, write_file
from tool.text import text_join


class CourseTests(TestCase):
    '''
    These tests verify the integrity of the views that do not rely on the
    data from the server.  All views that do not access the database can
    be tested here to ensure:

        Page exists at URL route
        Page content
        Template used
        Page redirect

    These test create a test database and get pages using the Django test
    client.
    '''

    def test_root(self):
        response = self.client.get('/course')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'page_theme.html')
        self.assertContains(response, 'Teaching Philosophy')

    def test_bacs200(self):
        response = self.client.get('/course/bacs200')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_theme.html')

    def test_lessons(self):
        response = self.client.get('/course/bacs200/lesson/Index')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_theme.html')

    def test_lesson_redirect(self):
        response = self.client.get('/course/bacs200/lesson/01')
        self.assertRedirects(response, '/static/pages/bacs200/lesson/01.html', 302, 404)

    def test_static_lesson(self):
        response = get('https://shrinking-world.com/static/pages/bacs200/lesson/01.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Lesson 2', response.text)


class RepoTests(SimpleTestCase):
    '''
    These tests verify the integrity of the views that are hosted on an
    web server.  All views may access the database since there is no direct
    link from the test to the database.

    Views can be tested here to ensure:

        Page exists at URL route
        Page content
        Template used
        Page redirect
        Page size in characters

    Tests require 'requests' client to succeed. Django client gets a 404 or a
    database not allowed error.
    '''

    def assertSize(self, response, min, max):
        num = len(response.text)
        self.assertTrue(min <= num and num <= max,
                        f'{num} is out of range; should be between {min} and {max}')

    def test_repo_exists(self):
        response = self.client.get('https://github.com/Mark-Seaman/UNC-CS-350')
        self.assertEqual(response.status_code, 200)

    def test_repo_code(self):
        response = get('https://github.com/Mark-Seaman/UNC-CS-350/blob/master/cs350/index.html')
        self.assertEqual(response.status_code, 200)

    def test_page_request(self):
        response = get('https://github.com/Mark-Seaman/UNC-CS-350/blob/master/cs350/index.html')
        self.assertSize(response, 600000, 700000)
        self.assertIn('UNC CS 350', response.text)

    # def test_sensei_lessons_index(self):
    #     response = get('https://shrinking-world.com/course/bacs200/lesson/Index')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('href="/course/bacs200/lesson/Index"', response.text)
    #     self.assertIn('href="01"', response.text)
    #     self.assertIn('href="../slides/01"', response.text)
    #     self.assertIn('href="lecture/01.html"', response.text)
    #     self.assertSize(response, 73932, 89468)

    def test_lesson_page(self):
        response = get('https://shrinking-world.com/static/pages/bacs200/lesson/01.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>Lesson #1</title>', response.text)
        self.assertIn('Lesson 1', response.text)
        self.assertSize(response, 7900, 8000)

    def test_lecture_page(self):
        response = get('https://shrinking-world.com/static/pages/bacs200/lecture/01.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>Table of Contents</title>', response.text)
        self.assertIn('Shrinking World Training', response.text)
        self.assertSize(response, 6000, 6100)

    def test_project_page(self):
        '''
        Must use TestCase and 'requests' client to prevent test failure.
        '''
        response = get('https://shrinking-world.com/static/pages/bacs200/project/05.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>Project #5</title>', response.text)
        self.assertIn('Web Pages with HTML/CSS', response.text)
        self.assertSize(response, 4700, 4800)

    def test_demo_page(self):
        '''
        Must use TestCase and 'requests' client to prevent test failure.
        '''
        response = get('https://shrinking-world.com/static/pages/bacs200/demo/index.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>BACS 200 Demo Code</title>', response.text)
        self.assertIn('Weekly Projects', response.text)
        self.assertSize(response, 849, 849)


class WebsiteTests(TestCase):
    '''
    These tests verify the integrity of the static web pages that are
    generated for the courses supported.  The generated files are tested
    directly.
    '''

    def assertFileLines(self, path, num_files):
        self.assertEqual(line_count(path), num_files)

    def assertFileCount(self, path, num_files):
        self.assertFileLines(path, num_files)

    def saveFileList(self, course):
        files = sorted(recursive_files(f'static/pages/{course}'))
        path = f'Documents/info/Test/course_{course}_files'
        write_file(path, text_join(files))
        return path

    def test_create_bacs200(self):
        course = 'bacs200'
        path = self.saveFileList(course)
        self.assertFileCount(path, 384)

    def test_create_bacs350(self):
        course = 'bacs350'
        path = self.saveFileList(course)
        self.assertFileCount(path, 1170)

    def test_create_cs350(self):
        course = 'cs350'
        path = self.saveFileList(course)
        self.assertFileCount(path, 603)

    def test_image_path(self):
        text = '''### Web Servers
Web servers respond

![](img/WebServer.png)
        '''
        html = text_to_html(fix_images(text, '../lesson/img'))
        self.assertIn('<img src="../lesson/img/WebServer.png" />', html)
        self.assertIn('<h3 id="web-servers">Web Servers</h3>', html)

