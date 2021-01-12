import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from maps.models import CoordData


class MapsView(View):
    """
    Rendering the template for maps
    """

    def get(self, request):
        return render(request, 'maps/maps.html')


class AddCoordsView(View):
    """
    Adding coordinates on click
    """

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            CoordData.objects.create(latitude=body.get('latlng')['lat'], longitude=body.get('latlng')['lng'])
            return JsonResponse(status=201, data={'success': 'Coordinates saved successfully'})
        except:
            return JsonResponse(status=500, data={'error': 'Something went wrong...'})


class CoordsView(View):
    """
    Adding coordinates on click
    """

    def get(self, request):
        coords = list(CoordData.objects.all())
        return render(request, 'maps/coords.html', context={'coords': coords})
