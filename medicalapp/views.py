# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .forms import *

from .models import *


# Create your views here.


class MedicineView(View):

    def get(self, request):
        return render(request, "medicalapp/medical.html")


class CreateMedicineView(View):

    def get(self, request):
        return render(request, "medicalapp/add_medicine.html");


class SaveMedicineView(View):

    def get(self, request):
        pass

    def post(self, request):
        data = json.loads(request.body)
        data1 = data["medicine"]
        print data1
        for dict in data1:
            m = Medicine(name=dict.get("name"), rate=dict.get("rate"), description=dict.get("description"))
            m.save()

        return JsonResponse({"response": "SUccessfully save."})


class ShowMedicineView(View):

    def get(self, request):
        medicine = Medicine.objects.all().values()
        data = list(medicine)
        return JsonResponse(data, safe=False)


class ListMedicineView(View):

    def get(self, request):
        return render(request, "medicalapp/medicine.html");


class LoadMedicineview(View):

    def get(self, request):
        medicine = Medicine.objects.all().values()
        data = list(medicine)
        print data
        return JsonResponse(data, safe=False)


class CreateMedicinePurchaseView(View):

    def get(self, request):
        return render(request, "medicalapp/purchase_medicine.html")


class SaveMedicinePurchaseView(View):

    def get(self, request):
        pass

    def post(self, request):
        data = json.loads(request.body)
        data1 = data["medicine_purchase"]
        dis = data['discount']
        net_total = data['netTotal']
        bill = Bill()
        bill.save()
        for dict in data1:
            mp = MedicinePurchase(bill_id=bill.id, medicine_id=dict["medicineId"].get("id"),
                                  quantity=dict.get("quantity"),
                                  manufacture_date=dict.get("manufacture_date"), expiry_date=dict.get("expiry_date"))
            m = Medicine.objects.get(id=dict["medicineId"].get("id"));
            m.rate = dict.get("rate")
            m.save()
            mp.save()

        mpa = MedicinePurchaseAmount(bill_id=bill.id, discount=dis, net_total=net_total)
        mpa.save()

        return JsonResponse({"response": "Successfully Save."}, safe=False)


class MedicineQuantityView(View):

    def get(self, request):
        return render(request, "medicalapp/medicine_list.html")


class MedicineListView(View):

    def get(self, request):
        medicine_list = []
        medicine = Medicine.objects.all();
        medicine_purchase = MedicinePurchase.objects.all()
        for m in medicine:
            total = 0
            for md in medicine_purchase:
                if m.id == md.medicine_id:
                    total += md.quantity
            medicine_list.append({"name": m.name, "total": total})

        print medicine_list
        data = medicine_list
        return JsonResponse(data, safe=False)


class ExpriedMedicineView(View):

    def get(self, reqeust):
        medicine_list = []
        medicine = Medicine.objects.all()
        medicine_purchase = MedicinePurchase.objects.all()
        for m in medicine:
            total = 0
            for mp in medicine_purchase:
                if m.id == mp.medicine_id:
                    if mp.cal_date() <= 0:
                        total += mp.quantity
            if total > 0:
                medicine_list.append({"name": m.name, "total": total})

        print medicine_list
        return JsonResponse(medicine_list, safe=False)


class ExpiredMedicineTemplateView(View):

    def get(self, request):
        return render(request, "medicalapp/expired_medicine.html")


class MedicinePurchaseTemplateView(View):

    def get(self, request):
        return render(request, "medicalapp/medicine_purchase_list.html")


class MedicinePurchaseListView(View):

    def get(self, reqeust):
        medicine_purchase_list = []
        medicine_purchase = MedicinePurchase.objects.all()
        medicine = Medicine.objects.all()
        for m in medicine:
            for mp in medicine_purchase:
                if (m.id == mp.medicine_id):
                    expiry_day = mp.cal_date()
                    name = m.name
                    medicine_purchase_list.append({"id": mp.id,
                                                   "name": name, "quantity": mp.quantity,
                                                   "manufacture_date": mp.manufacture_date,
                                                   "expiry_date": mp.expiry_date,
                                                   "purchase_date": mp.bill.created_date, "expiry_day": expiry_day})

        return JsonResponse(medicine_purchase_list, safe=False)


class MedicineCategoryView(View):

    form = MedicineCategoryForm()
    category_form = CategoryForm()
    def get(self, request):
        left_leg = MedicineCatetory.objects.filter(name='left leg')

        category = MedicineCatetory.objects.all()
        medicine = Medicine1.objects.all()
        print medicine
        context = {
            'category': category,
            'medicine': medicine,
            'form': self.form,
            'category_form': self.category_form,
        }

        return render(request, "medicalapp/medicine_category.html",context)

    def post(self, request):
        name = request.POST.get("name")
        category = request.POST.get("category")
        m = Medicine1(name=name, category_id=category)
        m.save()



class MedicalCategoryView(View):

    form = MedicineCategoryForm()
    def get(self, request):
        return render(request, "medicalapp/medicine_category.html", {'form': self.form})


