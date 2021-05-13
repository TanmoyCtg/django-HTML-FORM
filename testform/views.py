from django.shortcuts import render, redirect

# Create your views here.

def homePage(request):
	context = {}

	if request.method == 'POST':

		firstName = request.POST.get('firstName')
		lastName = request.POST.get('lastName')
		phoneNumber = request.POST.get('phoneNumber')
		nid = request.POST.get('nid')
		address = request.POST.get('address')

		print(firstName, lastName, phoneNumber, nid, address)
		print(type(firstName), type(lastName), type(phoneNumber), type(nid), type(address))



		return redirect('success')



	return render(request, 'simpleform/inputform.html',context)

def successPage(request):
	context = {}

	return render(request, 'simpleform/success.html',context)