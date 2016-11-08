from django.http import HttpResponse


def test_mw(get_response):
    def mw(request):
        print("MW")
        if not request.GET.get('a'):
            return get_response(request)
        return HttpResponse('aaa')
    return mw