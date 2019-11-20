import django_tables2 as tables
from .models import Issue
from django_tables2.utils import Accessor

class IssueTable(tables.Table):
    titol = tables.TemplateColumn('<a href= "./issue/{{record.id}}">{{record.titol}}</a>')
    nameC = tables.Column(verbose_name='Creador', accessor=Accessor('creator.username'))
    nameA = tables.Column(verbose_name='Assignat a', accessor=Accessor('assignee.username'))
    class Meta:
        model = Issue
        template_name = "django_tables2/bootstrap.html"
        fields = ("titol", "tipus", "prioritat" ,"nameA", "nameC", "data_creacio" )