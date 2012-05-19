# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response

from tlogtparser import get_parsers

def dashboard(request):
    parsers = get_parsers()
    return render_to_response('dashboard.html', {
        'parsers': parsers,
        }, context_instance=RequestContext(request))
