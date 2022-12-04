from django.shortcuts import render
info={
    "animals": [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 4,
            "name": "grenouille",
            "legs": 2,
            "weight": 5.67,
            "height": 4.2,
            "speed": 34,
            "family": 5
        },
        {
            "id": 5,
            "name": "cow",
            "legs": 2,
            "weight": 5.67,
            "height": 4.2,
            "speed": 34,
            "family": 3
        }
    ],
    "families": [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
        {
            "id": 3,
            "name": "mammal"
        },
        {
            "id": 4,
            "name": "reptile"
        },
        {
            "id": 5,
            "name": "amphibian"
        }
    ]
}
# Create your views here.
def family (request, id):
    context = {
        'info': info,
        'id':id,


    }
    return render(request, 'family.html', context)


def animal(request, id):
    context = {
        'info': info,
        'id':id,
    }
    return render(request, 'animal.html', context)



