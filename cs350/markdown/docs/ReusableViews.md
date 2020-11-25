<!doctype html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>static/pages/cs350/docs/ReusableViews.html</title>
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
    &lt;title&gt;static/pages/cs350/docs/ReusableViews.html&lt;/title&gt;
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
    &lt;title&gt;static/pages/cs350/docs/ReusableViews.html&lt;/title&gt;
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
        
            &lt;h1 id=&quot;reusable-views&quot;&gt;Reusable Views&lt;/h1&gt;</code></pre>
<p>
The best way to build views quickly in Django is simply use view that someone else has implemented and debugged.
</p>
<hr />
<h2 id="generic-views">
Generic Views
</h2>
<h3 id="templateview">
TemplateView
</h3>
<p>
From <a href="https://docs.djangoproject.com/en/3.1/topics/class-based-views/">Class-based Views</a> <a href="https://docs.djangoproject.com/en/3.1/ref/class-based-views/base">Base Views</a>
</p>
<h4 id="template-in-urls.py">
Template in urls.py
</h4>
<p>
urls.py
</p>
<pre><code>from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(&#39;about/&#39;, TemplateView.as_view(template_name=&quot;about.html&quot;)),
]</code></pre>
<h4 id="subclass-templateview">
Subclass TemplateView
</h4>
<p>
urls.py
</p>
<pre><code>from django.urls import path
from some_app.views import AboutView

urlpatterns = [
    path(&#39;about/&#39;, AboutView.as_view()),
]</code></pre>
<p>
views.py
</p>
<pre><code>from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = &quot;about.html&quot;
 </code></pre>
<p>
templates/about.html
</p>
<pre><code>&lt;h1&gt;Shrinking World&lt;/h1&gt;
&lt;p&gt;
    Founded in 2007 to bring practical software development training to
    students everywhere.
&lt;/p&gt;</code></pre>
<h4 id="setting-data-in-views">
Setting Data in Views
</h4>
<p>
urls.py
</p>
<pre><code>from django.urls import path
from .views import MyStoryView

urlpatterns = [
    path(&#39;story&#39;, MyStoryView.as_view()),
]</code></pre>
<p>
views.py
</p>
<pre><code>from django.views.generic import TemplateView

class MyStoryView(TemplateView):
    template_name = &quot;story.html&quot;
    
    def get_context_data(self, **kwargs):
        return {
            &#39;title&#39;: &#39;Three Pigs&#39;, 
            &#39;body&#39;: &#39;Once upon a time ...&#39;,
        }
 </code></pre>
<p>
templates/story.html
</p>
<pre><code>&lt;h1&gt;{{ title }}&lt;/h1&gt;
&lt;p&gt;
    {{ body}}
&lt;/p&gt;</code></pre>
<h3 id="redirectview">
RedirectView
</h3>
<p>
urls.py
</p>
<pre><code>from django.urls import path
from .views import DirectoryIndexView, RandomRedirectView

urlpatterns = [
    path(&#39;directory/&#39;, DirectoryIndexView.as_view()),
    path(&#39;random&#39;, RandomRedirectView.as_view()),
]</code></pre>
<p>
views.py
</p>
<pre><code>from django.views.generic import RedirectView

class DirectoryIndexView(RedirectView):
    url = &quot;directory/index.html&quot;
    
class RandomRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        article = choice ([
            &#39;http://google.com&#39;, 
            &#39;http://amazon.com&#39;, 
            &#39;http://facebook.com&#39;,
        ])
        return article</code></pre>
<h3 id="createview">
CreateView
</h3>
<h3 id="updateview">
UpdateView
</h3>
<h3 id="detailview">
DetailView
</h3>
<h3 id="listview">
ListView
</h3>
<h3 id="deleteview">
DeleteView
</h3>
<hr />
<h2 id="shrinking-world-page-layout">
Shrinking World Page Layout
</h2>
<h3 id="page-view">
Page View
</h3>
<h3 id="page-view-1">
Page View
</h3>
<h3 id="noteviewset">
NoteViewSet
</h3>
<h3 id="outlinedisplayview">
OutlineDisplayView
</h3>
<hr />
<h2 id="shrinking-world-component-views">
Shrinking World Component Views
</h2>
<h3 id="documentview">
DocumentView
</h3>
<h3 id="docindexview">
DocIndexView
</h3>
<h3 id="textview">
TextView
</h3>
<h3 id="cardview">
CardView
</h3>
<h3 id="tabview">
TabView
</h3>
<h3 id="accordionview">
AccordionView
</h3>
<h3 id="tableview">
TableView
</h3>
<h3 id="galleryview">
GalleryView
</h3>
<h3 id="featuresview">
FeaturesView
</h3>
<h3 id="carouselview">
CarouselView
</h3>
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