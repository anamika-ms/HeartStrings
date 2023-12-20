from django.contrib import admin
from . models import *


admin.site.register(model_user)
admin.site.register(donor)
admin.site.register(Hospital)
admin.site.register(recipient)
admin.site.register(feed)
