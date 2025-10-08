
from django.db import models



def get_upload_path(y,u):
    return "yess"


class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads")  ################### uploaded MEDIA_ROOT/uploads
    uploaded_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.file.name
