# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import pandas as pd
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import predict
from . import forms


@csrf_exempt
def initial(request):
    error = "None"
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            bedrooms = request.POST['bedrooms']
            bathrooms = request.POST['bathrooms']
            sqft_living = request.POST['sqft_living']
            sqft_lot = request.POST['sqft_lot']
            floors = request.POST['floors']
            yr_built = request.POST['yr_built']
            zipcode = request.POST['zipcode']
            return HttpResponse(predict.processRequest([float(bedrooms), float(bathrooms), float(sqft_living), float(sqft_lot), float(floors), float(yr_built), float(zipcode)])[0][0])
        else:
            error = form.errors
            return HttpResponse(str(error))
    else:
        return HttpResponse("Please Send Request Using POST")
    return HttpResponse(now)
