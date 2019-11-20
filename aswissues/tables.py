import django_tables2 as tables
from .models import Issue
from django_tables2.utils import Accessor

class IssueTable(tables.Table):
    titol = tables.TemplateColumn('<a href= "./issue/{{record.id}}">{{record.titol}}</a>')
    nameC = tables.Column(verbose_name='Creador', accessor=Accessor('creator.username'))
    nameA = tables.Column(verbose_name='Assignat a', accessor=Accessor('assignee.username'))
    prioritat = tables.TemplateColumn('<a href= "./?prioritat={{record.prioritat}}">{{record.prioritat}}</a>')
    tipus = tables.TemplateColumn('<a href= "./?tipus={{record.tipus}}">{{record.tipus}}</a>')
    status = tables.TemplateColumn('<a href= "./?tipus={{record.status}}">{{record.status}}</a>')
    # nameCr = tables.TemplateColumn('<a href= "./?creator='+nameC+'">'+nameC+'</a>')
    data_creacio = tables.TemplateColumn('<a href= "./?tidata_creacio={{record.data_creacio}}">{{record.data_creacio}}</a>')

    class Meta:
        model = Issue
        template_name = "django_tables2/bootstrap4.html"
        fields = ("titol", "tipus", "prioritat", "nameA", "nameC", 'status', "data_creacio")
        per_page = 20
