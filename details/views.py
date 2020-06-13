from django.shortcuts import render,HttpResponse
import csv
from details.models import ApiView

# Create your views here.
def index(request):
    context = {
        "first_name": "raj",
        "last_name": "kumar",
        "address": "Tamilnadu, India",
    }
    return render(request, 'index.html', context)

def student_list(request):
    with open('students.txt') as csvfile:
        read = csv.DictReader(csvfile)
        instances = [
            ApiView(
                stu_name=row['stu_name'],
                stu_age=row['stu_age'],
                stu_class=row['stu_class']
            )
            for row in read
        ]

        data = ApiView.objects.bulk_create(instances)
    return HttpResponse("created")

def delete(request):
    s = ApiView.objects.all().delete()
    return HttpResponse("deleted")