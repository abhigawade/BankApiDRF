from django.db import models

# Create your models here.
class BankModel(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def validate_ifsc_code(self):
        if len(self.ifsc_code) > 10:
            raise ValueError("IFSC code should be 10 digits")
        else:
            return True