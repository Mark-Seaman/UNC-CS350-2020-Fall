<!doctype html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>static/pages/cs350/docs/TestDriven.html</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
              integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z"
              crossorigin="anonymous">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css"
              integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp"
              crossorigin="anonymous">
        
    <link rel="stylesheet" href="../unc.css">

    </head>

    <body>

        
            

    <nav class="navbar navbar-expand-sm navbar-dark bg-dark">

        <div class="container">

            <button class="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarCollapse">
                <a href="https://shrinking-world.com" class="navbar-brand">Shrinking World</a>

                <ul class="navbar-nav ml-auto">

                    
                        <li class="nav-item ">
                            <a href="https://markseaman.org" class="nav-link">Mark Seaman</a>
                        </li>
                    
                        <li class="nav-item ">
                            <a href="https://seamanslog.com" class="nav-link">Blog</a>
                        </li>
                    
                        <li class="nav-item ">
                            <a href="https://shrinking-world.com/course" class="nav-link">Courses</a>
                        </li>
                    
                        <li class="nav-item ">
                            <a href="https://shrinking-world.com/book" class="nav-link">Books</a>
                        </li>
                    

                </ul>

                <ul class="navbar-nav ml-auto">
    
        <li
                
                    class="nav-item mr-3"
                
        >
            <a class="nav-link" href="/course//register">
                <i class="fas fa-user-plus"></i> Register</a>
        </li>
        <li
                
                    class="nav-item mr-3"
                
        >
            <a class="nav-link" href="/course//login">
                <i class="fas fa-sign-in-alt"></i>

                Login</a>
        </li>
    
</ul>

            </div>
        </div>

    </nav>



            

    <header class="p-lg-5">
        <div class="row media">
            <div class="media-body">
                <h1 class="display-4 ml-5">
                    <a href="../lesson/02.html">UNC BACS 200</a>
                </h1>
                <h2 class="display-6 ml-5">Web Dev Intro</h2>
            </div>
            <img class="m-3 rounded-circle image-fluid" src="../lesson/img/Bear.png" alt="Logo" width="150">
        </div>
    </header>



            

    <main>
        <div class="container">
            
                <!doctype html>
<html lang="en">
<pre><code>&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot;
          content=&quot;width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0&quot;&gt;
    &lt;meta http-equiv=&quot;X-UA-Compatible&quot; content=&quot;ie=edge&quot;&gt;
    &lt;title&gt;static/pages/cs350/docs/TestDriven.html&lt;/title&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css&quot;
          integrity=&quot;sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z&quot;
          crossorigin=&quot;anonymous&quot;&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://use.fontawesome.com/releases/v5.0.13/css/all.css&quot;
          integrity=&quot;sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp&quot;
          crossorigin=&quot;anonymous&quot;&gt;
    
&lt;link rel=&quot;stylesheet&quot; href=&quot;../unc.css&quot;&gt;

&lt;/head&gt;

&lt;body&gt;




&lt;nav class=&quot;navbar navbar-expand-sm navbar-dark bg-dark&quot;&gt;

    &lt;div class=&quot;container&quot;&gt;

        &lt;button class=&quot;navbar-toggler&quot; data-toggle=&quot;collapse&quot; data-target=&quot;#navbarCollapse&quot;&gt;
            &lt;span class=&quot;navbar-toggler-icon&quot;&gt;&lt;/span&gt;
        &lt;/button&gt;

        &lt;div class=&quot;collapse navbar-collapse&quot; id=&quot;navbarCollapse&quot;&gt;
            &lt;a href=&quot;https://shrinking-world.com&quot; class=&quot;navbar-brand&quot;&gt;Shrinking World&lt;/a&gt;

            &lt;ul class=&quot;navbar-nav ml-auto&quot;&gt;


                    &lt;li class=&quot;nav-item &quot;&gt;
                        &lt;a href=&quot;https://markseaman.org&quot; class=&quot;nav-link&quot;&gt;Mark Seaman&lt;/a&gt;
                    &lt;/li&gt;
                
                    &lt;li class=&quot;nav-item &quot;&gt;
                        &lt;a href=&quot;https://seamanslog.com&quot; class=&quot;nav-link&quot;&gt;Blog&lt;/a&gt;
                    &lt;/li&gt;
                
                    &lt;li class=&quot;nav-item &quot;&gt;
                        &lt;a href=&quot;https://shrinking-world.com/course&quot; class=&quot;nav-link&quot;&gt;Courses&lt;/a&gt;
                    &lt;/li&gt;
                
                    &lt;li class=&quot;nav-item &quot;&gt;
                        &lt;a href=&quot;https://shrinking-world.com/book&quot; class=&quot;nav-link&quot;&gt;Books&lt;/a&gt;
                    &lt;/li&gt;
                

            &lt;/ul&gt;

            &lt;ul class=&quot;navbar-nav ml-auto&quot;&gt;

    &lt;li
            
                class=&quot;nav-item mr-3&quot;
            
    &gt;
        &lt;a class=&quot;nav-link&quot; href=&quot;/course//register&quot;&gt;
            &lt;i class=&quot;fas fa-user-plus&quot;&gt;&lt;/i&gt; Register&lt;/a&gt;
    &lt;/li&gt;
    &lt;li
            
                class=&quot;nav-item mr-3&quot;
            
    &gt;
        &lt;a class=&quot;nav-link&quot; href=&quot;/course//login&quot;&gt;
            &lt;i class=&quot;fas fa-sign-in-alt&quot;&gt;&lt;/i&gt;

            Login&lt;/a&gt;
    &lt;/li&gt;</code></pre>
