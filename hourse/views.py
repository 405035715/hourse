# coding = utf-8

from django.shortcuts import render, HttpResponse
import json


def gethoursedata(request):
    """
    get hourse data from sohu
    :param request:
    :return:
    """

    return HttpResponse(json.dumps([]), content_type="application/json", status=200)