from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, Contact, Appointment,Testimonials,Clients,Email_subscription,Blog_Comment


# Register your models here.
# admin.site.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('heading',)}


admin.site.register(Blog, BlogAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'from_email', 'mobile_num', 'message', 'date']
    list_filter = ['date']
    search_fields = ['name']


admin.site.register(Contact, ContactAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'website']
    search_fields = ['name']


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Testimonials)
admin.site.register(Clients)
admin.site.register(Email_subscription)
admin.site.register(Blog_Comment)