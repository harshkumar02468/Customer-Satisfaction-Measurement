from django.shortcuts import render
from django.http import HttpResponse

from .forms import ReviewForm

from .pravallika  import  predict_sentiment

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_protect

from datetime import datetime
from home.models import Contact



@csrf_protect
def home_view(request):
    # Perform any necessary processing or data retrieval here
    # ...

    # Render the home page template and return the response
    return render(request, 'predict.html')
@csrf_protect
def predict(request):
    
             # Retrieve the input data from the request
            naming = request.POST.get('name')
            reviewed = request.POST.get('input-name')
            # Perform prediction using your ML model
            prediction, sentimentscore =  predict_sentiment(reviewed)
            context = {
                  'naming':naming,
                'reviewed': reviewed,
                'prediction': prediction,
                'sentimentscore' : sentimentscore
                 
               
            }

            if request.method=="POST":
                name=request.POST.get('name')
                email=request.POST.get('email')
                age=request.POST.get('age')
                role=request.POST.get('role')
                
                reviews=request.POST.get('input-name')
                contact=Contact(name=name ,email=email, age=age,role=role,reviews=reviews,prediction_result=prediction, sentimentscore=sentimentscore,date=datetime.today())
                contact.save()

            
                 
            return render(request, 'sreeja.html', context)
                       

@csrf_protect
def sentiment_analysis(request):
    contacts = Contact.objects.all()

    prediction_results = []  # Initialize an empty list

    for contact in contacts:
       prediction_results.append(contact.prediction_result)

    context = {
    'prediction_result': prediction_results
     }

      

    # Create a list to store the sentiment results
    

    # Pass the sentiment results to the template context
   


   

    positive_count = Contact.objects.filter(prediction_result = "Positive").count()
    negative_count = Contact.objects.filter(prediction_result = "Negative").count()
    neutral_count = Contact.objects.filter(prediction_result = "Neutral").count()
    total_count = Contact.objects.count()

    context = {
        'positive_count': positive_count,
        'negative_count': negative_count,
        'neutral_count': neutral_count,
        'total_count': total_count
    }

    return render(request, 'sentiment_results.html', context)

def heySweetheart(request):
    return render(request, 'predict.html')


   

                      
       

                    
            

            
            
   

     
                
            
        













