<!doctype html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>static/pages/cs350/docs/DjangoDataViews.html</title>
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
    &lt;title&gt;static/pages/cs350/docs/DjangoDataViews.html&lt;/title&gt;
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
    &lt;title&gt;static/pages/cs350/docs/DjangoDataViews.html&lt;/title&gt;
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
        
            &lt;h1 id=&quot;design-pattern---django-data-views&quot;&gt;Design Pattern - Django Data Views&lt;/h1&gt;</code></pre>
<p>
Build generic views to do all of the CRUD operations
</p>
<h3 id="django-view-classes">
Django View Classes
</h3>
<p>
Django defines a number of general purpose view classes. Each of these classes define the common behavoir for views.
</p>
<p>
Each view can be implmented in its simplest form with just a few lines of code. Then the view can be customized as much as needed.
</p>
<ul>
<li>
TemplateView
</li>
<li>
ListView
</li>
<li>
DetailView
</li>
<li>
CreateView
</li>
<li>
UpdateView
</li>
<li>
DeleteView
</li>
</ul>
<h3 id="superhero-example">
SuperHero Example
</h3>
<p>
Here is a very simple example that shows little customization.
</p>
<h3 id="define-python-class">
Define Python class
</h3>
<p>
Superhero (name, identity, image)
</p>
<p>
hero/models.py
</p>
<pre><code>class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
    image = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self): 
        return reverse(&#39;home&#39;, args=[str(self.id)])</code></pre>
<h3 id="templateview">
TemplateView
</h3>
<p>
templates/hero_detail.html
</p>
<pre><code>&lt;h1&gt;{{ title }}&lt;/h1&gt;
&lt;p&gt;
    Hero Name: {{ hero.name }}
&lt;/p&gt;
&lt;p&gt;
    Secret Identify: {{ hero.identity }}
&lt;/p&gt;
&lt;p&gt;
    SHIELD Number: {{ hero.pk }}
&lt;/p&gt;</code></pre>
<p>
hero/views.py
</p>
<pre><code>from django.views.generic import TemplateView

class HeroView(TemplateView):
    template_name = &quot;hero_detail.html&quot;

    def get_context_data(self, **kwargs):
        heroes = Superhero.objects.get(pk=1)
        return {&#39;hero&#39;: hero}</code></pre>
<p>
hero/urls.py
</p>
<pre><code>from django.urls import path
from .views import HeroView

urlpatterns = [
    path(&#39;&#39;, HeroView.as_view(), name=&#39;home&#39;),
    path(&#39;&lt;str:identity&gt;&#39;, HeroView.as_view(), name=&#39;hero_detail&#39;),
]</code></pre>
<h3 id="listview">
ListView
</h3>
<ul>
<li>
Create a table or divs that show a list of records
</li>
<li>
Each hero should have a link that goes to the details page
</li>
</ul>
<p>
templates/hero_list.html
</p>
<pre><code>{% extends &#39;page_theme.html&#39; %}


{% block main %}

    &lt;h1&gt;Heroes Gallery&lt;/h1&gt;

    {% for hero in heroes %}

        &lt;h2&gt;Hero - {{ hero.name }}&lt;/h2&gt;
        &lt;p&gt;
            This page shows my favorite hero.
        &lt;/p&gt;
        &lt;p&gt;
            Secret ID: {{ hero.identity }}
        &lt;/p&gt;
        &lt;img width=&quot;300&quot; src=&quot;/static/images/{{ hero.name }}.jpg&quot; alt=&quot;{{ hero.identity }}&quot;&gt;

    {% endfor %}

{% endblock main %}</code></pre>
<p>
hero/views.py
</p>
<pre><code>from django.views.generic import ListView
from .models import Superhero

class HeroListView(ListView):
    template_name = &quot;hero_list.html&quot;
    model = Superhero</code></pre>
<p>
hero/urls.py
</p>
<pre><code>from django.urls import path
from hero.views import HeroView

urlpatterns = [
    path(&#39;&#39;, HeroListView.as_view(), name=&#39;hero_list&#39;),        
]</code></pre>
<h3 id="detailview">
DetailView
</h3>
<ul>
<li>
Display all info from the Database record
</li>
<li>
Show the image as a thumbnail with a link to the large image
</li>
<li>
Add a button to Edit the record
</li>
</ul>
<p>
templates/hero_detail.html
</p>
<pre><code>&lt;a href=&quot;/&quot;&gt;Hero List&lt;/a&gt;
&lt;h1&gt;{{ title }}&lt;/h1&gt;
&lt;p&gt;
    Hero Name: {{ hero.name }}
&lt;/p&gt;
&lt;p&gt;
    Secret Identify: {{ hero.identity }}
&lt;/p&gt;
&lt;p&gt;
    SHIELD Number: {{ hero.pk }}
&lt;/p&gt;</code></pre>
<p>
hero/views.py
</p>
<pre><code>from django.views.generic import DetailView

class HeroView(DetailView):
    template_name = &quot;hero_detail.html&quot;
    model = Superhero
    </code></pre>
<p>
hero/urls.py
</p>
<pre><code>from django.urls import path
from .views import HeroDetailView

urlpatterns = [
    path(&#39;&lt;int:pk&gt;&#39;, HeroDetailView.as_view(), name=&#39;hero_detail&#39;),        
]</code></pre>
<h3 id="createview">
CreateView
</h3>
<ul>
<li>
Create new records with a view
</li>
<li>
You can cheat by loading the image file into a directory
</li>
<li>
Add the image as a URL pointing to this file
</li>
</ul>
<p>
templates/hero_add.html
</p>
<pre><code>{% extends &#39;page_theme.html&#39; %}

{% block content %}

    &lt;h1&gt;New Hero&lt;/h1&gt;

    &lt;form action=&quot;&quot; method=&quot;post&quot;&gt;{% csrf_token %}
        {{ form.as_p }}
        &lt;input type=&quot;submit&quot; value=&quot;Save&quot;&gt;
    &lt;/form&gt;

{% endblock content %}</code></pre>
<p>
hero/views.py
</p>
<pre><code>from django.views.generic.edit import CreateView
from .models import Superhero

class HeroAddView(CreateView):
    template_name = &quot;hero_add.html&quot;
    model = Superhero
    fields = &#39;__all__&#39;</code></pre>
<p>
hero/urls.py
</p>
<pre><code>from django.urls import path
from .views import HeroAddView

urlpatterns = [
    path(&#39;&lt;int:pk&gt;&#39;, HeroAddView.as_view(), name=&#39;hero_add&#39;),        
]</code></pre>
<h3 id="updateview">
UpdateView
</h3>
<ul>
<li>
Make sure that you can edit the records
</li>
<li>
Make sure that the page is redirected after save
</li>
</ul>
<p>
templates/hero_edit.html
</p>
<pre><code>{% extends &#39;page_theme.html&#39; %}

{% block content %}

    &lt;h1&gt;Edit Hero&lt;/h1&gt;

    &lt;form action=&quot;&quot; method=&quot;post&quot;&gt;{% csrf_token %}
        {{ form.as_p }}
        &lt;input type=&quot;submit&quot; value=&quot;Save&quot;&gt;
    &lt;/form&gt;

{% endblock content %}</code></pre>
<p>
hero/views.py
</p>
<pre><code>from django.views.generic.edit import CreateView
from .models import Superhero

class HeroEditView(CreateView):
    template_name = &quot;hero_edit.html&quot;
    model = Superhero
    fields = &#39;__all__&#39;</code></pre>
<p>
hero/urls.py
</p>
<pre><code>from django.urls import path
from .views import HeroAddView, HeroEditView

urlpatterns = [
    path(&#39;&lt;int:pk&gt;&#39;,  HeroAddView.as_view(),    name=&#39;hero_add&#39;),        
    path(&#39;&lt;int:pk&gt;/&#39;, HeroUpdateView.as_view(), name=&#39;hero_edit&#39;),
]</code></pre>
<h3 id="deleteview">
DeleteView
</h3>
<ul>
<li>
Delete the records after confirmation
</li>
<li>
Go to the list after a delete
</li>
</ul>
<p>
templates/hero_delete.html
</p>
<pre><code>{% extends &#39;page_theme.html&#39; %}

{% block content %}

    &lt;h1&gt;Delete Hero?&lt;/h1&gt;

    &lt;form action=&quot;&quot; method=&quot;post&quot;&gt;{% csrf_token %}
        &lt;p&gt;Are you sure you want to delete &quot;{{ hero.name }}&quot;?&lt;/p&gt;
        &lt;input type=&quot;submit&quot; value=&quot;Confirm&quot;&gt;
    &lt;/form&gt;

{% endblock content %}</code></pre>
<p>
hero/views.py
</p>
<pre><code>from django.urls import reverse_lazy 
from django.views.generic.edit import DeleteView
from .models import Superhero

class HeroDeleteView(DeleteView):
    template_name = &quot;hero_delete.html&quot;
    model = Superhero
    success_url = reverse_lazy(&#39;hero_list&#39;)
    </code></pre>
<p>
hero/urls.py
</p>
<pre><code>from django.urls import path
from .views import HeroAddView, HeroDetailView, HeroEditView, HeroListView, HeroUpdateView

urlpatterns = [
    path(&#39;&#39;,          HeroListView.as_view(),   name=&#39;hero_list&#39;),
    path(&#39;add&#39;,       HeroAddView.as_view(),    name=&#39;hero_add&#39;),        
    path(&#39;&lt;int:pk&gt;&#39;,  HeroDetailView.as_view(), name=&#39;hero_detail&#39;),
    path(&#39;&lt;int:pk&gt;/&#39;, HeroUpdateView.as_view(), name=&#39;hero_edit&#39;),
    path(&#39;&lt;int:pk&gt;/delete&#39;, HeroDeleteView.as_view(), name=&#39;hero_delete&#39;),
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