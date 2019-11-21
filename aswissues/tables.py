import django_tables2 as tables
from .models import Issue
from django_tables2.utils import Accessor

class IssueTable(tables.Table):
    titol = tables.TemplateColumn('<a href= "./issue/{{record.id}}">{{record.titol}}</a>')
    Assignat = tables.TemplateColumn('<a href= "./?assignee={{record.assignee}}">{{record.assignee}}</a>')
    prioritat = tables.TemplateColumn('<a href= "./?prioritat={{record.prioritat}}">{{record.prioritat}}</a>')
    tipus = tables.TemplateColumn('<a href= "./?tipus={{record.tipus}}">{{record.tipus}}</a>')
    status = tables.TemplateColumn('<a href= "./?status={{record.status}}">{{record.status}}</a>')
    data_creacio = tables.TemplateColumn('<a href= "./?tidata_creacio={{record.data_creacio}}">{{record.data_creacio}}</a>')


    class Meta:
        model = Issue
        template_name = "django_tables2/bootstrap4.html"
        fields = ("titol", "tipus", "prioritat", "status", "Assignat", "data_creacio")
        per_page = 20