</ul>
<pre><code>        &lt;/div&gt;
    &lt;/div&gt;

&lt;/nav&gt;





&lt;header class=&quot;p-lg-5&quot;&gt;
    &lt;div class=&quot;row media&quot;&gt;
        &lt;div class=&quot;media-body&quot;&gt;
            &lt;h1 class=&quot;display-4 ml-5&quot;&gt;
                &lt;a href=&quot;../lesson/02.html&quot;&gt;UNC BACS 200&lt;/a&gt;
            &lt;/h1&gt;
            &lt;h2 class=&quot;display-6 ml-5&quot;&gt;Web Dev Intro&lt;/h2&gt;
        &lt;/div&gt;
        &lt;img class=&quot;m-3 rounded-circle image-fluid&quot; src=&quot;../lesson/img/Bear.png&quot; alt=&quot;Logo&quot; width=&quot;150&quot;&gt;
    &lt;/div&gt;
&lt;/header&gt;





&lt;main&gt;
    &lt;div class=&quot;container&quot;&gt;
        
            &lt;!doctype html&gt;</code></pre>
<html lang="en">
<pre><code>&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot;
          content=&quot;width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0&quot;&gt;
    &lt;meta http-equiv=&quot;X-UA-Compatible&quot; content=&quot;ie=edge&quot;&gt;
    &lt;title&gt;static/pages/cs350/docs/TestDriven.html&lt;/title&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css&quot;
          integrity=&quot;sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z&quot;
          crossorigin=&quot;anonymous&quot;&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://use.fontawesome.com/releases/v5.0.13/css/all.css&quot;
          integrity=&quot;sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp&quot;
          crossorigin=&quot;anonymous&quot;&gt;
    
&lt;link rel=&quot;stylesheet&quot; href=&quot;../unc.css&quot;&gt;

&lt;/head&gt;

&lt;body&gt;




