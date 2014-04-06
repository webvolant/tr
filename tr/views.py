
from django.db.models import Q
def search(request):
    if 'search' in request.GET and request.GET['search']:
        try:
            er = ''
            search = request.GET['search']
            art = article.objects.filter(Q(title__icontains=search)|Q(text__icontains=search))
            if not len(wr):
                er = u'По вашему запросу не найдено ни одной статьи.'
        except:
            art = []
            er = u'пзвините. В данный момент доступ к базе данных невозможен. попробуйте повторить ваш запрос позже.'
    else:
        wr = []
        er = u'Вы не ввели данные в строку запроса'
    c = RequestContext(request, {'text':art, 'sercher':er,})
    return render_to_response('serch/serch.html',c)

def einfach(request):
    hello = "hell"
    c = RequestContext(request, {'text':art, 'sercher':er,})
    return render_to_response('serch/serch.html',c)