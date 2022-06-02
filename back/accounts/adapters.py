
from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: profile_image
        age = data.get("age")
        user.age = age
        occupation = data.get("occupation")
        user.occupation = occupation
        gender = data.get("gender")
        user.gender = gender


        user.save()
        return user