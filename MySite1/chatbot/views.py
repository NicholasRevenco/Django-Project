from django.shortcuts import render
import openai
from .models import PastQ

questionCheck = 0

# Create your views here.
def home(request):
    if request.method == "POST":
        userQuestion = request.POST['question']
        userImage = request.POST['image']

        openai.api_key = # Own key
        openai.Model.list()

        if userImage == "gpt":
            GPT_Response = openai.Completion.create (
                model="text-davinci-003",
                prompt=userQuestion,
                temperature=0.1,
                max_tokens=60,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            GPT_Response = GPT_Response["choices"][0]["text"].strip()
            questionCheck = 0
        elif userImage == "dalle":
            imagePixel = request.POST['imageSize']
            if imagePixel == "two":
                imagePixel = "256x256"
            elif imagePixel == "five":
                imagePixel = "512x512"
            elif imagePixel == "one":
                imagePixel = "1024x1024"
            print(imagePixel)
            GPT_Response = openai.Image.create(
                prompt=userQuestion,
                n=1,
                size=imagePixel
            )
            GPT_Response = GPT_Response['data'][0]['url']
            questionCheck = 1
        
        saveQ = PastQ(question=userQuestion, answer=GPT_Response)
        saveQ.save()
        return render(request, "chatbot/home.html", {"userQuestion": userQuestion, "GPT_Response": GPT_Response, "userImage": userImage, "questionCheck": questionCheck})
    questionCheck = 1
    return render(request, "chatbot/home.html", {"questionCheck": questionCheck})