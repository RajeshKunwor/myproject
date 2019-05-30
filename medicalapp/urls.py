from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^medical/$', MedicineView.as_view(), name='medical'),
    # url(r'^add_medicine/$',CreateMedicineView.as_view(), name='add_medicine'),
    # url(r'^medicine/$', ShowMedicineView.as_view(), name='medicine'),
    url(r'^list_medicine/$', ListMedicineView.as_view(), name='list_medicine'),
    url(r'add_medicine/$', CreateMedicineView.as_view()),
    url(r'^save_medicine/$', SaveMedicineView.as_view(), name='save_medicine'),
    url(r'^add_medicine_purchase/$', SaveMedicinePurchaseView.as_view(), name="add_purchase_medicine"),
    url(r'^load_medicine/$', LoadMedicineview.as_view(), name="load-medicine"),
    url(r'^create_medicine_purchase', CreateMedicinePurchaseView.as_view(), name='create_medicine_purchase'),
    url(r'^medicine_list/$', MedicineListView.as_view(), name='medicine_list'),
    url(r'^medicine/$', MedicineQuantityView.as_view()),
    url(r'^expire_medicine/$', ExpriedMedicineView.as_view(), name="expire_medicine"),
    url(r'^expired_medicine/$', ExpiredMedicineTemplateView.as_view()),
    url(r'medicine_purchase_list/$', MedicinePurchaseTemplateView.as_view()),
    url(r'medicine_purchase_load/$', MedicinePurchaseListView.as_view(), name='medicine_purchase_load'),
    url(r'^medicine_category/$', MedicineCategoryView.as_view()),

]