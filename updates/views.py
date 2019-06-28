import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Update
from restapi.mixins import JsonResponseMixin
from django.views.generic import View
from django.core.serializers import serialize

# Create your views here.

#def detail_view(request):
    #return render() #return JSON data or XML

# Django Fixtures 
# python manage.py dumpdata --format json --indent 4
# python manage.py dumpdata updates.Update --format json --indent 4

def json_example_view(request):
    '''
    URI -- for a REST API
    GET -- Retrieve data
    '''
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    #Old ways of doing it.
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
    #return JsonResponse(data)


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
         }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return self.render_to_json_response(data)

class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        data = Update.objects.get(id=1).serialize()
        # data = obj.serialize()
        # data = serialize("json", [obj,], fields=('user', 'content'))
        # data = {
        #     "user": obj.id,
        #     "username": obj.username,
        #     "content": obj.content
        # }
        return JsonResponse(data, safe=False)

class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        data = Update.objects.all().serialize()
        # data = serialize("json", qs, fields=('user', 'content'))
        # print(data)
        # obj = Update.objects.get(id=1)
        # data = {
        #     "username": obj.username,
        #     "content": obj.content
        # }
        return JsonResponse(data, safe=False)

