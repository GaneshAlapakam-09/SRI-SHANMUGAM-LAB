import json
from django.http import JsonResponse
from django.shortcuts import render,redirect

from num2words import num2words

from . models import Billing_Details, Billing_Master,Test_Master

# Create your views here.

def dashboard(request):
    return render(request,'index.html')
def add_bill(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        name = data.get('name')
        last_name = data.get('last_name')
        dob = data.get('dob')
        years = data.get('years')
        months = data.get('months')
        days = data.get('days')
        gender = data.get('gender')
        phone = data.get('phone')
        alt_phone = int(data.get('alt_phone')) if data.get('alt_phone') else 0
        email = data.get('email')
        refered_by = data.get('reference')
        address = data.get('address')
        discount = data.get('discount')
        amount = data.get('grand_total')
        final_amount = int(amount) - int(discount)


        items = data.get('items', [])


        last_bill = Billing_Master.objects.order_by('-S_No').first()
        if last_bill:
            new_s_no = last_bill.S_No + 1
            new_bill = f"BILL{(int(last_bill.Bill_Id[4:]) + 1):04d}"
        else:
            new_s_no = 1
            new_bill = 'BILL0001' 
        bill=Billing_Master.objects.create(
            S_No = new_s_no, 
            Bill_Id = new_bill, 
            Title = title, 
            Name = name, 
            Last_Name = last_name, 
            DOB = dob, 
            Years = years, 
            Months = months, 
            Days = days, 
            Gender = gender, 
            Phone = phone, 
            Alt_Phone = alt_phone,
            Email=email, 
            Refered_By = refered_by, 
            Address = address,
            Discount = discount, 
            Amount = amount,
            Final_Amount = final_amount
        )

        for item in items:
            Billing_Details.objects.create(
                Bill_Id = bill,
                Particulars = item.get('particular'),
                Price = item.get('price')
            )
        # Process or save the data
        return JsonResponse({'status': 'success'})



        
    data = Test_Master.objects.all()
    return render(request,'add_bill.html',{'data':data})

def list_bill(request):
    data = Billing_Master.objects.all()
    context = {'data':data}
    return render(request,'list_bill.html',context)


def print_bill(request,id):
    data = Billing_Master.objects.get(Bill_Id = id)
    data2 = Billing_Details.objects.filter(Bill_Id = id)
    amount = data.Final_Amount
    amount_in_words = num2words(amount, to='cardinal', lang='en_IN').title() + " Rupees Only"
    context = {'data':data,'data2':data2,'amount_in_words':amount_in_words}
    return render(request,'overall_invoice.html',context)

def add_test(request):
    if request.method == "POST":
        last_test = Test_Master.objects.order_by('-S_No').first()
        if last_test:
            new_s_no = last_test.S_No + 1
            new_id = f"BILL{(int(last_test.Test_Id[4:]) + 1):04d}"
        else:
            new_s_no = 1
            new_id = 'BILL0001' 
        particulars = request.POST['particulars']
        price = request.POST['price']
        Test_Master.objects.create(S_No = new_s_no, Test_Id = new_id, Test_Name = particulars, Price = price)
    return render(request,'add_test.html')

def list_test(request):
    data = Test_Master.objects.all()
    context = {'data':data}
    return render(request,'list_test.html',context)