&lt;nav class=&quot;navbar navbar-expand-sm navbar-dark bg-dark&quot;&gt;

    &lt;div class=&quot;container&quot;&gt;

        &lt;button class=&quot;navbar-toggler&quot; data-toggle=&quot;collapse&quot; data-target=&quot;#navbarCollapse&quot;&gt;
            &lt;span class=&quot;navbar-toggler-icon&quot;&gt;&lt;/span&gt;
        &lt;/button&gt;

        &lt;div class=&quot;collapse navbar-collapse&quot; id=&quot;navbarCollapse&quot;&gt;
            &lt;a href=&quot;https://shrinking-world.com&quot; class=&quot;navbar-brand&quot;&gt;Shrinking World&lt;/a&gt;

            &lt;ul class=&quot;navbar-nav ml-auto&quot;&gt;


                    &lt;li class=&quot;nav-item &quot;&gt;
                        &lt;a href=&quot;https://markseaman.org&quot; class=&quot;nav-link&quot;&gt;Mark Seaman&lt;/a&gt;
                    &lt;/li&gt;
                
                    &lt;li class=&quot;nav-item &quot;&gt;
                        &lt;a href=&quot;https://seamanslog.com&quot; class=&quot;nav-link&quot;&gt;Blog&lt;/a&gt;
                    &lt;/li&gt;
                
                    &lt;li class=&quot;nav-item &quot;&gt;
                        &lt;a href=&quot;https://shrinking-world.com/course&quot; class=&quot;nav-link&quot;&gt;Courses&lt;/a&gt;
                    &lt;/li&gt;
                
                    &lt;li class=&quot;nav-item &quot;&gt;
                        &lt;a href=&quot;https://shrinking-world.com/book&quot; class=&quot;nav-link&quot;&gt;Books&lt;/a&gt;
                    &lt;/li&gt;
                

            &lt;/ul&gt;

            &lt;ul class=&quot;navbar-nav ml-auto&quot;&gt;

    &lt;li
            
                class=&quot;nav-item mr-3&quot;
            
    &gt;
        &lt;a class=&quot;nav-link&quot; href=&quot;/course//register&quot;&gt;
            &lt;i class=&quot;fas fa-user-plus&quot;&gt;&lt;/i&gt; Register&lt;/a&gt;
    &lt;/li&gt;
    &lt;li
            
                class=&quot;nav-item mr-3&quot;
            
    &gt;
        &lt;a class=&quot;nav-link&quot; href=&quot;/course//login&quot;&gt;
            &lt;i class=&quot;fas fa-sign-in-alt&quot;&gt;&lt;/i&gt;

            Login&lt;/a&gt;
    &lt;/li&gt;</code></pre>
</ul>
<pre><code>        &lt;/div&gt;
    &lt;/div&gt;

&lt;/nav&gt;





&lt;header class=&quot;p-lg-5&quot;&gt;
    &lt;div class=&quot;row media&quot;&gt;
        &lt;div class=&quot;media-body&quot;&gt;
            &lt;h1 class=&quot;display-4 ml-5&quot;&gt;
                &lt;a href=&quot;../lesson/02.html&quot;&gt;UNC BACS 200&lt;/a&gt;
            &lt;/h1&gt;
            &lt;h2 class=&quot;display-6 ml-5&quot;&gt;Web Dev Intro&lt;/h2&gt;
        &lt;/div&gt;
        &lt;img class=&quot;m-3 rounded-circle image-fluid&quot; src=&quot;../lesson/img/Bear.png&quot; alt=&quot;Logo&quot; width=&quot;150&quot;&gt;
    &lt;/div&gt;
&lt;/header&gt;





&lt;main&gt;
    &lt;div class=&quot;container&quot;&gt;
        
            &lt;h1 id=&quot;test-driven-development&quot;&gt;Test Driven Development&lt;/h1&gt;</code></pre>
<p>
Using TDD for Book Builder Data
</p>
<h3 id="test-driven-development-setup">
Test-driven Development Setup
</h3>
<ul>
<li>
Developer tools setup
</li>
<li>
Github Desktop
<ul>
<li>
View changes
</li>
<li>
Commit and changes
</li>
<li>
Pull new code
</li>
</ul>
</li>
<li>
Run Editor
<ul>
<li>
Use Open Folder in Brackets to remember code location
</li>
<li>
Remember last change made
</li>
</ul>
</li>
<li>
Run a terminal window
<ul>
<li>
Verify the virtual environment
</li>
<li>
Run the server
</li>
<li>
Test the code
</li>
<li>
Fix any errors
</li>
</ul>
</li>
</ul>
<h3 id="workflow-for-development">
Workflow for Development
</h3>
<ul>
<li>
Pull code
</li>
<li>
Feature Loop (focus on one feature)
<ul>
<li>
Create a failing test
</li>
<li>
Create the code to pass the test
</li>
<li>
Save the test code for later
</li>
<li>
Commit and push changes
</li>
<li>
Select next feature
</li>
</ul>
</li>
<li>
Run all tests
</li>
<li>
Fix all defects
</li>
<li>
Push code
</li>
</ul>
<h2 id="book-builder-data">
Book Builder Data
</h2>
<p>
Data Classes and database tables
</p>
<ul>
<li>
Reader
<ul>
<li>
user*
</li>
</ul>
</li>
<li>
Author
<ul>
<li>
user*
</li>
<li>
name
</li>
</ul>
</li>
<li>
Book
<ul>
<li>
author*
</li>
<li>
title
</li>
</ul>
</li>
<li>
Chapter
<ul>
<li>
book*
</li>
<li>
title
</li>
<li>
order
</li>
</ul>
</li>
<li>
Paragraph
<ul>
<li>
chapter*
</li>
<li>
text
</li>
<li>
order
</li>
</ul>
</li>
<li>
Image
<ul>
<li>
chapter*
</li>
<li>
src
</li>
<li>
alt
</li>
<li>
order
</li>
</ul>
</li>
</ul>
<p>
“*” makes a link to another table. This is implemented by a foreign key relationship between the two tables.
</p>
<p>
Example: Books have Authors so the Book data model has a ForeignKeyField that points to the Author Model class.
</p>
<h4 id="bookmodels.py">
book/models.py
</h4>
<p>
bookbuilder/settings.py
</p>
<pre><code>INSTALLED_APPS = [
    ...
    &#39;book&#39;,
]</code></pre>
<p>
book/models.py
</p>
<pre><code>from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Book(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)</code></pre>
<p>
Migrate the database
</p>
<pre><code>python manage.py makemigrations

