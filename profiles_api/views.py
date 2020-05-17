from rest_framework.views import APIView
from rest_framework.response import Response

class HellowApiView(APIView):
    """Test APIView"""

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
