from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime,timedelta
#import schedule
import time
import random
from random import randint, randrange, random, uniform
import tkinter
import tkinter.ttk as ttk


driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("https://www.pokepara.jp/kanto/login/login_gal.aspx?url=%2ftokyo%2fm3%2fa10007%2fshop8778%2fgal%2f303175%2fblog%2fdiary_21586628.html")


#while 1<2:
#    try:
#        driver.find_element_by_id("bt_login")
#        sleep(1)
#    except:
#        break




xpaths=[

    "/html/body/div[2]/div[2]/div/div[2]/div/ul[1]/li[1]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[1]/li[2]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[1]/li[3]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[1]/li[4]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[1]/li[5]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[2]/li[1]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[2]/li[2]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[2]/li[3]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[2]/li[4]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[2]/li[5]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[3]/li[1]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[3]/li[2]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[3]/li[3]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[3]/li[4]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[3]/li[5]/div[1]/a/img",  
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[4]/li[1]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[4]/li[2]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[4]/li[3]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[4]/li[4]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[4]/li[5]/div[1]/a/img",      
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[5]/li[1]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[5]/li[2]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[5]/li[3]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[5]/li[4]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[5]/li[5]/div[1]/a/img",    
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[6]/li[1]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[6]/li[2]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[6]/li[3]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[6]/li[4]/div[1]/a/img",
    "/html/body/div[2]/div[2]/div/div[2]/div/ul[6]/li[5]/div[1]/a/img",    
]

xpaths2=[

    "/html/body/div[1]/div[2]/div[1]/article[1]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[2]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[3]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[4]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[5]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[6]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[7]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[8]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[9]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[10]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[11]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[12]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[13]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[14]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[15]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[16]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[17]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[18]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[19]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[20]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[21]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[22]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[23]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[24]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[25]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[26]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[27]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[28]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[29]/div/div/div[1]/div[4]/a",
    "/html/body/div[1]/div[2]/div[1]/article[30]/div/div/div[1]/div[4]/a",
]




def tryrandgood(num):
    i=0
    counter = 0
    while counter<num:
        
        if i ==30:
            
            #num-=30
            i=0
            xpath = "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/a[12]"
            driver.find_element_by_xpath(xpath).click()
            
        

        try:
            print(xpaths[i])
            sleep(0.2)
            driver.find_element_by_xpath(xpaths[i]).click()
            sleep(0.2)
            driver.find_element_by_id("iine_bottom").click()
            sleep(0.2)
            driver.back()
            counter +=1
        except:
            driver.back()
            counter +=0
        i+=1

#https://www.pokepara.jp/kanto/blog.html?
#/html/body/div[2]/div[2]/div/div[2]/div/ul[1]/li[1]/div[1]/a/img
#/html/body/div[2]/div[2]/div/div[2]/div/ul[1]/li[2]/div[1]/a/img
#/html/body/div[2]/div[2]/div/div[2]/div/ul[2]/li[1]/div[1]/a/img
#/html/body/div[2]/div[2]/div/div[2]/div/ul[2]/li[2]/div[1]/a/img
#/html/body/div[2]/div[2]/div/div[2]/div/ul[3]/li[1]/div[1]/a/img

def main(event):
    


    #    driver.find_element_by_id("bt_login").click()
    sleep(2)
    #url0 = "https://www.pokepara.jp/tokyo/m9/a10034/shop"
    #url1 = "blog/"

    url = "https://www.pokepara.jp/kanto/blog.html?"

    E1 = EditBox3.get()
    num = int(E1)

    if num>100:
        return


    print (num)
    
        #url = shop[randam]+url1
        #url = url.replace(" ","")
    try:
        #driver.get(url)
        #print(url)
        tryrandgood(num)
    except:
        print(url)

    

def test(events):
    driver.get("https://sp.pokepara.jp/gal_manage/diary/good_history.html")

    #/html/body/div[1]/div[2]/div[1]/article[1]/div/div/div[1]/div[5]/a
    #/html/body/div[1]/div[2]/div[1]/article[2]/div/div/div[1]/div[5]/a
    #/html/body/div[1]/div[2]/div[1]/article[4]/div/div/div[1]/div[4]/a
    #/html/body/div[1]/div[2]/div[1]/article[1]/div/div/div[1]/div[4]/a
    #/html/body/div[1]/div[2]/div[1]/article[1]/div/div/div[1]/div[4]/a

    num = int(EditBox4.get())

    if num>100:
        return

    i=1
    counter =0
    while counter<num:
        driver.get("https://sp.pokepara.jp/gal_manage/diary/good_history.html")


        try:
            #xpath = xpath1+str(i)+xpath2
            #print(xpath)
            sleep(0.2)
            driver.find_element_by_xpath(xpaths2[i-1]).click()
            sleep(0.2)
            driver.find_element_by_id("iine_bottom").click()
            sleep(0.2)
            #driver.back()
            sleep(0.2)
            i+=1
            counter +=1
            print("click iine")
        except:
            #driver.back()
            i+=1
            print("click dont")

        if i>num+20:
            break
    print ("test botton")

names = ["きいろ", "B", "C", "D"]
ids = ["klnj-19335","hihi","www","rty"]
passs = ["0518", "0000","0001","0002"]

def test2(event2):
    name = combo.get()
    print (name)
    for i in range(4):
        if name ==names[i]:
            idf = driver.find_element_by_id("txtId")
            passf = driver.find_element_by_id("txtPass")
            idf.clear()
            passf.clear()
            idf.send_keys(ids[i])
            passf.send_keys(passs[i])

            driver.find_element_by_id("bt_login").click()
            sleep(2)
            #print (ids[i],passs[i])

    



panel = tkinter.Tk()
panel.title("ポケパラコントローラー")
panel.geometry("400x300")

option = ["きいろ", "B", "C", "D"]  # 選択肢
variable = tkinter.StringVar ( ) #A~Dが文字列の場合
combo = ttk.Combobox ( panel , values = option , textvariable = variable )
combo.bind("<<ComboboxSelected>>")
combo.pack()

Button = tkinter.Button(panel,text=u'ログイン')
Button.bind("<Button-1>",test2) 
Button.pack()
Static1 = tkinter.Label(text=u'======================================================')
Static1.pack()
#Static1 = tkinter.Label(text=u'user number')
#Static1.pack()
#EditBox1 = tkinter.Entry(width=50)
#EditBox1.pack()
#Static1 = tkinter.Label(text=u'\n')
#Static1.pack()
#Static1 = tkinter.Label(text=u'pass word')
#Static1.pack()
#EditBox2 = tkinter.Entry(width=50)
#EditBox2.pack()
Static1 = tkinter.Label(text=u'ブログ周りのいいね数')
Static1.pack()
EditBox3 = tkinter.Entry(width=50)
EditBox3.pack()
Button = tkinter.Button(panel,text=u'ブログ周り実行')
Button.bind("<Button-1>",main) 
Button.pack()
Static1 = tkinter.Label(text=u'======================================================')
Static1.pack()
Static1 = tkinter.Label(text=u'いいね返し')
Static1.pack()
EditBox4 = tkinter.Entry(width=50)
EditBox4.pack()
Button = tkinter.Button(panel,text=u'いいね返し実行')
Button.bind("<Button-1>",test) 
Button.pack()
Static1 = tkinter.Label(text=u'======================================================')
Static1.pack()
Static1 = tkinter.Label(text=u'　')
Static1.pack()
Static1 = tkinter.Label(text=u'きいろちゃんが、一生懸命いいねを押してるので、応援してね。')
Static1.pack()

panel.mainloop()




    

driver.close()


print("end")


