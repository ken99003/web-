from django.http import HttpResponse
from django.template import loader
from .models import Member,userData
from .forms import registerform,loginform
from django.shortcuts import redirect


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
    context = {'form':registerform()}
    return HttpResponse(newUser.render(context, requset))
  elif requset.method == 'POST':
    user_form=registerform(requset.POST)
    if user_form.is_valid():
      print('is valid')
      user_form.save()
      result = 'success'
    else:
      result=user_form.errors.as_data()
    user_form_result=loader.get_template('register_result.html')
    return HttpResponse(user_form_result.render({'result':result}, requset))
  

def login(request):
  if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            password = form.cleaned_data['password']
            try:
                user = userData.objects.get(account=account)
                if user.password == password:  # 简单明文比对密码，不推荐
                    # 登录成功，设置会话
                    request.session['user_id'] = user.id
                    return redirect('information')
                      # 登录成功后跳转到主页
                else:
                    form.add_error('password', 'Incorrect password.')
            except userData.DoesNotExist:
                form.add_error('account', 'Account does not exist.')
  else:
      form = loginform()
  template=loader.get_template('login.html')
  context = {
     'form' : form,
  }
  return HttpResponse(template.render(context,request))
    
      
def personal_information(request):
  template=loader.get_template('personal_information.html')
  data = request.session.get('user_id')#待處理
  return HttpResponse(template.render())

