from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 
import logging
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def home_page(request):
    logging.basicConfig(filename="scrapper_home.log" , level=logging.INFO)
    if request.method == 'GET':
        try:
            return render(request,"search.html")
        except:
            logging.info("no home page")
        else:
            logging.shutdown()

@api_view(['GET','POST'])
def review(request):
    logging.basicConfig(filename="scrapper.log" , level=logging.INFO)
    if request.method == 'POST':
        try:
            searchString = request.POST.get('content').replace(" ","")
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            urlClient=urlopen(flipkart_url)
            flipkart_page=urlClient.read()
            flipkart_html=bs(flipkart_page,"html.parser")
            bigbox=flipkart_html.find_all("div",{"class":"_1AtVbE col-12-12"})
            reviews = []
            for i in bigbox:
                try:
                    product_href_link=i.div.div.div.a['href']
                    product_link="https://www.flipkart.com"+product_href_link
                    product_req=requests.get(product_link)
                    product_req.encoding='utf-8'
                    product_html=bs(product_req.text,"html.parser")
                    comment_box=product_html.find_all("div",{"class":"_16PBlm"})
                    for j in comment_box:
                        try:
                            product_name=product_html.find_all("span",{"class":"B_NuCI"})[0].text
                        except Exception as e:
                            logging.info(e)
                        try:
                            Custumer_name=j.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
                        except Exception as e:
                            logging.info("no customer name")
                        try:
                            Product_rating=j.div.div.div.div.text
                        except Exception as e:
                            logging.info("no rating")
                        try:
                            Product_Caption=j.div.div.div.p.text
                        except Exception as e:
                            logging.info("no caption")
                        try:
                            Product_Discription=j.div.div.find("div",{"class":""}).div.text 
                        except Exception as e:
                            logging.info("no discription")
                        mydict = {"Product": product_name, "Name": Custumer_name, "Rating": Product_rating, "CommentHead": Product_Caption,
                          "Comment":Product_Discription}
                        reviews.append(mydict)
                    
                except Exception as e:
                    logging.info(e)
            logging.info("log my final result {}".format(reviews))
            return render(request,'result.html',{"reviews":reviews})
        except Exception as e:
                    logging.info(e)
                    
    else:
        return render('index.html')
                    