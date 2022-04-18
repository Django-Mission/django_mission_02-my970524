from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
# 질문 모델
class Inquiry(models.Model):
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
    title = models.TextField('제목')
    email = models.CharField('이메일', max_length=320)
    phone_number_regex = RegexValidator(
        regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$'
    )
    phone_number = models.CharField('전화번호', max_length=11)
    content = models.TextField('내용')
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)

# 답변 모델
class Answer(models.Model):
    content = models.TextField('답변 내용')
    inquiry = models.ForeignKey(
        to=Inquiry, 
        verbose_name='참조 문의글 번호', 
        on_delete=models.CASCADE
    )
    writer = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        verbose_name='답변 작성자'
    )
    created_at = models.DateTimeField('답변 작성일시', auto_now_add=True)
    updater = models.ManyToManyField(
        to=User, 
        verbose_name='최종 수정자', 
        related_name='updated_answers',
        blank=True
    )
    updated_at = models.DateTimeField('최종 수정일시', auto_now=True)