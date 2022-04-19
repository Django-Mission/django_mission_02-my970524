from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Faq(models.Model):
    question = models.TextField('질문 내용')

    # choices에 들어갈 변수들 정의
    GENERAL = 'general'
    ACCOUNT = 'account'
    ETCETERA = 'etc'

    # choices 튜플 리스트 생성
    CATEGORY_CHOICES = [
        (GENERAL, '일반'),
        (ACCOUNT, '계정'),
        (ETCETERA, '기타'),
    ]
    category = models.CharField(
        '카테고리', 
        max_length=15, 
        choices=CATEGORY_CHOICES, 
        default=CATEGORY_CHOICES[0][0]
    )
    answer = models.TextField('답변 내용')
    writer = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        verbose_name='작성자'
    )
    created_at = models.DateTimeField('작성일시', auto_now_add=True)
    updater = models.ManyToManyField(
        to=User, 
        verbose_name='최종 수정자', 
        related_name='updated_posts',
        blank=True
    )
    updated_at = models.DateTimeField('최종 수정일시', auto_now=True)






