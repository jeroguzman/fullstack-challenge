from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from .models import Persona


class CsvJsonView(APIView):
    def post(self, request):
        try:
            archivo = request.FILES["archivo"]
            archivo_data = archivo.read().decode("utf-8")
            lines = archivo_data.split("\n")
            list = []
            for line in lines:
                if line != "Nombre,Correo Electronico,Telefono":
                    fields = line.split(",")
                    if next((x for x in list if x["nombre"] == fields[0]), None) is None:
                        if len(fields) == 3:
                            data_dict = {}
                            data_dict["nombre"] = fields[0]
                            data_dict["email"] = fields[1]
                            data_dict["telefono"] = fields[2]
                            persona = Persona.objects.create(**data_dict)
                            list.append(data_dict)
                    if next((x for x in list if x["email"] == fields[1]), None) is None:
                        if len(fields) == 3:
                            data_dict = {}
                            data_dict["nombre"] = fields[0]
                            data_dict["email"] = fields[1]
                            data_dict["telefono"] = fields[2]
                            persona = Persona.objects.create(**data_dict)
                            list.append(data_dict)
                    if next((x for x in list if x["telefono"] == fields[2]), None) is None:
                        if len(fields) == 3:
                            data_dict = {}
                            data_dict["nombre"] = fields[0]
                            data_dict["email"] = fields[1]
                            data_dict["telefono"] = fields[2]
                            persona = Persona.objects.create(**data_dict)
                            list.append(data_dict)
            return Response(list, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
