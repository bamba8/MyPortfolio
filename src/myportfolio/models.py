from django.db import models

# Section Accueil (home)


class Home(models.Model):
    name = models.CharField(max_length=30)
    greetings_1 = models.CharField(max_length=10)
    greetings_2 = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='picture/')
# save time when modified
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    
# Section à propos de (about)

class About(models.Model):
    heading = models.CharField(max_length=60)
    career = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.career  
    
    
class Profile(models.Model):
    About = models.ForeignKey(About, on_delete=models.SET_NULL, null=True, blank=True)
    social_name = models.CharField(max_length=20)
    link = models.URLField(max_length=300) 
  
# Section de competence (skills)


class Category(models.Model):

    name = models.CharField(max_length=30)
    
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        
    def __str__(self):
        return self.name 


class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=30)



# portfolio section 


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=300)
    
    def __str__(self):
        return f"Portfolio {self.id}"


# portfolio Message


class PorfolioMessage(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


    class Meta:
        verbose_name = "Message"
        
    def __str__(self):
        return self.nom
    
# Experience professionelle
    
class Experiences(models.Model):
    experience_name = models.CharField(max_length=100)
    experience_Post = models.CharField(max_length=100)
    experience_description = models.TextField()
    experience_img = models.ImageField(upload_to='experience/')
   


    class Meta:
        verbose_name = "Experience"
        
    def __str__(self):
        return self.experience_name    
        