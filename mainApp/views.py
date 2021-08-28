from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import *


class login(TemplateView):
    template_name = "login/login_page.html"

    def get(self, request):
        form = login_form()
        return render(request, self.template_name, context={"form": form, "ERR": ""})

    def post(self, request):
        post = request.POST
        db = User.objects
        form = login_form(request.POST)
        if post["password"] == post["repit_password"]:

            if len(db.filter(email=post["email"])) == 0:
                db.create(email=post["email"], password=post["password"],
                          profile_photo="photos/profile_photos/defoult.png", description="Я простой рабочий диод")
                obj = db.get(email=post['email'])
                obj.login = obj.pk
                obj.name = "Диод"
                obj.save()

                request.session["logedacc"] = str(obj.login)
                return redirect(f"/profile/{db.get(email=post['email']).login}")
            else:
                obj = db.get(email=post['email'])
                request.session["logedacc"] = str(obj.login)
                if post["password"] == obj.password:
                    return redirect(F"/profile/{db.get(email=post['email']).login}")
                else:
                    return render(request, self.template_name,
                                  context={"form": form, "ERR": "Не верный пароль или email"})
        else:
            return render(request, self.template_name, context={"form": form, "ERR": "Не совпадают пароли"})


class profile(TemplateView):
    template_name = "profile_page/profile_page.html"

    def get(self, request, login):
        obj = User.objects.get(login=login)
        if login == request.session["logedacc"]:
            return render(request, self.template_name,
                          context={"is_owner": True, "obj": obj, "change_page": f"/changedata/{obj.login}"})
        else:
            return render(request, self.template_name, context={"is_owner": False, "obj": obj})


class changedata(TemplateView):
    template_name = "changedata_page/changedata_page.html"

    def get(self, request, login):

        obj = User.objects.get(login=login)
        form = change_data_form(
            {"login": obj.login, "name": obj.name, "description": obj.description, "photo": obj.profile_photo,
             "email": obj.email, "password": obj.password, "profile_photo": obj.profile_photo})
        return render(request, self.template_name, context={"form": form, "obj": obj, "ERR": ""})

    def post(self, request, login):
        post = request.POST
        obj = User.objects.get(login=login)
        form = change_data_form(request.POST, request.FILES)
        if len(User.objects.filter(login=post["login"])) >= 1 and User.objects.get(login=post["login"]) != obj:
            print(request.POST)
            return render(request, self.template_name, context={"form": form, "obj": obj, "ERR": "Не уникальный логин"})
        else:
            obj.name = post["name"]
            obj.login = post["login"]
            obj.description = post["description"]
            obj.email = post["email"]
            obj.password = post["password"]
            if request.FILES.get("profile_photo"):
                obj.profile_photo = request.FILES["profile_photo"]
            obj.save()
            return redirect(f"/profile/{obj.login}")


class redir(TemplateView):
    def get(self, request):
        return redirect("/login/")



class messenger(TemplateView):
    template_name = "messenger_page/messenger_page.html"

    def get(self, request, login_id, chat_id):
        obj = User.objects.get(login=login_id)
        if login_id == request.session["logedacc"]:
            return render(request, self.template_name,
                          context={"is_owner": True, "obj": obj})
        else:
            return render(request, self.template_name, context={"is_owner": False, "obj": obj})




def pagenotfound(reqest, exception):
    return HttpResponse(f"<h1>Либо ты проебався либ о я еблан;(</h1>")
