# -*- coding: utf-8 -*-

from django.http import HttpResponseBadRequest
from django.template import RequestContext
from django.shortcuts import render_to_response

from tlogtparser import get_parsers, Secure

def dashboard(request):
    parsers = get_parsers()
    return render_to_response('dashboard.html', {
        'parsers': parsers,
        }, context_instance=RequestContext(request))

def _get_parser_from_name(parser_name):
    if parser_name.lower() == 'secure':
        return Secure

def _get_logs_for_parser_page(request, parser_name, index=0):
    parser = _get_parser_from_name(parser_name)
    assert parser
    dates_list = parser.get_log_dates() or []
    index = int(index)
    try:
        date = dates_list[index]
        logs = parser.get_log(date)
    except Exception, e:
        return HttpResponseBadRequest()
    return render_to_response('parser.html', {
            'dates_list': dates_list,
            'index': index,
            'logs': logs,
            'parser_name': parser_name
        }, context_instance=RequestContext(request))

def parser_page(request, parser_name):
    return _get_logs_for_parser_page(request, parser_name)

def parser_page_on_specific_date(request, parser_name, index):
    return _get_logs_for_parser_page(request, parser_name, index)

