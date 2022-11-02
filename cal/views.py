from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html')

def result(request):
	value_1 = int(request.GET['num_one'])
	value_2 = int(request.GET['num_two'])

	return render(request, 'result.html', {
		'num_1': value_1,
		'num_2': value_2,
		'sum': value_1 + value_2,
		'dif': value_1 - value_2,
		'div': value_1 / value_2,
		'mul': value_1 * value_2
	})
