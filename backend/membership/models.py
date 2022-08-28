from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _



# Create your models here.
class User(AbstractUser):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    REGION = [
        ('Arusha', 'Arusha'),('Dar es Salaam', 'Dar es Salaam'),
        ('Dodoma', 'Dodoma'),('Geita', 'Geita'),
        ('Iringa', 'Iringa'),
        ('Kagera', 'Kagera'),
        ('Katavi', 'Katavi'),
        ('Kigoma', 'Kigoma'),
        ('Kilimanjaro', 'Kilimanjaro'),
        ('Lindi', 'Lindi'),
        ('Manyara', 'Manyara'),
        ('Mara', 'Mara'),
        ('Mbeya', 'Mbeya'),
        ('Mjini Magharibi', 'Mjini Magharibi'),
        ('Morogoro', 'Morogoro'),
        ('Mtwara', 'Mtwara'),
        ('Mwanza', 'Mwanza'),
        ('Njombe', 'Njombe'),
        ('Pemba North', 'Pemba North'),
        ('Pemba South', 'Pemba South'),
        ('Pwani', 'Pwani'),
        ('Rukwa', 'Rukwa'),
        ('Ruvuma', 'Ruvuma'),
        ('Shinyanga', 'Shinyanga'),
        ('Simiyu', 'Simiyu'),
        ('Singida', 'Singida'),
        ('Songwe', 'Songwe'),
        ('Tabora', 'Tabora'),
        ('Tanga', 'Tanga'),
        ('Unguja North', 'Unguja North'),
        ('Unguja South', 'Unguja South'),

    ]

    Proffesion = [
        ('Administrator','Administrator'),
        ('ommunity health worker','ommunity health worker'),
        ('First responder such as EMT or Paramedic','First responder such as EMT or Paramedic'),
        ('Medical doctor','Medical doctor'),
        ('Mental health provider such as counselor, psychologist, social worker','Mental health provider such as counselor, psychologist, social worker'),
        ('Nurse or practitioner or physician assistant','Nurse or practitioner or physician assistant'),
        ('Pharmacist','Pharmacist'),
        ('Paediatrician','Paediatrician'),
        ('Public health official','Public health official'),
        ('Testing or laboratory personnel','Testing or laboratory personnel'),
        ('Teacher/educator','Teacher/educator'),
        ('Researcher','Researcher'),
        ('Student','Student'),
        ('Other','Other'),
    ]
    
    AreaOfWork = [
        ('Work','Work'),
        ('Hospital','Hospital'),
        ('Community healthcare','Community healthcare'),
        ('Nursing/care facility','Nursing/care facility'),
        ('Non-governmental organization','Non-governmental organization'),
        ('School/university','School/university'),
        ('Government','Government'),
        ('Others','Others'),
    ]
    
    TypeOfMember = [
        ('Associate Member','Associate Member'),
        ('Ordinary Member','Ordinary Member'),
    ]
    
    middlename = models.CharField(_("Middle Name"), max_length=50)
    mctnumber = models.CharField(_("MCT Number"), max_length=50)
    gender = models.CharField(_("Gender"), max_length=8,choices=GENDER)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    region = models.CharField(_("Region"), max_length=50,choices=REGION)
    organization = models.CharField(_("Your Organization"), max_length=180)
    profession = models.CharField(_("Your Profession"), max_length=180,choices=Proffesion)
    areaofwork = models.CharField(_("Area of work"), max_length=180,choices=AreaOfWork)
    typeofmember = models.CharField(_("Membership type"), max_length=180,choices=TypeOfMember)
    memberId = models.SlugField(_("Membership Identification"))
    


    def __str__(self):
        return self.user.username

    def save(self,*args, **kwargs):
        if self.typeofmember == "Associate Member":
            self.memberId = "pat-am-"+str(self.pk)
        elif self.typeofmember == "Ordinary Member":
            self.memberId = "pat-od-"+str(self.pk)
        super(User,self).save()