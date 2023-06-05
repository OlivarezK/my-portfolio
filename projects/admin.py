from django.contrib import admin
from .models import Project
from .models import WDCertificate
from .models import UXCertificate
from .models import DTCertificate
from .models import PMCertificate
from .models import WMCertificate
from .models import Appendix

# Register your models here.
admin.site.register(Project)
admin.site.register(WDCertificate)
admin.site.register(UXCertificate)
admin.site.register(DTCertificate)
admin.site.register(PMCertificate)
admin.site.register(WMCertificate)
admin.site.register(Appendix)