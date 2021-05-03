from django.db import models

# Create your models here.
class district(models.Model):
    name=models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.name

class thana(models.Model):
    thana=models.ForeignKey(district, on_delete=models.CASCADE)
    name=models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return 'District:' + self.thana +', Thana:'+ self.name
    
class empdepartment(models.Model):
    name=models.CharField(max_length=100, blank=False, unique=True)
    
    def __str__(self):
        return self.name

class empdesignation(models.Model):
    name=models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.name

class empbasicinfo(models.Model):
    empstatus=(
        ('Permanent','Permanent'),
        ('Trainee','Trainee'),
    )
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50, blank=True)
    dob=models.DateField()
    email=models.EmailField(max_length=50,unique=True)
    phone=models.CharField(max_length=15,unique=True)
    district=models.ForeignKey(district, on_delete=models.CASCADE)
    thana=models.ForeignKey(thana, on_delete=models.CASCADE)
    joiningdate=models.DateField()
    department=models.ForeignKey(empdepartment, on_delete=models.CASCADE)
    designation=models.ForeignKey(empdesignation, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    status=models.CharField(max_length=20,choices=empstatus)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname +' '+ self.lastname
    
class empsalary(models.Model):
    employee=models.ForeignKey(empbasicinfo, on_delete=models.CASCADE)
    basicsalary=models.FloatField()
    medical=models.FloatField()
    houserent=models.FloatField()
    others=models.FloatField()

    def __str__(self):
        return str(self.basicsalary + self.medical + self.houserent + self.others)
    
class empeducation(models.Model):
    exam=(
        ('SSC','SSC'),
        ('HSC','HSC'),
        ('Bachelor','Bachelor')
    )
    employee=models.ForeignKey(empbasicinfo, on_delete=models.CASCADE)
    degree=models.CharField(max_length=10,choices=exam)
    institute=models.CharField(max_length=100)
    passingyear=models.IntegerField()
    result=models.CharField(max_length=10)





