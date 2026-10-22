from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

from .models import Product

class SignUpForm(UserCreationForm):

    name = forms.CharField(
        max_length=100,
        label="이름"
    )

    birth_date = forms.DateField(
        label="생년월일",
        widget=forms.DateInput(
            attrs={
                "type": "date"
            }
        )
    )

    phone = forms.CharField(
        max_length=20,
        label="휴대폰번호"
    )

    class Meta:

        model = User

        fields = [
            "username",
            "name",
            "birth_date",
            "phone",
            "password1",
            "password2",
        ]


    def clean_username(self):

        username = self.cleaned_data.get(
            "username"
        )

        if User.objects.filter(
            username=username
        ).exists():

            raise forms.ValidationError(
                "이미 사용 중인 아이디입니다."
            )

        return username


    def clean_phone(self):

        phone = self.cleaned_data.get(
            "phone"
        )

        if Profile.objects.filter(
            phone=phone
        ).exists():

            raise forms.ValidationError(
                "이미 사용 중인 휴대폰번호입니다."
            )

        return phone


    def save(self, commit=True):

        user = super().save(
            commit=False
        )

        user.first_name = self.cleaned_data[
            "name"
        ]

        if commit:

            user.save()

            Profile.objects.create(
                user=user,
                birth_date=self.cleaned_data[
                    "birth_date"
                ],
                phone=self.cleaned_data[
                    "phone"
                ]
            )

        return user

class ProductForm(forms.ModelForm):

    image = forms.ImageField(
        required=False,
        label="상품 사진"
    )

    class Meta:
        model = Product

        fields = [
            "title",
            "content",
            "region",
            "price",
            "negotiable",
            "image",
        ]

        labels = {
            "title": "제목",
            "content": "본문내용",
            "region": "판매 지역",
            "price": "판매 가격",
            "negotiable": "네고 가능",
        }