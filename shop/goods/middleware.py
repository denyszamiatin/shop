from http.client import HTTPResponse


def test_mw(get_request):
    def mw(request):
        print("MW")
        if not request.GET.get('a'):
            return get_request(request)
        return None
    return mw