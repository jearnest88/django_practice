from django.shortcuts import render, redirect
import string, random
def index(request):
	if ('attempt' in request.session) == False:
		request.session['attempt'] = 1
	request.session['rand_word'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(14))
	return render(request, 'random_word/index.html')
def random_word(request):
	if request.method == 'POST':
		request.session['attempt'] += 1
		request.session['rand_word'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(14))
		return redirect('/')
	else:
		return redirect('/')
