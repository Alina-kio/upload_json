from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyModelSerializer
import json


from rest_framework.viewsets import ModelViewSet
from .models import MyModel


class MyModelView(APIView):
    def post(self):
        # Получить данные из файла
        with open(r"C:\Users\User\Desktop\json\price.json") as f:
            data = json.load(f)

            # Создать объекты модели и сохранить их в базу данных
            serializer = MyModelSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                # Отправить ответ об успешной загрузке
                return Response(serializer.data, status=201)
            return Response({'status': 'success'})
            # return Response(serializer.errors, status=400)
    

    def get(self, request):
        model = MyModel.objects.all()
        data = MyModelSerializer(model, many=True).data
        return Response(data=data)


class JsonItemView(ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer