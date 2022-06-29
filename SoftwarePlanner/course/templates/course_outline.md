{{ course }}

LESSON PLAN
{% autoescape off %}{% for i in lessons %}
    Lesson {{ i.lesson }} - {{ i.date }}
    
        {{ i.title }}
        lesson url: {{ i.url }}
        Project #{{ i.milestone }}
            {% if i.details %}{{ i.details }}{% endif %}
    {% endfor %}
{% endautoescape %}


