from django.shortcuts import render, redirect
from .models import profile
import os
from django.db.models import Q
from django.contrib import messages


def index(request):

    if request.method == "POST":
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        age = request.POST.get("age")
        number = request.POST.get("number")
        address = request.POST.get("address")
        image = request.FILES.get("image")
        blood = request.POST.get("blood")
        nationality = request.POST.get("nationality")
        gender = request.POST.get("gender")
        relegion = request.POST.get("relegion")
        qualification = request.POST.get("qualification")
        date = request.POST.get("date")
        father_name = request.POST.get("father_name")
        mother_name = request.POST.get("mother_name")
        if profile.objects.filter(Q(name=lname) | Q(email=email)).exists():
            messages.warning(request, "this name or email already exit")
            return redirect('index')
        else:
            if image:

                add = profile.objects.create(name=lname, email=email, age=age, number=number,
                                             address=address, image=image, blood_group=blood, nationality=nationality,
                                             gender=gender, relegion=relegion, qualification=qualification,
                                             date_of_birth=date, father_name=father_name, mother_name=mother_name)
                add.save()
                messages.success(request, "Account Created.")
                return redirect(curd)

            else:
                add = profile.objects.create(name=lname, email=email, age=age, number=number,
                                             address=address,  blood_group=blood, nationality=nationality,
                                             gender=gender, relegion=relegion, qualification=qualification,
                                             date_of_birth=date, father_name=father_name, mother_name=mother_name)
                add.save()
                messages.success(request, "Account Created.")
                return redirect(curd)
    return render(request, 'home.html')


def curd(request):
    prof = profile.objects.all()
    if request.method == 'GET':
        src = request.GET.get('src')
        if src:
            prof = profile.objects.filter(name__icontains=src)
        elif src == None:
            prof = profile.objects.all()
        else:
            prof = profile.objects.all()
    return render(request, 'curd.html', {'prof': prof})


def profilSow(request, id):
    prof = profile.objects.get(id=id)
    return render(request, 'profile.html', {'prof': prof})


def delete(request, id):
    prof = profile.objects.get(id=id)
    if prof.image != 'def.png':
        os.remove(prof.image.path)
    prof.delete()
    return redirect("curd")


def updet(request, id):
    prof = profile.objects.get(id=id)
    if request.method == "POST":
        if len(request.FILES)!= 0:
            if len(prof.image)> 0:
                os.remove(prof.image.path)
            prof.image =request.FILES['image']
        prof.name = request.POST.get("lname")
        prof.email = request.POST.get("email")
        prof.age = request.POST.get("age")
        prof.number = request.POST.get("number")
        prof.address = request.POST.get("address")
        prof.nationality = request.POST.get("nationality")
        prof.qualification = request.POST.get("qualification")
        prof.date_of_birth = request.POST.get("date")
        prof.father_name = request.POST.get("father_name")
        prof.mother_name = request.POST.get("mother_name")
        
        prof.save()
        return redirect(curd)
    return render(request, 'updet.html', locals())
