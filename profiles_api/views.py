from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HellowApiView(APIView):
    """Test APIView"""

    serializers_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, put, delete)',
            'Similar to traditional django view',
            'Gives you the most control of your application logic',
            'Is mapped manually to urls',
        ]

        return Response({
            'message': 'Hello world',
            'an_apiview': an_apiview
        })

    def post(self, request, format=None):
        """Post request"""

        serializers_result = self.serializers_class(data=request.data)

        if serializers_result.is_valid():
            name = serializers_result.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializers_result.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """PUT request"""

        return Response({ 'method': 'PUT'})

    def patch(self, request, pk=None):
        """PATCH request"""

        return Response({ 'method': 'PATCH'})

    def delete(self, request, pk=None):
        """DELETE request"""

        return Response({ 'method': 'DELETE' })
