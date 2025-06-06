from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone


User = get_user_model()

LEVEL_EXPERIENCE_TABLE = {
    **{i: 300 + (i - 1) * 50 for i in range(1, 10)},
    **{i: 800 + (i - 10) * 100 for i in range(10, 20)},
    **{i: 1800 + (i - 20) * 150 for i in range(20, 30)},
    **{i: 3300 + (i - 30) * 200 for i in range(30, 40)},
    **{i: 5300 + (i - 40) * 250 for i in range(40, 50)},
    **{i: 7800 + (i - 50) * 350 for i in range(50, 60)},
    **{i: 11300 + (i - 60) * 500 for i in range(60, 100)},
    **{i: 31300 + (i - 100) * 1000 for i in range(100, 200)},
    **{i: 131300 + (i - 200) * 1500 for i in range(200, 400)},
    **{i: 431300 + (i - 400) * 2000 for i in range(400, 700)},
    **{i: 1031300 + (i - 700) * 2500 for i in range(700, 1001)},
}

class Bookworm(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bookworm')
    name = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)

    def experience_to_next_level(self):
        if self.level >= 1000:
            return 0
        return LEVEL_EXPERIENCE_TABLE.get(self.level, 999999999)
    def add_experience(self, amount):
        self.experience += amount
        while self.experience >= self.experience_to_next_level():
            self.experience -= self.experience_to_next_level()
            self.level += 1
        self.save()


# 피드
class Pheed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='pheeds/', blank=True, null=True)
    like_users = models.ManyToManyField(User, related_name='liked_pheeds', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 댓글
class Comment(models.Model):
    pheed = models.ForeignKey(Pheed, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





# 책 등록
class Book(models.Model):
    isbn = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    cover_image = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # ✅ Gemini API 호출 결과 캐싱
    genres = models.JSONField(default=list, blank=True)
    keywords = models.JSONField(default=list, blank=True)
    
class ReadingRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='readingrecord_set')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    pages = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    last_updated = models.DateField(null=True, blank=True) 
    is_finished = models.BooleanField(default=False)
    quiz_completed = models.BooleanField(default=False)

    def is_today_recorded(self):
        return self.last_updated == timezone.now().date()


class Question(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    question_text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField()  # 1~4
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.PositiveIntegerField()  # 1 ~ 5 사이
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')  # 한 유저가 같은 책에 여러 리뷰 못 달게
