from dbm import error

from django.contrib import admin
from django.contrib import messages
from .models import DistributionProject, Apk

@admin.register(DistributionProject)
class DistributionProjectAdmin(admin.ModelAdmin):
    list_display = ['description', 'package_name']

@admin.register(Apk)
class ApkAdmin(admin.ModelAdmin):
    list_display = ['project', 'uploaded_at', 'apk_file']

    def save_model(self, request, obj, form, change):
        is_valid, actual_package_name = validate_apk_package(obj.apk_file.path, obj.project.package_name)


        if is_valid:
            super().save_model(request, obj, form, change)

        else:
            if actual_package_name:
                error_message = f"The uploaded APK's package name '{actual_package_name}' does not match the expected package name '{obj.project.package_name}'."
            else:
                error_message = "Failed to validate APK package name. Please ensure the file is a valid APK."
            messages.error(request, error_message)

def validate_apk_package(apk_file_path, expected_package_name):
    # allow any apk
    # todo: validate apk package name
    pass
    return True, None
