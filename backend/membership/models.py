from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django_resized import ResizedImageField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import random


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)

        user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_approved=False,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user=self._create_user(email, password, True, True, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
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
        ('Community health worker','ommunity health worker'),
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
    

    ROLE_CHOICES = (
        ('Fm', 'Farmer'),
        ('Inv', 'Investor'),
        ('Inp', 'Input Provider'),
        ('Str', 'Storage Facilitator'),
        ('Prc', 'Processing Company'),
        ('Off', 'Offtakers'),

    )

    Initials = (
        ('Dr', 'Passport'),
        ('Mr', 'Driving Lincense'),
        ('NID', 'National Indentification Card'),

    )
    TypeOfMember = [
        ('Associate Member','Associate Member'),
        ('Ordinary Member','Ordinary Member'),
    ]

    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(verbose_name="First name",max_length=254, null=False, blank=True)
    middle_name = models.CharField(verbose_name="Middle name",max_length=254, null=True, blank=True)
    last_name = models.CharField(verbose_name="Last name",max_length=254, null=True, blank=True)
    phone = models.CharField(verbose_name="Phone Number",max_length=14, validators=[RegexValidator(r'^(\+\d{1,3})?,?\s?\d{8,13}')],unique=True,help_text="Example +255714112233",null=False,blank=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    typeofmember = models.CharField(_("Membership type"), max_length=180,choices=TypeOfMember,default="Associate Member")
    memberId = models.SlugField(_("Membership Identification"),editable=False,unique=True)
    gender = models.CharField(_("Gender"), max_length=8,choices=GENDER)
    region = models.CharField(_("Region"), max_length=50,choices=REGION)
    organization = models.CharField(_("Your Organization"), max_length=180)
    profession = models.CharField(_("Your Profession"), max_length=180,choices=Proffesion)
    areaofwork = models.CharField(_("Area of work"), max_length=180,choices=AreaOfWork)
    typeofmember = models.CharField(_("Membership type"), max_length=180,choices=TypeOfMember)
    mctnumber = models.CharField(_("MCT Number"), max_length=50,blank=True,null=True)
    avatar = ResizedImageField(upload_to = 'profile/images/%Y/%m/%d',verbose_name=_("Profile Image"),size=[300, 300], crop=['middle', 'center'],default='default.jpg')
    collage = models.CharField(_("Collage that you had your masters"), max_length=180,blank=True,null=True)
    year = models.IntegerField(_("Year that you graduated"),blank=True,null=True)
    


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    
    def get_user_fullname(self):
      return "{} {}".format(self.first_name,self.last_name)

    def get_user_is_approved(self):
      return self.is_approved

    def __str__(self):
        return self.email

    def get_avatar(self):
        if self.avatar:
            return 'http://api.pediatrics.or.tz' + self.avatar.url
        return ''

    def save(self,*args, **kwargs):
        if self.typeofmember == "Ordinary Member":
            self.memberId = "pat-od-"+ str(random.randint(0, 1000))
        else:
            self.memberId = "pat-as-"+ str(random.randint(0,1000))
        super(User,self).save()

        
# # class Profile(models.Model):


#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     gender = models.CharField(_("Gender"), max_length=8,choices=GENDER)
#     region = models.CharField(_("Region"), max_length=50,choices=REGION)
#     organization = models.CharField(_("Your Organization"), max_length=180)
#     profession = models.CharField(_("Your Profession"), max_length=180,choices=Proffesion)
#     areaofwork = models.CharField(_("Area of work"), max_length=180,choices=AreaOfWork)
#     mctnumber = models.CharField(_("MCT Number"), max_length=50,blank=True,null=True)
#     collage = models.CharField(_("Collage that you had your masters"), max_length=180,blank=True,null=True)
#     year = models.IntegerField(_("Year that you graduated"),blank=True,null=True)
#     avatar = ResizedImageField(upload_to = 'profile/images/%Y/%m/%d',verbose_name=_("Profile Image"),size=[300, 300], crop=['middle', 'center'],default='default.jpg')



#     def __str__(self):  # __unicode__ for Python 2
#         return self.user.email

#     def get_avatar(self):
#         if self.avatar:
#             return 'http://api.pediatrics.or.tz' + self.avatar.url
#         return ''

#     @receiver(post_save, sender=settings.AUTH_USER_MODEL)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)

#     @receiver(post_save, sender=settings.AUTH_USER_MODEL)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()

# # @receiver(post_save, sender=User)
# # def create_or_update_user_profile(sender, instance, created, **kwargs):
# #     if created:
# #         Profile.objects.create(user=instance)
# #     instance.profile.save()


# end of users profile

MEMBERSHIP_CHOICES = (
    ('Associate Plan', 'Associate Plan'),
    ('Ordinary Plan', 'Ordinary Plan'),
)


class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES,
        default='Associate Plan',
        max_length=30)
    price = models.IntegerField(default=15)
    planId = models.CharField(max_length=40)

    def __str__(self):
        return self.membership_type

class UserMembership(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership = models.ForeignKey(
        Membership, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.email


class Subscription(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

class PaymentDate(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    price = models.IntegerField(default=15)
    created = models.DateTimeField(_("Paid at"), auto_now=False, auto_now_add=False)
    expire = models.DateTimeField(_("Paid at"), auto_now=False, auto_now_add=False)
