<!doctype html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>static/pages/cs350/docs/ViewPrototype.html</title>
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
    &lt;title&gt;static/pages/cs350/docs/ViewPrototype.html&lt;/title&gt;
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
    &lt;title&gt;static/pages/cs350/docs/ViewPrototype.html&lt;/title&gt;
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
        
            &lt;h1 id=&quot;prototype-views&quot;&gt;Prototype Views&lt;/h1&gt;</code></pre>
<p>
This simple application is used to illustrate the general flow of the views in the finished application. The main purpose of building a prototype app for the views is to have a robust conversation between the developers and the client.
</p>
<p>
A sketch (or wireframe diagram) is not real enough. And waiting for the real app to be built out introduces a huge delay in the project. To be useful the prototype must be both quick and realistic.
</p>
<ul>
<li>
Create an app to illustrate the views
</li>
<li>
Everything is fake
</li>
<li>
Views have no style
</li>
<li>
Show the user flow and navigation
</li>
<li>
Limit the time spend to 4 hours
</li>
<li>
Build a reusable app to show HTML files
</li>
</ul>
<p>
The prototype is a simple app that displays a series of HTML pages. Each page represents a view in the final application. Text is added to the view to illustrate the contents that will be in the view.
</p>
<p>
Hyperlinks are used to sequence between the views so that the client can evaluate the user experience that will be built out later in the project.
</p>
<h3 id="book-builder-app-views">
Book Builder App Views
</h3>
<p>
To illustrate how to build a view prototype let's look at the Book Builder project. There are a number of different views that will be built.
</p>
<ul>
<li>
Users
<ul>
<li>
Register Author
</li>
<li>
Register Reader
</li>
<li>
Login
</li>
<li>
Logout
</li>
</ul>
</li>
<li>
Books
<ul>
<li>
Create Book
</li>
<li>
List Books
</li>
<li>
Edit Book
</li>
<li>
Read Book
</li>
<li>
Delete Book
</li>
</ul>
</li>
<li>
Chapters
<ul>
<li>
New Chapter
</li>
<li>
Edit Chapter
</li>
<li>
Read Chapter
</li>
<li>
Delete Chapter
</li>
</ul>
</li>
</ul>
<p>
For each of these views we build the simplest possible HTML code that captures the essence of what will happen in the view. While the eventual view will be dynamically created we don't want to worry about any of that now.
</p>
<p>
We hard-code all text directly into the HTML templates so that we can get something that look real enough at a small fraction of the cost. Our goal is to spend no longer than 15 minutes per view created.
</p>
<h3 id="book-builder-view-templates">
Book Builder View Templates
</h3>
<p>
Visit the <a href="https://github.com/Mark-Seaman/Book-Builder/tree/master/bookbuilder/templates">View Templates</a> to see the implementation of the book builder prototype.
</p>
<p>
List of HTML files
</p>
<pre><code>delete_book.html
delete_chapter.html
edit_book.html
edit_chapter.html
index.html
list_books.html
login.html
logout.html
missing.html
read_book.html
read_chapter.html
register_author.html
register_reader.html</code></pre>
<h3 id="template-pages-viewer">
Template Pages Viewer
</h3>
<p>
Use one URL Route to load different Page Templates. The following code snippets show how to get pages displayed directly from HTML files for Django apps.
</p>
<h4 id="pagesviews.py">
pages/views.py
</h4>
<pre><code>from django.views.generic import TemplateView

class PageView(TemplateView):

    def get_template_names(self):
        template_name = self.kwargs.get(&#39;template&#39;)
        return template_name
    </code></pre>
<h4 id="urls.py">
urls.py
</h4>
<pre><code>from django.urls import path
from page.views import PageView

urlpatterns = [
    path(&#39;&lt;str:template&gt;&#39;, PageView.as_view()),
]</code></pre>
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