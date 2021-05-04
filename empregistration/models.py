from django.db import models

# Create your models here.
# All Class name will start with capital letter
class District(models.Model):
    name=models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.name

class Thana(models.Model):
    thana=models.ForeignKey(District, on_delete=models.CASCADE)
    name=models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return 'District:' + self.thana +', Thana:'+ self.name
    
class EmpDepartment(models.Model):
    name=models.CharField(max_length=100, blank=False, unique=True)
    
    def __str__(self):
        return self.name

class EmpDesignation(models.Model):
    name=models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.name

class EmpBasicInfo(models.Model):
    empstatus=(
        ('Permanent','Permanent'),
        ('Trainee','Trainee'),
    )
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50, blank=True)
    dob=models.DateField()
    email=models.EmailField(max_length=50,unique=True)
    phone=models.CharField(max_length=15,unique=True)
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    thana=models.ForeignKey(Thana, on_delete=models.CASCADE)
    joiningdate=models.DateField()
    department=models.ForeignKey(EmpDepartment, on_delete=models.CASCADE)
    designation=models.ForeignKey(EmpDesignation, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    status=models.CharField(max_length=20,choices=empstatus)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname +' '+ self.lastname
    
class EmpSalary(models.Model):
    employee=models.ForeignKey(EmpBasicInfo, on_delete=models.CASCADE)
    #employee1=models.ForeignKey(EmpBasicInfo, related_name="employee1", on_delete=models.CASCADE)
    basicsalary=models.FloatField()
    medical=models.FloatField()
    houserent=models.FloatField()
    others=models.FloatField()

    def __str__(self):
        return str(self.basicsalary + self.medical + self.houserent + self.others)
    
class EmpEducation(models.Model):
    exam=(
        ('SSC','SSC'),
        ('HSC','HSC'),
        ('Bachelor','Bachelor')
    )
    employee=models.ForeignKey(EmpBasicInfo, on_delete=models.CASCADE)
    degree=models.CharField(max_length=10,choices=exam)
    institute=models.CharField(max_length=100)
    passingyear=models.IntegerField()
    result=models.CharField(max_length=10)





