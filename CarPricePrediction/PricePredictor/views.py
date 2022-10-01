from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pickle

from .models import Data

model = pickle.load(open("./model/car_price_prediction_ml_model.sav", "rb"))


# Create your views here.
def index(request):
    return render(request, 'PricePredictor/index.html')


def about(request):
    return render(request, 'PricePredictor/about.html')


def predict(request):
    # temp ={}
    scoreval = {}

    if request.method == 'POST':
        year = int(request.POST.get('year'))
        presentprice = float(request.POST.get('presentprice'))
        kms_driven = float(request.POST.get('kilometer'))
        fuel_type = int(request.POST.get('fuel'))
        seller_type = int(request.POST.get('seller'))
        transmission = int(request.POST.get('transmission'))
        owner = int(request.POST.get('owner'))
        #     temp = {'Year': request.POST.get('year'), 'Present_Price': request.POST.get('presentprice'),
        #             'Kms_Driven': request.POST.get('kilometer'), 'Fuel_Type': request.POST.get('fuel'),
        #             'Seller_Type': request.POST.get('seller'), 'Transmission': request.POST.get('transmission'),
        #             'Owner': request.POST.get('owner')}
        #
        # testData = pd.DataFrame({'x': temp}).transpose()
        data = Data(year=year, selling_price=presentprice, kilometer_driven=kms_driven, fuel_type=fuel_type, seller_type=seller_type, transmission=transmission, owner=owner)
        data.save()
        scoreval = model.predict([[year, presentprice, kms_driven, fuel_type, seller_type, transmission, owner]])

        scoreval = np.around(scoreval, decimals=3)

    return render(request, 'PricePredictor/predict.html', {'scoreval': scoreval})


def contact(request):
    return render(request, 'PricePredictor/contact.html')
