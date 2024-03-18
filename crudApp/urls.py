from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='HomePage'),
    path('delete/<int:id>', views.delete_data, name='DeleteData'),
    path('<int:id>/', views.update_data, name='UpdateData'),
]


# elif 'search' in request.POST:
#         query = request.POST.get('searchquery')
#         if query:
#             students = Student.objects.filter(Q(name__icontains=query) | Q(email__icontains=query) | Q(address__icontains=query))
#     context = {'students': students, "query":query}
#     return render(request, 'AddandShow.html', context=context)