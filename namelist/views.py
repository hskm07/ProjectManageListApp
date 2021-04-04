from django.views import generic
from .forms import SearchForm
from .models import ProjectMember

class IndexView(generic.ListView):
    model = ProjectMember
    paginate_by = 5

    def get_context_data(self):
        """Create a context to pass to the template"""
        context = super().get_context_data()
        context['form'] =SearchForm(self.request.GET)
        return context
    
    def get_queryset(self):
        """create a projectmember_listを作成する"""
        form = SearchForm(self.request.GET)
        form.is_valid()

        """Get All member"""
        queryset = super().get_queryset()

        """Narrow down by project members"""
        project_member = form.cleaned_data['projectname']
        if project_member:
            queryset = queryset.filter(project=project_member)

        """Narrow down by department"""
        department = form.cleaned_data['department']
        if department:
            queryset = queryset.filter(department=department)

        return queryset
