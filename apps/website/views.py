# -*- coding: utf-8 -*-

import os
import simplejson
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.http import Http404

def generic(request):
    """
    Generic view for serving templates
    """

    # Load context
    json_path = os.path.join(settings.STATIC_ROOT,'json/context.json')
    context = simplejson.loads(''.join(open(json_path).readlines()))

    # Determine template name
    template_path = request.path[1:]
    if template_path == '':
        template_path = 'index.html'
    if template_path.endswith('/'):
        template_path += 'index.html'
    elif not template_path.endswith('.html'):
        template_path += '.html'

    # Check if template exists 
    template_found = False
    for template_dir in settings.TEMPLATE_DIRS:
        full_template_path = os.path.join(template_dir, template_path)
        if os.path.isfile(full_template_path):
            template_found = True
            break

    if not template_found:
        raise Http404

    return direct_to_template(request, template_path, context)
