from django.shortcuts import render,redirect
from.models import model_user,donor,Hospital,recipient,feed

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def user_register(request):
     if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        gender=request.POST['gender']
        bloodgroup=request.POST['bloodgroup']
        phone_no=request.POST['phone_no']
        mail=request.POST['mail']
        password=request.POST['password']
        model_user(name=name,dob=dob,gender=gender,bloodgroup=bloodgroup,phone_no=phone_no,mail=mail,password=password).save()
        return render(request,'user_login.html')
     else:
         return render(request,'user_register.html')
 


def user_login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('pswd')
        cr=model_user.objects.filter(name=name,password=password)
        if cr:
            details=model_user.objects.get(name=name,password=password)
            ml=details.mail
            request.session['email']=ml
            return render(request,'home.html',{'m':ml})
        else:
            msg='Invalid credentials!'
            return render(request,'user_login.html',{'msg':msg})
    else:
        return render(request,'user_login.html')
    


def profile(request):
    email=request.session['email']
    cr=model_user.objects.get(mail=email)
    if cr:
        user_info = {
            'name':cr.name,
            'dob': cr.dob,
            'gender': cr.gender,
            'bloodgroup': cr.bloodgroup,
            'phone_no': cr.phone_no,
            'email': cr.mail,
            'password': cr.password
        }
        return render(request, 'profile.html', user_info)
    else:
        return render(request, 'user_login.html')   


def donation(request):
    email=request.session['email']
    cr=model_user.objects.get(mail=email)
    name = cr.name
    dob = cr.dob
    gender = cr.gender
    bloodgroup = cr.bloodgroup
    phone_no = cr.phone_no
    if request.method == 'POST':
        type=request.POST['organtype']
        agree=request.POST['agree']
        address=request.POST['address']
        emergency=request.POST['emergency']
        
        donor(name=name,dob=dob,contactno=phone_no,gender=gender,bloodgroup=bloodgroup,organtype=type,mail=email,agreement=agree,address=address,emergency=emergency).save()
        return render(request,'home.html')
    else:
         return render(request,'donation.html',{'email':email,'name':name,'dob':dob,'gender':gender,'bloodgroup':bloodgroup,'phone_no':phone_no})
     

def donors(request):

    return render(request,'donors.html')
def bloodview(request):
    o=donor.objects.filter(organtype='Blood')
    
    return render (request,'list_donors.html',{'data':o})

    
def bonemarrowview(request):
    cr= donor.objects.filter(organtype='Bone Marrow')

    return render(request,'list_donors.html',{'data':cr})


def kidneyview(request):
    cr= donor.objects.filter(organtype='Kidney')
    
    return render(request,'list_donors.html',{'data':cr})


def lungsview(request):
    cr= donor.objects.filter(organtype='Lungs')
    
    return render(request,'list_donors.html',{'data':cr})


def liverview(request):
     cr= donor.objects.filter(organtype='Liver')

     return render(request,'list_donors.html',{'data':cr})


def heartview(request):
    cr= donor.objects.filter(organtype='Heart')

    return render(request,'list_donors.html',{'data':cr})

def pancreasview(request):
    cr= donor.objects.filter(organtype='Pancreas')

    return render(request,'list_donors.html',{'data':cr})

def intestineview(request):
    cr= donor.objects.filter(organtype='Intestine')

    return render(request,'list_donors.html',{'data':cr})

def eyeview(request):
    cr= donor.objects.filter(organtype='Eye')

    return render(request,'list_donors.html',{'data':cr})



def feedback(request):
     email=request.session['email']
     if request.method == 'POST':
        name=request.POST['name']
        phone_no=request.POST['phone_no']
        msg=request.POST['msg']
        feed(name=name,phone=phone_no,mail=email,message=msg).save()
        return render(request,'home.html')
     else:
         return render(request,'feedback.html',{'email':email})
     

def about(request):
    return render(request,'about.html')
 

def hospital_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        cr = Hospital.objects.filter(email=email)
        if cr:
            msg = "A hospital is already registered with this email."
            return render(request, 'hospital_register.html', {'msg': msg})
        else:
            h_name = request.POST.get('h_name')
            own_name = request.POST.get('own_name')
            city = request.POST.get('city')
            state = request.POST.get('state')
            ph = request.POST.get('phone_number')
            password = request.POST.get('password')
            Hospital(h_name=h_name,own_name=own_name,city=city,state=state,ph=ph,email=email, pswd=password,status='applied' ).save()
            msg='Registration application commpleted.please wait for admin confirmation'
            return render(request, 'hospital_register.html', {'msg': msg})
    else:
        return render(request, 'hospital_register.html')
    

def hospital_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cr = Hospital.objects.filter(email=email, pswd=password, status='approved')
        if cr:
            details = Hospital.objects.get(email=email, pswd=password, status='approved')
            request.session['h_email'] = details.email
            request.session['h_name'] = details.h_name
            return render(request, 'h_home.html')
        else:
            message = 'Invalid credentials or the hospital is not approved by the admin.'
            return render(request, 'hospital_login.html', {'message': message})
    else:
        return render(request, 'hospital_login.html')
    
def h_home(request):
    return render(request, 'h_home.html')

def h_profile(request):
    email = request.session['h_email']
    cr = Hospital.objects.get(email=email)
    if cr:
        h_info = {
            'h_name': cr.h_name,
            'own_name': cr.own_name,
            'city': cr.city,
            'state': cr.state,
            'ph': cr.ph,
            'email': cr.email,
            'status': cr.status
        }
        return render(request, 'h_profile.html', h_info)

