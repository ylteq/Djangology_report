from django.contrib import admin
from import_export import resources
from models import Annotation,Document
from import_export.admin import ImportExportMixin, ExportActionModelAdmin

# Yu add 09/30/15
#######

class AnnotationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('document','annotator','annotation_type','begin_index','end_index',)
    list_filter = ['annotation_type',]


admin.site.register(Annotation, AnnotationAdmin)


#class AnnotationResource(resources.ModelResource):
#    class Meta:
#        model = Annotation
#        fields = ('annotator','annotation_type','begin_index','end_index',)

#class AnnotationAdmin(ImportExportModelAdmin):
#    resource_class = AnnotationResource
#    pass
########

