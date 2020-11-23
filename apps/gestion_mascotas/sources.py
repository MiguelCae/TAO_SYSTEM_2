from import_export import resources  
from .models import mascota

class Mascota_resource(resources.ModelResource):
    class Meta:
        model = mascota