try:
    import os,requests,time,uuid,secrets,random,string,threading
    from colorama import Fore
except ModuleNotFoundError as e:
    m = str(e).split("'")[1]
    os.system(f'pip install {m}')

logo = """

▀▄░▄▀ ▄▀▀▄ ▄▀▀▄ ░█▀▀▀█ █▀█ 
─░█── █▄▄─ ▀▄▄█ ─▄▄▄▀▀ ─▄▀ 
▄▀░▀▄ ▀▄▄▀ ─▄▄▀ ░█▄▄▄█ █▄▄

"""


print(logo)
print("Write accounts you want to report from in accounts.txt as usr:pass")
print("")
class Strng():
    def __init__(self):
        paw = str(input("Enter Password > "))
        if paw == "":
            pass
        else:
            exit()
        os.system('cls' if os.name == 'nt' else 'clear')
        self.red = Fore.RED  
        self.lred = Fore.LIGHTRED_EX
        self.blue = Fore.BLUE
        self.lblue  = Fore.LIGHTBLUE_EX
        self.cyan = Fore.CYAN
        self.lcyan = Fore.LIGHTCYAN_EX
        self.green = Fore.GREEN
        self.lgreen = Fore.LIGHTGREEN_EX
        self.yellow = Fore.YELLOW
        print(self.red + logo)
        self.r = requests.Session()
        self.uid = str(uuid.uuid4())
        self.tkn = secrets.token_hex(8)*2
        self.cookies = []
        self.ids = []
        self.login()
    
    def login(self):

        for accs in open('accounts.txt').read().splitlines():
            self.username = str(accs).split(':')[0]
            self.password = str(accs).split(':')[1]
            
            url_log = 'https://i.instagram.com/api/v1/accounts/login/'
 
            self.headers = {
                'X-Pigeon-Session-Id': self.uid,
                'X-IG-Device-ID': self.uid,
                'X-IG-App-Locale': 'en_US',
                'X-IG-Device-Locale': 'en_US',
                'X-IG-Mapped-Locale': 'en_US',
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3brTvw8=',
                'User-Agent': 'Instagram 27.0.0.7.97 Android (28/9; 480dpi; 1080x2137; HUAWEI; JKM-LX1; HWJKM-H; kirin710; en_US; 216817344)',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': 'i.instagram.com'
            }
 
            data = {
 
                '_uuid': self.uid,
                'username': self.username,
                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(self.password),
                'queryParams': '{}',
                'optIntoOneTap': 'false',
                'device_id': self.uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_count': '0'
            }

            self.req1 = self.r.post(url_log, headers=self.headers, data=data)
            if ('logged_in_user') in self.req1.text:
                print(self.green+f"[+] {self.username} True")
                self.cookies.append(self.req1.cookies)
            else:
                print(self.red+f"[-] {self.username} bad")

        if len(self.cookies) >= 1:
            self.attack()
        else:
            print(self.blue+"[x] Check Your accounts and try again ...")
            input("")
            exit()
        
    
    def attack(self):

        self.target = str(input(self.yellow+'[+] Target to report >> '))

        if self.target == "- [ #X69Z2 ] -":
            print(self.lred+f"You're too stupid to report the programmer :/")
            input("")
            exit(1)
        else:
            pass

        try:
            get_id = str(self.r.get(f"https://www.instagram.com/{self.target}/?__a=1").json()['logging_page_id']).split('_')[1]
        except:
            print(self.lblue+"[-] No Target Found !!")
            self.attack()
        try:
            req_stories = self.r.get(f"https://i.instagram.com/api/v1/feed/user/{get_id}/story/",headers=self.headers,cookies=random.choice(self.cookies))

            for cnt in req_stories.json()['reel']['items']:
                get_str = cnt['id']
                self.ids.append(get_str)
                count = len(self.ids)
            print(self.cyan+f"Loaded {count} stories From {self.target}")
            time.sleep(4)
        except:
            print(self.lblue+"[-] No Stories Found !!")
            self.attack()
        
        self.report()
        
    def report(self):
        done = 1
        error = 0
        while True:
            for cookies in self.cookies:
                for idd in self.ids:
                    for i in range(1,8):

                        data = {
                            'source_name':'reel_profile',
                            'reason_id':i,
                            'location':'ig_post',
                            'session_id':str(uuid.uuid4()),
                            'tags':'[]',
                            'is_dark_mode':'false',
                            'frx_feedback_submitted':'false'
                        }

                        url = f'https://i.instagram.com/api/v1/media/{idd}/flag/'

                        req = self.r.post(url,data=data,headers=self.headers,cookies=cookies)

                        if '{"status":"ok"}' in req.text:
                            print(self.lgreen+f"done report by @X69Z2 BOT total stories reported [{done}]")
                            done+=1
                        else:
                            error+=1
                            print(self.red+f"error reporting [{error}] blocked or challenge_requierd")  

                        time.sleep(1)



if __name__ == "__main__":
    Strng()
