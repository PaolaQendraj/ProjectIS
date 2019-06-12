from django.contrib import admin

from HealthApp.models import Vakte
from HealthApp.models import Mengjesi
from HealthApp.models import Dreka
from HealthApp.models import Darka
from HealthApp.models import Snacks
from HealthApp.models import Sport_Natyre
from HealthApp.models import Sport_Ujore
from HealthApp.models import Sport_Grupe
from HealthApp.models import Sport_Palester
from HealthApp.models import Pyetesor


# Register your models here.

admin.site.register(Vakte)
admin.site.register(Mengjesi)
admin.site.register(Dreka)
admin.site.register(Darka)
admin.site.register(Snacks)
admin.site.register(Sport_Natyre)
admin.site.register(Sport_Ujore)
admin.site.register(Sport_Grupe)
admin.site.register(Sport_Palester)
admin.site.register(Pyetesor)


