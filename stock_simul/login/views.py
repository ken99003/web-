from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import userform



def memberlist(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template=loader.get_template('main.html')
  return HttpResponse(template.render())


def newUser(requset):
  if requset.method == 'GET':
    newUser = loader.get_template('register.html')
    context = {'form':userform()}
    return HttpResponse(newUser.render(context, requset))
  elif requset.method == 'POST':
    user_form=userform(requset.POST)
    if user_form.is_valid():
      print('is valid')
      user_form.save()
      result = 'success'
    else:
      result=user_form.errors.as_data()
    user_form_result=loader.get_template('register_result.html')
    return HttpResponse(user_form_result.render({'result':result}, requset))
    
      


