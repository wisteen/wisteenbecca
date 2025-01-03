from django.db import models
from ckeditor.fields import RichTextField


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.email}'


class Webdata(models.Model):
    logo = models.FileField(upload_to='webImages')
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    git_url = models.URLField(blank=True)
    welcome_text = models.CharField(max_length=255)
    sub_welcome_text = models.CharField(max_length=255)
    about_us_short = models.TextField()
    about_us_long = models.TextField()
    profile_img = models.FileField(upload_to='webImages')

class Client(models.Model):
    picture = models.FileField(upload_to='webImages')
    full_name = models.CharField(max_length=255)
    quote = models.TextField()
  
SERVICE_CONTOUR = (
        ('M300,503.46388370962813C374.79870501325706,506.71871716319447,464.8034551963731,527.1746412648533,510.4981551193396,467.86667711651364C555.9287308511215,408.9015244558933,512.6030010748507,327.5744911775523,490.211057578863,256.5855673507754C471.097692560561,195.9906835881958,447.69079081568157,138.11976852964426,395.19560036434837,102.3242989838813C329.3053358748298,57.3949838291264,248.02791733380457,8.279543830951368,175.87071277845988,42.242879143198664C103.41431057327972,76.34704239035025,93.79494320519305,170.9812938413882,81.28167332365135,250.07896920659033C70.17666984294237,320.27484674793965,64.84698225790005,396.69656628748305,111.28512138212992,450.4950937839243C156.20124167950087,502.5303643271138,231.32542653798444,500.4755392045468,300,503.46388370962813', 'style 1'),
        ('M300,532.3542879108572C369.38199826031484,532.3153073249985,429.10787420159085,491.63046689027357,474.5244479745417,439.17860296908856C522.8885846962883,383.3225815378663,569.1668002868075,314.3205725914397,550.7432151929288,242.7694973846089C532.6665558377875,172.5657663291529,456.2379748765914,142.6223662098291,390.3689995646985,112.34683881706744C326.66090330228417,83.06452184765237,258.84405631176094,53.51806209861945,193.32584062364296,78.48882559362697C121.61183558270385,105.82097193414197,62.805066853699245,167.19869350419734,48.57481801355237,242.6138429142374C34.843463184063346,315.3850353017275,76.69343916112496,383.4422959591041,125.22947124332185,439.3748458443577C170.7312796277747,491.8107796887764,230.57421082200815,532.3932930995766,300,532.3542879108572', 'style 2'),
        ('M300,566.797414625762C385.7384707136149,576.1784315230908,478.7894351017131,552.8928747891023,531.9192734346935,484.94944893311C584.6109503024035,417.5663521118492,582.489472248146,322.67544863468447,553.9536738515405,242.03673114598146C529.1557734026468,171.96086150256528,465.24506316201064,127.66468636344209,395.9583748389544,100.7403814666027C334.2173773831606,76.7482773500951,269.4350130405921,84.62216499799875,207.1952322260088,107.2889140133804C132.92018162631612,134.33871894543012,41.79353780512637,160.00259165414826,22.644507872594943,236.69541883565114C3.319112789854554,314.0945973066697,72.72355303640163,379.243833228382,124.04198916343866,440.3218312028393C172.9286146004772,498.5055451809895,224.45579914871206,558.5317968840102,300,566.797414625762', 'style 3'),
        ('M300,541.5067337569781C382.14930387511276,545.0595476570109,479.8736841581634,548.3450877840088,526.4010558755058,480.5488172755941C571.5218469581645,414.80211281144784,517.5187510058486,332.0715597781072,496.52539010469104,255.14436215662573C477.37192572678356,184.95920475031193,473.57363656557914,105.61284051026155,413.0603344069578,65.22779650032875C343.27470386102294,18.654635553484475,251.2091493199835,5.337323636656869,175.0934190732945,40.62881213300186C97.87086631185822,76.43348514350839,51.98124368387456,156.15599469081315,36.44837278890362,239.84606092416172C21.716077023791087,319.22268207091537,43.775223500013084,401.1760424656574,96.891909868211,461.97329694683043C147.22146801428983,519.5804099606455,223.5754009179313,538.201503339737,300,541.5067337569781', 'style 4'),
        ('M300,582.0697525312426C382.5290701553225,586.8405444964366,449.9789794690241,525.3245884688669,502.5850820975895,461.55621195738473C556.606425686781,396.0723002908107,615.8543463187945,314.28637112970534,586.6730223649479,234.56875336149918C558.9533121215079,158.8439757836574,454.9685369536778,164.00468322053177,381.49747125262974,130.76875717737553C312.15926192815925,99.40240125094834,248.97055460311594,18.661163978235184,179.8680185752513,50.54337015887873C110.5421016452524,82.52863877960104,119.82277516462835,180.83849132639028,109.12597500060166,256.43424936330496C100.08760227029461,320.3096726198365,92.17705696193138,384.0621239912766,124.79988738764834,439.7174275375508C164.83382741302287,508.01625554203684,220.96474134820875,577.5009287672846,300,582.0697525312426', 'style 5'),
        ('M300,521.0016835830174C376.1290562159157,517.8887921683347,466.0731472004068,529.7835943286574,510.70327084640275,468.03025145048787C554.3714126377745,407.6079735673963,508.03601936045806,328.9844924480964,491.2728898941984,256.3432110539036C474.5976632858925,184.082847569629,479.9380746630129,96.60480741107993,416.23090153303,58.64404602377083C348.86323505073057,18.502131276798302,261.93793281208167,40.57373210992963,193.5410806939664,78.93577620505333C130.42746243093433,114.334589627462,98.30271207620316,179.96522072025542,76.75703585869454,249.04625023123273C51.97151888228291,328.5150500222984,13.704378332031375,421.85034740162234,66.52175969318436,486.19268352777647C119.04800174914682,550.1803526380478,217.28368757567262,524.383925680826,300,521.0016835830174', 'style 6'),
    )


