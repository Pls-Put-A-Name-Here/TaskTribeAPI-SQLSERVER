from django.db import connection
from rest_framework import viewsets
from .models import Project, ProjectDetails, ProjectTeam, ProjectDetail
from .serializers import ProjectSerializer, ProjectDetailsSerializer, ProjectTeamSerializer, ProjectDetailSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response

class ProjectDetailsAPIView(APIView):
    @extend_schema(responses=ProjectDetailsSerializer(many=True))
    def get(self, request,pk=None):
        # Use a database connection cursor to execute the stored procedure
        with connection.cursor() as cursor:
            if pk is not None:
                cursor.execute("EXEC GetProjectDetailsById @ProjectID=%s", [pk])
            else:
                cursor.execute("EXEC GetProjectDetails")

            # Fetch the results from the cursor
            results = cursor.fetchall()

        # Manually match tuples to serializer fields
        results_list = []
        for result in results:
            result_dict = {
                'ProjectID': result[0],  # Assuming ProjectID is the first column in the result set
                'ProjectName': result[1],  # Assuming ProjectName is the second column
                'ProjectTeamName': result[2],  # Assuming ProjectTeamName is the third column
                'ProjectManager': result[3],  # Assuming ProjectManager is the fourth column
                'ProjectBudget': result[4],  # Assuming ProjectBudget is the fifth column
                'ProjectNotes': result[5],  # Assuming ProjectNotes is the sixth column
                'ProjectStartDate': result[6],  # Assuming ProjectStartDate is the seventh column
                'ProjectEndDate': result[7],  # Assuming ProjectEndDate is the eighth column
            }
            results_list.append(result_dict)

        if results_list == []:
            return Response({"detail":"not found"})
        else:
            # Serialize the results using the custom serializer
            serializer = ProjectDetailsSerializer(results_list, many=True)

            # Return the serialized data in the response
            return Response(serializer.data)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailsViewSet(viewsets.ModelViewSet):
    queryset = ProjectDetails.objects.all()
    serializer_class = ProjectDetailsSerializer

class ProjectTeamViewSet(viewsets.ModelViewSet):
    queryset = ProjectTeam.objects.all()
    serializer_class = ProjectTeamSerializer

class ProjectDetailViewSet(viewsets.ModelViewSet):
    queryset = ProjectDetail.objects.all()
    serializer_class = ProjectDetailSerializer
