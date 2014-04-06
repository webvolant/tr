from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
	template = loader.get_template('main/index.html')
	context = RequestContext(request, {
        #'latest_post_list': list_of_objects,
    })
	return HttpResponse(template.render(context))

