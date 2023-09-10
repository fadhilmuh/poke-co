from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name':'Fadhil Muhammad',
        'class':'PBP-B',
        'char_name':'Pikachu',
        'char_description':'This is Pikachu. You know this is Pikachu. Why are you asking me about why i wrote this?',
        'char_amount':'You have Gazillion amount of this character.'
    }

    return render(request, 'main.html', context)