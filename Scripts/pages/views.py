from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from pages.models import ImageCard
from .forms import CreateImageCardForm
from account.models import User
from operator import attrgetter

IMAGE_CARDS_PER_PAGE = 3

def home_page_view(request):
    return render(request, 'home.html')


def upload_picture_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    if request.method == 'POST':
        form = CreateImageCardForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = User.objects.filter(email=user.email).first()
            obj.author = author
            obj.save()

            return redirect('gallery')
    else:
        form = CreateImageCardForm()

    context['form'] = form



    return render(request, 'upload_picture.html', context)

def must_authenticate_view(request):
    return render(request, 'must_authenticate.html')


def gallery_view(request):
    context = {}

    images = sorted(ImageCard.objects.all(), key=attrgetter('date_published'), reverse=True)
    

    #Pagination

    page = request.GET.get('page', 1)
    image_cards_paginator = Paginator(images, IMAGE_CARDS_PER_PAGE)

    try:
        images = image_cards_paginator.page(page)
    except PageNotAnInteger:
        images = image_cards_paginator.page(IMAGE_CARDS_PER_PAGE)
    except EmptyPage:
        images = image_cards_paginator.page(image_cards_paginator.num_pages)

    context['images'] = images

    return render(request, 'gallery.html', context)
