from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)  # Making email unique
    password = models.CharField(max_length=100)
    
    otp = models.CharField(max_length=6, null=True, blank=True)  # OTP field
    is_verified = models.BooleanField(default=False)  # Email verification status

    # To save the data
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return None

    def isExists(self):
        if Customer.objects.filter(email=self.email).exists():
            return True
        return False
