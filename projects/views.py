from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from projects.serializers import UserSerializer, GroupSerializer, ProjectSerializer, UpdateSerializer
from projects.models import Project, Update

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProjectViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows projects to be viewed or edited.
	"""
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer

class UpdateViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows updates to be viewed or edited.
	"""

	queryset = Update.objects.all()
	serializer_class = UpdateSerializer

class UpdateListing(generics.ListAPIView):
	"""
	API endpoint that allows to retrieve the list of Updates of a given Project paginated by 5
	"""
	
	model = Update
	serializer_class = UpdateSerializer
	paginate_by = 5

	def get_queryset(self):
		pk = self.kwargs['pk']
		queryset = Update.objects.filter(proyecto=pk)
		return queryset