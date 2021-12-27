from django.contrib import admin
from django.db import models
from .models import Experiences, Home, About, Profile, Category, Skills, Portfolio, PorfolioMessage


# Section Accueil (home)
admin.site.register(Home)


# Section à propos de (about)
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin): 
    inlines = [
        ProfileInline,
    ]
    

# Section de competence (skills)
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2
    
    
@admin.register(Category)   
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline, 
    ]
    
    
# portfolio section 
admin.site.register(Portfolio)


# formulaire
admin.site.register(PorfolioMessage)


#Experience professionnelle

admin.site.register(Experiences)