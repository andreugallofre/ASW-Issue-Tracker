import django_tables2 as tables
from .models import Issue, Vote, Watch
from django_tables2.utils import Accessor

class VotesColumn(tables.TemplateColumn):
    def render(self, record, table, value, bound_column, **kwargs):
            return(Vote.objects.filter(issue=record).count())

class WatchersColumn(tables.TemplateColumn):
    def render(self, record, table, value, bound_column, **kwargs):
            return(Watch.objects.filter(issue=record).count())


class IssueTable(tables.Table):

    titol = tables.TemplateColumn('<a href= "./issue/{{record.id}}">{{record.titol}}</a>')
    Assignat = tables.TemplateColumn('<a href= "./?assignee={{record.assignee}}">{{record.assignee}}</a>')
    prioritat = tables.TemplateColumn('<a href= "./?prioritat={{record.prioritat}}">{{record.prioritat}}</a>')
    tipus = tables.TemplateColumn('<a href= "./?tipus={{record.tipus}}">{{record.tipus}}</a>')
    status = tables.TemplateColumn('<a href= "./?status={{record.status}}">{{record.status}}</a>')
    data_creacio = tables.TemplateColumn('<a href= "./?data_creacio={{record.data_creacio}}">{{record.data_creacio}}</a>')
    votes = VotesColumn('<a href= "/"></a>')
    watchers = WatchersColumn('<a href= "/"></a>')

    class Meta:
        model = Issue
        template_name = "django_tables2/bootstrap4.html"
        fields = ("titol", "tipus", "prioritat", "status", "Assignat", "votes", "watchers", "data_creacio")
        per_page = 20
