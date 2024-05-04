from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response
from threading import Timer
import time
from random import randint


class ReactView(APIView):
    # def get(self, request):

    #     output = [{"employee": output.employee, "department": output.department}
    #               for output in React.objects.all()[::-1]
    #               ]
    #     # output = [{"employee": output.employee, "department": output.department}
    #     #           for output in React.objects.all()[::-1]
    #     #           ]
    #     return Response(output)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    def get(self,request):
        new_record= React.objects.create(employee=f"Worker-{str(randint(1,50))}",department=f"Department-{str(randint(1,50))}")
    #     for i in range(100):
        output = [{"employee": output.employee, "department": output.department}
                for output in React.objects.all()[::-1]
                ]
    #         output = [{"employee": str(i) , "department": "döngü 100"}]
    #         time.sleep(2)
        print(f"timer_random {output}")
        return Response(output)

