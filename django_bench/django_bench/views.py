from django.http import JsonResponse


def test_json(request):
    return JsonResponse({"hello": "world"})
