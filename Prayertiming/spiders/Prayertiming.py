import scrapy
from datetime import datetime
from Prayertiming.items import HamariwebItem
from skpy import Skype,SkypeChats


class hamariweb(scrapy.Spider):
    name = "prayerinfo"
    start_urls = ["https://hamariweb.com"]
    
    
    def parse(self,response):
        url  = "https://hamariweb.com/islam/karachi_prayer-timing1.aspx"
        yield scrapy.Request(url, callback=self.parse_dir_contents)	

    def parse_dir_contents(self, response):
        username='talha.iftikhar@technologyally.com'
        password='ti.12345'
        item=HamariwebItem()
        
        item['time'] = response.xpath("//td[contains(@class,'h5')]/b/text()").extract()
        dictitem=dict(item)
    
        for key,value in dictitem.items():
            Fajr,Tulu,Zuhr,Asr,Magrib,Isha = map(str,value)
            now=datetime.now()
            #now = datetime.now().strftime('%I:%M %p')
            
            Zh=int(Zuhr.split(':')[0])+2
            Zm=00
            Ah=int(Asr.split(':')[0]);
            Am_str=Asr.split(':')[1];
            Am=int(Am_str.split(' ')[0]);
            Mh=int(Magrib.split(':')[0]);
            Mm_str=Magrib.split(':')[1];
            Mm=int(Mm_str.split(' ')[0]);
            Ih=int(Isha.split(':')[0]);
            Im_str=Isha.split(':')[1];
            Im=int(Im_str.split(' ')[0]);
           
            if now.hour==Zh and now.minute==Zm:
                 sk = Skype(username, password)
                 ch=sk.chats.chat("19:afe93eddaa6a406fb123749b291b70ca@thread.skype");
                 ch.sendMsg("It`s time for: Zuhr")
            elif now.hour==Ah and now.minute==Am:
                sk = Skype(username, password)
                ch=sk.chats.chat("19:afe93eddaa6a406fb123749b291b70ca@thread.skype");
                ch.sendMsg("It`s time for: Asr")
            elif now.hour==Mh and now.minute==Mm:
                sk = Skype(username, password)
                ch=sk.chats.chat("19:afe93eddaa6a406fb123749b291b70ca@thread.skype");
                ch.sendMsg("It`s time for: Maghrib")
            elif now.hour-12==Ih and now.minute==Im+34:
                sk = Skype(username, password)
                ch=sk.chats.chat("19:afe93eddaa6a406fb123749b291b70ca@thread.skype");
                ch.sendMsg("It`s time for : Isha");
            else:
                print("Else called")
        
                
        yield item
    
    
    
    
    

#
#if __name__ == "__main__":
#    QuotesSpider()