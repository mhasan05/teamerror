from skill.models import *
from contact.models import *
from account.models import UserAccount
def left_slider(request):
    get_user = UserAccount.objects.get(username = "teamerror")
    languages = Language.objects.all()
    coreskills = CoreSkill.objects.all()
    otherskills = OtherSkill.objects.all()
    cv = CV.objects.all()
    social_links = Social.objects.all()
    addresses = Address.objects.all

    data = {
        'languages':languages,
        'coreskills':coreskills,
        'otherskills':otherskills,
        'social_links':social_links,
        'addresses':addresses,
        'cv':cv,
        'get_user':get_user,
    }
    return data