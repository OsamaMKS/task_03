from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list": [
                {
                "restaurant_name":"Burgerzz",
                "food_type":"Burgers",

                },
                {
                "restaurant_name":"99 grill",
                "food_type":"Burgers and Wings",

                },
                {
                "restaurant_name":"Shawermaaz",
                "food_type":"Shawerma",

                }
    ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object":
        {
        "restaurant_name":"99 grill",
        "food_type":"Burgers and Wings",
        }
    }
    return render(request, 'detail.html', context)
