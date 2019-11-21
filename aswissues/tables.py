import django_tables2 as tables
from .models import Issue, Vote, Watch
from django_tables2.utils import Accessor

class IssueTable(tables.Table):

    titol = tables.TemplateColumn('<a href= "./issue/{{record.id}}">{{record.titol}}</a>')
    Assignat = tables.TemplateColumn('<a href= "./?assignee={{record.assignee.id}}">{{record.assignee}}</a>')
    prioritat = tables.TemplateColumn('<a href= "./?prioritat={{record.prioritat}}">{{record.prioritat}}</a>')
    tipus = tables.TemplateColumn('<a href= "./?tipus={{record.tipus}}">{{record.tipus}}</a>')
    status = tables.TemplateColumn('<a href= "./?status={{record.status}}">{{record.status}}</a>')
    data_creacio = tables.TemplateColumn('<a href= "./?data_creacio={{record.data_creacio}}">{{record.data_creacio}}</a>')
    votes = tables.Column(empty_values=(), verbose_name="Vots")
    watchers = tables.Column(empty_values=(), verbose_name= "Watching?")

    
    def render_votes(self, value, record):
        return Vote.objects.filter(issue=record).count()

    def render_watchers(self, value, record):
        if self.request.user.is_authenticated:
            if Watch.objects.filter(issue=record, watcher=self.request.user).count() > 0: return "Sí"
        return "No"

    class Meta:
        model = Issue
        template_name = "django_tables2/bootstrap4.html"
        fields = ("titol", "tipus", "prioritat", "status", "Assignat", "votes", "data_creacio", "watchers")
        per_page = 20
