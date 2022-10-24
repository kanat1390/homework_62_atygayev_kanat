from django.urls import reverse


class SuccessDetailUrlMixin:
    detail_url_name = None 
    def get_success_url(self):
        return  reverse(self.detail_url_name, kwargs={'pk':self.object.pk})