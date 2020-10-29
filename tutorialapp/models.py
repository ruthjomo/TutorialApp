from django.db import models  

class Post(models.Model):
    image = models.ImageField(upload_to = 'media/', default='No Image')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    caption = models.CharField(max_length = 60)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    @classmethod
    def get_posts(cls):
        posts = cls.objects.all()
        return posts
        
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    class Meta:
        ordering = ['pub_date']

    @classmethod
    def update_post(self, update):
        self.post = update
        self.save

    @classmethod
    def display_user_post(cls):
        post = cls.objects.filter()
        return post

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,default='')
    photo = models.ImageField(upload_to = 'media/', default='No Image')
    bio = models.TextField(max_length = 255)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def updateProfile(self, update):
       self.bio = update
       self.save

    @classmethod
    def search_profile(cls, search_term):
        user = cls.objects.filter(user__username__icontains=search_term)
        return user 

    @classmethod
    def get_by_id(cls, id):
        profile = cls.objects.get(id=id)
        return profile
