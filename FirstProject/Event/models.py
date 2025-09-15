from django.db import models

# Create your models here.

class Person(models.Model):
    cin = models.CharField(max_length=20)
    email = models.EmailField()
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(email__endswith='@esprit.tn'),
                name='email_domain_constraint'
            )
        ]

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Musique', 'Musique'),
        ('Cinema', 'Cinema'),
        ('Sport', 'Sport'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    state = models.BooleanField(default=False)
    nbe_participant = models.IntegerField(default=0)
    evt_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    organizer = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='organized_events')

class User(Person):
    pass

class Participation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participation_date = models.DateTimeField(auto_now_add=True)
