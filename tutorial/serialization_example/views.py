from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from serialization_example.serializers import SnippetSerializer
from serialization_example.models import Snippet
from rest_framework.parsers import JSONParser


@csrf_exempt
def snippet_list(request):
    """
    List all snippets, or create a new snippet
    class JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs)
    """
    if request.method == 'GET':
        serializer = SnippetSerializer(Snippet.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



