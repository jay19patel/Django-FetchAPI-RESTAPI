# Django-FetchAPI-RESTAPI


create venv and  install 
  django
  djangorestframework
  and all stuffs
activate env 





Representational State Transfer Application Programming Interface
: REST API :


-install:
    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter  # Filtering support
    
-json:
    json.dumps(data) : python object to json string (python -> json) 
    json.loads(data) : parse the json string (json data ->python )

- serializer : complaxe data type to navite python data type (queryset,model instance -> python data set -> json)
- deserializer : revser serializer  
- create separate file for serializer
    
    ex : class serializer(serializers.Serializer): # same as model
            name=serializes.charfeilds()
- serialize data to json ( JSONRenderer)
    data = JSONRenderer().render(serialize.data)

                        :::::steps :::::

- create django and app 
- create model 
- migrate
-  create serialize.py file 
-  create view using  model get fnction
-   import :
    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    in view.py file and return respone to the browser


- add decorators up to function 
    @api_view(['GET','POST','PUT,'DELETE'])
    GET : backend -> frontend 
    POST : forntend -> backend 
    PUT : update
    DELETE : delete

-  get model data in view.py
note(eror : Object of type Student is not JSON serializable)

- convert python variable to serialize data 

- some validateion perform in serialization .py file 
    def validate(self,data):
        if data['roll']>=200:
            raise serializers.ValidationError({'error':'id is more then 200'})
        return data