def add_recipient(request):
     if request.method == 'POST':
        name=request.POST['name']
        age=request.POST['age']
        gender=request.POST['gender']
        bloodgroup=request.POST['bloodgroup']
        organ = request.POST['organs']
        desease=request.POST['desease']
        phone_no=request.POST['phone_no']
        mail=request.POST['mail']
        address=request.POST['address']
        recipient(name=name,age=age,gender=gender,bloodgroup=bloodgroup,organ=organ,disease=desease,phone_no=phone_no,mail=mail,address=address).save()
        return render(request,'h_home.html')
     else:
         return render(request,'add_recipient.html')
     
     
def add_donors(request):
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        gender=request.POST['gender']
        contactno=request.POST['contactno']
        bloodgroup=request.POST['bloodgroup']
        organtype=request.POST['organtype']
        email=request.POST['email']
        address=request.POST['address']
        address=request.POST['address']
        agree=request.POST['agree']
        emergency=request.POST['emergency']
        
        donor(name=name,dob=dob,contactno=contactno,gender=gender,bloodgroup=bloodgroup,organtype=organtype,mail=email,agreement=agree,address=address,emergency=emergency).save()
        return render(request,'h_home.html')
    else:
         return render(request,'add_donors.html')
     
# def recipient_register(request):
#      if request.method == 'POST':
#         name=request.POST['name']
#         age=request.POST['age']
#         gender=request.POST['gender']
#         bloodgroup=request.POST['bloodgroup']
#         organ = no=request.POST['organs']
#         phone_no=request.POST['phone_no']
#         mail=request.POST['mail']
#         password=request.POST['password']
#         recipient(name=name,age=age,gender=gender,bloodgroup=bloodgroup,organ=organ,phone_no=phone_no,mail=mail,password=password).save()
#         return render(request,'user_login.html')
#      else:
#          return render(request,'recipient_reg.html')
        
# def recipient_login(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         password=request.POST.get('pswd')
#         cr=recipient.objects.filter(name=name,password=password)
#         if cr:
#             details=recipient.objects.get(name=name,password=password)
#             ml=details.mail
#             request.session['r_email']=ml
#             return render(request,'home.html',{'m':ml})
#         else:
#             msg='Invalid credentials!'
#             return render(request,'recipient_login.html',{'msg':msg})
#     else:
#         return render(request,'recipient_login.html')
    
# def r_profile(request):
#     email=request.session['r_email']
#     cr=recipient.objects.get(mail=email)
#     if cr:
#         user_info = {
#             'name':cr.name,
#             'age': cr.age,
#             'gender': cr.gender,
#             'bloodgroup': cr.bloodgroup,
#             'phone_no': cr.phone_no,
#             'email': cr.mail,
#             'password': cr.password
#         }
#         return render(request, 'r_profile.html', user_info)
#     else:
#         return render(request, 'user_login.html')
    
def list_recipient(request):
    cr= recipient.objects.all()
    return render(request,'list_recipient.html',{'data':cr})

def search(request):
    if request.method=='POST':
        bt=request.POST.get('blood')
        data= donor.objects.filter(bloodgroup=bt)
        return render(request,'list_recipient.html',{'data':data})

    
    
# admin side

def admin_home(request):
    return render(request,'admin_home.html')


def admin_login(request):  
   if request.method=='POST':
      uname = request.POST.get('uname')
      passw = request.POST.get('pass')
      u = 'admin'
      p = 'admin'
      if uname==u:
         if passw==p:
          return render(request,'admin_home.html')  
   return render(request,"admin_login.html")

# users list view

def users_list(request):
    data=model_user.objects.all()
    return render(request,'users_list.html',{'data':data})


def delete_record1(request,id):
    data=model_user.objects.get(id=id)
    data.delete()
    return render(request,'admin_home.html')

def hospitals_list(request):
    data=Hospital.objects.all()
    return render(request,'hospitals_list.html',{'data':data})

def update_status(request):
    if request.method == 'POST':
        hid = request.POST.get('hid')
        print(hid)
        status = request.POST.get('status')
        dt=Hospital.objects.get(h_name=hid)
        dt.status = status
        dt.save()
        return redirect('hospitals_list') 
    
    
def delete_record2(request,id):
    data=Hospital.objects.get(id=id)
    data.delete()
    return render(request,'admin_home.html')

def organs_list(request):
    data=donor.objects.all()
    return render(request,'organs_list.html',{'data':data})


def delete_record3(request,id):
    data=donor.objects.get(id=id)
    data.delete()
    return render(request,'admin_home.html')

def recipients_list(request):
    data=recipient.objects.all()
    return render(request,'recipients_list.html',{'data':data})


def delete_record4(request,id):
    data=recipient.objects.get(id=id)
    data.delete()
    return render(request,'admin_home.html')


def my_donations(request):
   email=request.session['email']
   cr=donor.objects.filter(mail=email)
   return render(request,'my_donations.html',{'data':cr})

def feedback_list(request):
    data=feed.objects.all()
    return render(request,'feedback_list.html',{'data':data})


def delete_record5(request,id):
    data=feed.objects.get(id=id)
    data.delete()
    return render(request,'admin_home.html')


# update profile view

def edit_profile(request):
   c=request.session['email']
   cr = model_user.objects.get(mail=c)
   id = cr.id
   a = cr.name
   b = cr.dob
   c = cr.gender
   d = cr.bloodgroup
   e = cr.phone_no
   f = cr.mail 
   g = cr.password


  
   return render(request,'edit_profile.html',{'id':id,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g})


def update_profile(request):
   if request.method=='POST':
      id = request.POST.get('id')
      a = request.POST.get('phone_no')
      b = request.POST.get('mail')
      c = request.POST.get('password')
      
      dt=model_user.objects.get(id=id)
      
    
      dt.phone_no = a
      dt.mail = b
      dt.password = c
      dt.save()
      return render(request,'home.html')
