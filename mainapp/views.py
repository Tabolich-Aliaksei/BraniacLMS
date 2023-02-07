from django.http import HttpResponse
from django.views.generic import View


class HelloWorldView(View)):
    def get(self, *args):
        return HttpResponse("Hello world!")


def check_kwargs(request, **kwargs):
    return HttpResponse("kwargs:<br>" + kwargs)