from django.shortcuts import render

from .models import Finch

# finches = [
#     {
#         'species': 'Zebra Finch',
#         'scientific_name': 'Taeniopygia guttata',
#         'habitat': 'Grasslands and savannas',
#         'status': 'Least Concern',
#     },
#     {
#         'species': 'Gouldian Finch',
#         'scientific_name': 'Erythrura gouldiae',
#         'habitat': 'Tropical savannas',
#         'status': 'Near Threatened',
#     },
#     {
#         'species': 'European Goldfinch',
#         'scientific_name': 'Carduelis carduelis',
#         'habitat': 'Open woodlands and gardens',
#         'status': 'Least Concern',
#     },
#     # Add more finch dictionaries as needed
# ]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html',{
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {
        'finch': finch
    })