SERVICE_COLOR = (
        ('yellow', 'yellow'),
        ('blue', 'blue'),
        ('orange', 'orange'),
        ('pink', 'pink'),
        ('red', 'red'),
        ('teal', 'teal'),
    )

SERVICE_ICON = (
        ('bx bx-arch', 'bx bx-arch'),
        ('bx bx-tachometer', 'bx bx-tachometer'),
        ('bx bx-chalkboard', 'bx bx-chalkboard'),
        ('bx bx-book-reader', 'bx bx-book-reader'),
        ('bx bx-group', 'bx bx-group'),
        ('bx bx-clipboard', 'bx bx-clipboard'),
        ('bx bx-teacher', 'bx bx-teacher'),
        (' bx bx-palette', ' bx bx-palette'),
        ('bx bx-code-alt', 'bx bx-code-alt'),
        ('bx bx-brush', 'bx bx-brush'),
        ('bx bx-laptop', 'bx bx-laptop'),
        ('bx bx-wrench-alt', 'bx bx-wrench-alt'),
        ('bx bx-airplane', 'bx bx-airplane'),
        ('bx bx-globe-alt', 'bx bx-globe-alt'),
        ('bx bx-suitcase-alt', 'bx bx-suitcase-alt'),
        ('bx bx-map-alt', 'bx bx-map-alt'),
        ('bx bx-passport', 'bx bx-passport'),
        ('bx bx-vector', 'bx bx-vector'),
        ('bx bx-image', 'bx bx-image'),
        ('bx bx-paint', 'bx bx-paint'),
        ('bx bx-pen', 'bx bx-pen'),
        ('bx bx-palette-alt', 'bx bx-palette-alt'),

    )

class Service(models.Model):
    icon = models.CharField(max_length=255, choices=SERVICE_ICON)
    icon_color = models.CharField(max_length=255, choices=SERVICE_COLOR)
    icon_contor = models.CharField(max_length=5555, choices=SERVICE_CONTOUR)
    service_title = models.CharField(max_length=50)
    service_brief_description = models.CharField(max_length=400)
    service_link = models.URLField(max_length=300, blank=True)


class SkillRight(models.Model):
    skill_title = models.CharField(max_length=255)
    skill_percent = models.CharField(max_length=255)

class SkillLeft(models.Model):
    skill_title = models.CharField(max_length=255)
    skill_percent = models.CharField(max_length=255)

class Summary(models.Model):
    name = models.CharField(max_length=255)
    about_me = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Education(models.Model):
    certificate = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    year_range = models.CharField(max_length=255)
    brief_description = models.CharField(max_length=255)

class Experience(models.Model):
    experience = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    year_range = models.CharField(max_length=255)
    brief_description = RichTextField()

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    
class Facts(models.Model):
    happy_clients = models.CharField(max_length=255)
    project = models.CharField(max_length=255)
    hours_of_support = models.CharField(max_length=255)
    award_and_certifications = models.CharField(max_length=255)

PORTFOLIO = (
        ('graphics', 'graphics'),
        ('webapp', 'webapp'),
        ('others', 'others'),
    )
class Portfolio(models.Model):
    category = models.CharField(max_length=255, choices=PORTFOLIO)
    brief_description = RichTextField()
    image = models.FileField(upload_to='Portfolio')
    url = models.URLField(blank=True)













from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField

from django.utils import timezone
from django.utils.text import slugify


from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
import random
import string


def generate_unique_slug(instance, name):
    slug = slugify(name)
    model_class = instance.__class__
    unique_slug = slug
    counter = 1

    while model_class.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{slug}-{counter}"
        counter += 1

    return unique_slug


class Category(models.Model):
    ICON_CHOICES = [
        ('fa-laptop', 'Laptop'),
        ('fa-mobile-alt', 'Mobile'),
        ('fa-tshirt', 'T-shirt'),
        ('fa-home', 'Home'),
        ('fa-car', 'Car'),
        ('fa-book', 'Book'),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='fa-laptop')
    image = models.ImageField(upload_to="category_images/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product_image/")
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    description = RichTextField()
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    details = RichTextField(blank=True, null=True)
    product_code = models.CharField(max_length=8, unique=True, editable=False, blank=True, null=True)
    stock = models.IntegerField(default=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discount(self):
        if self.old_price and self.new_price:
            return round((self.old_price - self.new_price) / self.old_price * 100, 2)
        return None

    @property
    def is_available(self):
        return self.stock > 0

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)

        if not self.product_code:
            self.product_code = self.generate_product_code()


        super().save(*args, **kwargs)

    def generate_product_code(self):
        prefix = 'IHM'
        suffix = ''.join(random.choices(string.digits, k=5))
        return f"{prefix}{suffix}"

    def average_rating(self):
        ratings = Rating.objects.filter(product=self)
        if ratings.count() == 0:
            return 0
        cal = sum(rating.rating for rating in ratings) / ratings.count()
        return round(cal, 1)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Rating out of 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images/")
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product.name}"