from django.shortcuts import render
from django.http import JsonResponse
import json
from statistics import *
import operator
from .models import Bike


def index(request):
    return render(request, 'gomoto/index.html', {})


def get_bikes(request):
    data_from_vue = json.loads(request.body)
    priorities_list = data_from_vue["priorities_list"]
    filters_dict = data_from_vue["filters_dict"]

    response_dictionary = {}

    bikes = Bike.objects.all()

    # This gives me all bikes
    bikes = bikes.filter(**filters_dict)
    filters_dict = {}
    if len(bikes) < 3:
        # return JsonResponse({'bikes':[]}) #<--- Matthew
        return JsonResponse(
            {'message': 'There are no motorcycle that meet these filters. GOMOTO some more!', 'bikes': []})

    bike_score_list = []
    for property in priorities_list:
        property_set = []
        count = 0
        none_count = 0
        for bike in bikes:
            property_value = getattr(bike, property)
            if property_value is None:
                none_count += 1
            elif property_value is not None:
                property_set.append(property_value)

        # mean_list[property]=mean(property_set)
        property_mean = mean(property_set)
        standard_dev = stdev(property_set)

    top_3_bikes = std_dev_calc(property_mean, standard_dev, bikes, priorities_list)

    return_list = []

    keys = []
    for field in Bike._meta.fields:
        if field.name != 'id':
            keys.append(field.name)

    for bike in top_3_bikes:
        values = []
        for field in keys:
            values.append(getattr(bike, field))
        return_list.append(dict(zip(keys, values)))

    return_data = {'bikes': return_list}

    return JsonResponse(return_data)


def std_dev_calc(property_mean, standard_dev, bikes, priorities_list):
    all_bikes_scores = {}
    count_bikes = 0
    for bike in bikes:
        bike_score = 0
        count = len(priorities_list)
        count_bikes += 1
        for property in priorities_list:
            weighted = count / len(priorities_list)
            bike_prop_value = getattr(bike, property)
            if bike_prop_value is not None:
                z_score = (bike_prop_value - property_mean) / standard_dev * weighted
                if property == 'seatheight' or property == 'weight' or property == 'price':
                    z_score *= -1
                count -= 1
            else:
                z_score = -1
                count -= 1
            bike_score += z_score
        all_bikes_scores[bike] = bike_score

    all_bikes_scores = sorted(all_bikes_scores.items(), key=operator.itemgetter(1), reverse=True)
    all_bikes_scores = dict(all_bikes_scores[:3])
    #
    # for bike in all_bikes_scores:
    #     top_3_bikes.append(bike[0])

    return all_bikes_scores
