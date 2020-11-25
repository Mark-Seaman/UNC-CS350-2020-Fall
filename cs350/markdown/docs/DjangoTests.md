<!doctype html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>static/pages/cs350/docs/DjangoTests.html</title>
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
    &lt;title&gt;static/pages/cs350/docs/DjangoTests.html&lt;/title&gt;
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
    &lt;title&gt;static/pages/cs350/docs/DjangoTests.html&lt;/title&gt;
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
        
            &lt;h1 id=&quot;django-tests&quot;&gt;Django Tests&lt;/h1&gt;</code></pre>
<p>
Django is a web framework for perfectionists with deadlines. It comes with batteries included.
</p>
<p>
One of the huge benefits of using Django is the direct support for testing via the test framework.
</p>
<h3 id="defining-tests">
Defining Tests
</h3>
<p>
Here is a simple test that fetches the root page of this site and checks for a status code of 200.
</p>
<p>
book/tests.py
</p>
<pre><code>from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get(&#39;/&#39;)
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(&#39;/book_list.html&#39;)
        self.assertEqual(response.status_code, 200)</code></pre>
<p>
Create a test class that inherits from <strong>SimpleTest</strong>. This makes you test visible to Django test. It will be automatically executed from that point.
</p>
<p>
Define a series of specific tests as methods within the SimpleTest class. These methods start with <strong>test_</strong>.
</p>
<p>
Fetch web pages from your app by calling &quot;self.client.get&quot;. This performs an HTTP GET operation for the requested page. For example, &quot;/&quot; or &quot;/book_list.html&quot;.
</p>
<p>
Look in the response for the &quot;status_code&quot; and make sure that it is &quot;200&quot;.
</p>
<h3 id="running-tests">
Running Tests
</h3>
<p>
A django script runs all of the tests defined inside all of the installed apps within the project.
</p>
<pre><code>python manage.py test</code></pre>
<p>
If any test fails the reason is shown so that it can be quickly fixed. A good test is two or three lines of code that tests one thing. Writing simple tests makes it easy to produce test code and maintain it.
</p>
<p>
Tests should be run before committing code. Tests should be written before writing code.
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
<h3 id="book-builder-tests">
Book Builder Tests
</h3>
<p>
On Book Builder we will write tests that make page requests for each view in our project. These will be written as we create views to remove any development burden. Each test will check to make sure that the page is available and that the correct HTML template is used.
</p>
<ul>
<li>
See code for <a href="https://github.com/Mark-Seaman/Book-Builder/tree/master/bookbuilder/book/tests.py">Book Builder Tests</a>
</li>
<li>
Link to <a href="https://github.com/Mark-Seaman/Book-Builder/tree/master/docs/plan/Milestone-2/Code.md">Code for Book Builder</a>
</li>
</ul>
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