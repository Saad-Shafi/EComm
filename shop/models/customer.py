from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    def isExist(self):
        if Customer.objects.filter(email= self.email):
            return True
        return False

    def isExistCon(self):
        if Customer.objects.filter(phone= self.phone):
            return True
        return False

    @staticmethod
    def getCustomer(em):
        try:
            return Customer.objects.get(email= em)
        except:
            False