python manage.py migrate</code></pre>
<p>
book/tests.py
</p>
<pre><code>class AuthorTests(TestCase):

    def test_author_model(self):
        self.assertEqual(len(Author.objects.all()), 0)</code></pre>
<p>
Test iterations
</p>
<p>
Test 1 - No Authors
</p>
<pre><code>self.assertEqual(len(Author.objects.all()), 0)</code></pre>
<p>
Test 2 - Create One Author
</p>
<pre><code>def test_create_author(self):
    user = get_user_model().objects.create_user(username=&#39;TEST_DUDE&#39;, email=&#39;me@here.com&#39;, password=&#39;secret&#39;)
    author = Author.objects.create(user=self.user, name=&#39;Charles Dickens&#39;)
    self.assertEqual(len(Author.objects.all()), 1)</code></pre>
<p>
Test 3 - Check Author Name
</p>
<pre><code>def setUp(self):
    self.user = get_user_model().objects.create_user(username=&#39;TEST_DUDE&#39;, email=&#39;me@here.com&#39;, password=&#39;secret&#39;)
    self.author = Author.objects.create(user=self.user, name=&#39;Charles Dickens&#39;)

def test_author_model(self):
    self.assertEqual(self.author.name, &#39;Charles Dickens&#39;)
    self.assertEqual(self.author.user.username, &#39;TEST_DUDE&#39;)</code></pre>
<p>
Test 4 - Add Author
</p>
<pre><code>    def test_create_author(self):
        self.assertEqual(len(Author.objects.all()), 1)
        a = Author.objects.create(user=self.user, name=&#39;Jack London&#39;)
        self.assertEqual(len(Author.objects.all()), 2)
        self.assertEqual(a.name, &#39;Jack London&#39;)
        self.assertEqual(a.user.username, &#39;TEST_DUDE&#39;)</code></pre>
<p>
Test 5 - List Authors
</p>
<pre><code>    def test_list_authors(self):
        self.assertEqual(len(Author.objects.all()), 1)
        self.assertEqual(Author.objects.get(name=&#39;Charles Dickens&#39;).name, &#39;Charles Dickens&#39;)</code></pre>
<p>
Test 6 - Update Author
</p>
<pre><code>    def test_update_author(self):
        a = Author.objects.get(pk=1)
        self.assertEqual(a.name, &#39;Charles Dickens&#39;)
        a.name = &#39;George Orwell&#39;
        a.save()
        a = Author.objects.get(pk=1)
        self.assertEqual(a.name, &#39;George Orwell&#39;)</code></pre>
<p>
Test 7 - Delete Author
</p>
<pre><code>    def test_delete_author(self):
        a = Author.objects.get(pk=1)
        a.delete()
        self.assertEqual(len(Author.objects.all()), 0)</code></pre>
<p>
Refactor
</p>
<p>
book/author.py
</p>
<pre><code>def add_author(user, name):
    return Author.objects.create(user=user, name=name)
    
def list_authors():
    return Author.objects.all()
    
def get_author(name):
    return Author.objects.get(name=name)
    
def delete_author(name):
    Author.objects.get(name=name).delete()</code></pre>
<p>
book/tests.py
</p>
<pre><code>def check_author_name(self, pk, name):
    a = Author.objects.get(pk=pk)
    self.assertEqual(a.name, name)
    
def check_author_user(self, pk, username):
    a = Author.objects.get(pk=pk)
    self.assertEqual(a.user.username, username)
    
def check_num_authors(self, num):
    self.assertEqual(len(list_authors()), num)
   
def create_test_user(self):
     self.user = get_user_model().objects.create_user(
        username=&#39;TEST_DUDE&#39;, 
        email=&#39;me@here.com&#39;, 
        password=&#39;secret&#39;
     )
    </code></pre>
<p>
Refactored Tests
</p>
<pre><code>def create_test_user():
    return get_user_model().objects.create_user(username=&#39;TEST_DUDE&#39;, email=&#39;me@here.com&#39;, password=&#39;secret&#39;)

class AuthorTests(TestCase):

    def check_author_name(self, pk, name):
        a = Author.objects.get(pk=pk)
        self.assertEqual(a.name, name)

    def check_author_user(self, pk, username):
        a = Author.objects.get(pk=pk)
        self.assertEqual(a.user.username, username)

    def check_num_authors(self, num):
        self.assertEqual(len(list_authors()), num)

    def setUp(self):
        self.user = create_test_user()
        self.author = add_author(self.user, &#39;Charles Dickens&#39;)

    def test_author_model(self):
        self.check_num_authors(1)
        self.check_author_name(1, &#39;Charles Dickens&#39;)
        self.check_author_user(1, &#39;TEST_DUDE&#39;)

    def test_create_author(self):
        self.check_num_authors(1)
        add_author(self.user, &#39;Jack London&#39;)
        self.check_author_name(2, &#39;Jack London&#39;)
        self.check_author_user(2, &#39;TEST_DUDE&#39;)
        self.check_num_authors(2)

    def test_list_authors(self):
        self.check_num_authors(1)
        self.assertEqual(get_author(&#39;Charles Dickens&#39;).pk, 1)

    def test_update_author(self):
        self.check_num_authors(1)
        a = get_author(&#39;Charles Dickens&#39;)
        a.name = &#39;George Orwell&#39;
        a.save()
        self.check_author_name(1, &#39;George Orwell&#39;)

    def test_delete_author(self):
        delete_author(&#39;Charles Dickens&#39;)
        self.check_num_authors(0)</code></pre>
<pre><code>    &lt;/div&gt;
&lt;/main&gt;





&lt;footer class=&quot;text-center m-5&quot;&gt;
    &amp;copy;2020 &lt;a href=&quot;https://shrinking-world.com&quot;&gt;Shrinking World&lt;/a&gt;
    - Practical Software Engineering

















&lt;/footer&gt;





    &lt;script src=&quot;https://code.jquery.com/jquery-3.5.1.slim.min.js&quot;
            integrity=&quot;sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj&quot;
            crossorigin=&quot;anonymous&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js&quot;
            integrity=&quot;sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN&quot;
            crossorigin=&quot;anonymous&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js&quot;
            integrity=&quot;sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV&quot;
            crossorigin=&quot;anonymous&quot;&gt;&lt;/script&gt;

&lt;/body&gt;</code></pre>
</html>
<pre><code>    &lt;/div&gt;
&lt;/main&gt;





&lt;footer class=&quot;text-center m-5&quot;&gt;
    &amp;copy;2020 &lt;a href=&quot;https://shrinking-world.com&quot;&gt;Shrinking World&lt;/a&gt;
    - Practical Software Engineering

















&lt;/footer&gt;





    &lt;script src=&quot;https://code.jquery.com/jquery-3.5.1.slim.min.js&quot;
            integrity=&quot;sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj&quot;
            crossorigin=&quot;anonymous&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js&quot;
            integrity=&quot;sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN&quot;
            crossorigin=&quot;anonymous&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js&quot;
            integrity=&quot;sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV&quot;
            crossorigin=&quot;anonymous&quot;&gt;&lt;/script&gt;

&lt;/body&gt;</code></pre>
</html>

            
        </div>
    </main>



            
                
    <footer class="text-center m-5">
        &copy;2020 <a href="https://shrinking-world.com">Shrinking World</a>
        - Practical Software Engineering

















    </footer>

            

        

        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
                integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
                crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"
                integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN"
                crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
                integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV"
                crossorigin="anonymous"></script>

    </body>
</html>