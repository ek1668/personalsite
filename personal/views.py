from django.shortcuts import render
from .models import Experience, Education, Photo, Personal, Certification, Post, Skill
# Create your views here.
def index(request):
  experiences = Experience.objects.all()
  educations = Education.objects.all()
  photos = Photo.objects.all()
  count = Photo.objects.all().count()
  personals = Personal.objects.all()
  certifications = Certification.objects.all()
  skills = Skill.objects.all()
  return render(request, 'index.html', {'experiences': experiences, 'educations': educations, 'photos': photos, "count": count, "personals": personals, "certifications": certifications, "skills": skills})

def blog(request):
  photos = Photo.objects.all()
  posts = Post.objects.all()
  return render(request, 'blog.html', {'photos': photos, 'posts': posts})

def post(request, pk):
  photos = Photo.objects.all()
  posts = Post.objects.get(id=pk)
  return render(request, 'post.html', {'photos': photos, 'posts': posts})

# def base(request):
#   photos = Photo.objects.all()
#   return render(request, 'base.html', {'photos': photos})