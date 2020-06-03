from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import add_bottle, add_crate, add_keg
from .forms import add_bottle_form, add_crate_form, add_keg_form


def products(request):
    # returns homepage
    add_bottles = add_bottle.objects.all()
    add_crates = add_crate.objects.all()
    add_kegs = add_keg.objects.all()

    return render(request, "../templates/products.html", 
    {"add_bottles": add_bottles,
    "add_crates": add_crates,
    "add_kegs": add_kegs})


def get_add_bottle_form(request):
    # add bottle form
    if request.method == "POST":
        print(request.POST)
        bottle_form = add_bottle_form(request.POST, request.FILES)
        if bottle_form.is_valid():
            bottle_form.save()
            return redirect(reverse('products'))
    else:
        bottle_form = add_bottle_form()

    return render(request, "../templates/add_bottle.html", {"bottle_form": bottle_form})


def get_add_crate_form(request):
    # add crate form
    if request.method == "POST":
        print(request.POST)
        crate_form = add_crate_form(request.POST, request.FILES)
        if crate_form.is_valid():
            crate_form.save()
            return redirect(reverse('products'))
    else:
        crate_form = add_crate_form()

    return render(request, "../templates/add_crate.html", {"crate_form": crate_form})


def get_add_keg_form(request):
    # add keg form
    if request.method == "POST":
        print(request.POST)
        keg_form = add_keg_form(request.POST, request.FILES)
        if keg_form.is_valid():
            keg_form.save()
            return redirect(reverse('products'))
    else:
        keg_form = add_keg_form()

    return render(request, "../templates/add_keg.html", {"keg_form": keg_form})

def bottlepk_delete(request, pk=None):
    # deletes selected bottle

    delete_bottle = get_object_or_404(add_bottle, pk=pk)
    delete_bottle.delete()

    return redirect(reverse('products'))

def bottlepk_edit(request, pk):
    # deletes selected bottle
    edit_bottle = get_object_or_404(add_bottle, pk=pk)

    if request.method == "POST":

        edit_info_bottle = add_bottle_form(
            request.POST, request.FILES, instance=edit_bottle)
        if edit_info_bottle.is_valid():
            edit_bottle = edit_bottle.save()
            edit_info_bottle.save()
            return redirect(reverse('products'))

    else:
        edit_info_bottle = add_bottle_form(instance=edit_bottle)

    return render(request, "../templates/product_edit.html", {
        "edit_info": edit_info_bottle})


def cratepk_delete(request, pk=None):
    # deletes selected crate

    delete_crate = get_object_or_404(add_crate, pk=pk)
    delete_crate.delete()

    return redirect(reverse('products'))

def cratepk_edit(request, pk):
    # deletes selected bottle
    edit_crate = get_object_or_404(add_crate, pk=pk)

    if request.method == "POST":

        edit_info_crate = add_crate_form(
            request.POST, request.FILES, instance=edit_crate)
        if edit_info_crate.is_valid():
            edit_crate = edit_crate.save()
            edit_info_crate.save()
            return redirect(reverse('products'))

    else:
        edit_info_crate = add_crate_form(instance=edit_crate)

    return render(request, "../templates/product_edit.html", {
        "edit_info": edit_info_crate})



def kegpk_delete(request, pk=None):
    # deletes selected bottle

    delete_keg = get_object_or_404(add_keg, pk=pk)
    delete_keg.delete()

    return redirect(reverse('products'))

def kegpk_edit(request, pk):
    # deletes selected bottle
    edit_keg = get_object_or_404(add_keg, pk=pk)

    if request.method == "POST":

        edit_info_keg = add_keg_form(
            request.POST, request.FILES, instance=edit_keg)
        if edit_info_keg.is_valid():
            edit_keg = edit_keg.save()
            edit_info_keg.save()
            return redirect(reverse('products'))

    else:
        edit_info_keg = add_keg_form(instance=edit_keg)

    return render(request, "../templates/product_edit.html", {
        "edit_info": edit_info_keg})
