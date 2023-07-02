from datetime import datetime
user_details=[]
home_details=[]
verifi_house=[]
approve_house=[]
req_house=[]
history=[]
class user_profile:
    def __init__(self,user_id:int=None,user_name:str=None,user_email:str=None,user_phno:str=None,user_password:str=None,user_city:str=None,user_role:str=None):
        self.user_id=user_id
        self.user_name=user_name
        self.user_email=user_email
        self.user_phno=user_phno
        self.__user_password=user_password
        self.user_city=user_city
        self.user_role=user_role
    def hardcodedata(self):
        user_details.append(self)
        return user_details
    def validate_login(self,email,password):
        for i in user_details:
            if i.user_email==email and i.__user_password==password :
                return i
    def welcome(self):
        print('Welcome',login_user.user_role)
class Home_details(user_profile):
    def __init__(self,Home_id=None,Home_locality=None,Home_city=None,Home_square_feet=None,Home_type=None,Home_rent=None,user_id=None):
        self.Home_id=Home_id
        self.Home_locality=Home_locality
        self.Home_city=Home_city
        self.Home_square_feet=Home_square_feet
        self.Home_type=Home_type
        self.Home_rent=Home_rent
        super().__init__(user_id)
    def hardcodedata(self):
        #print(self.Home_id)
        home_details.append(self)
        return home_details
    
    def choice(self):
        choice=input('Whether add the new house details then print ""yes"" or remove the house details : ')
        if(choice=='yes'):
            self.add_home_details()
        else:
            self.delete_details()
    def add_home_details(self):
        home=Home_details(3,'Anna Nagar','Chennai','1200','3BHK','Rs.15000/Month')
        home.hardcodedata()
    def delete_details(self):
        for i in home_details:
            if(login_user.user_id==i.user_id):
                home_details.remove(i)
class payment:
    def __init__(self,payment_id=None,card_number=None,cvv=None,exp_date=None):
        self.payment_id=payment_id
        self.card_number=card_number
        self.cvv=cvv
        self.exp_date=exp_date
    def add_to_card(self):
        self.card_number=input('Enter your card number : ')
        self.cvv=int(input('Enter your cvv : '))
        self.exp_date=input('Enter your exp_date : ')
        print('Thanks for pay the payment : ')
    def time(self):
        now=datetime.now
        da_ti=now.strftime('%y &m %d %H:%M:%S')
        history.append(da_ti)

class verified_House(Home_details):
    def __init__(self,verified_home_id=None,Home_id=None,status=None):
        self.verified_home_id=verified_home_id
        self.status=status
        super().__init__(Home_id)
    def veri_house(self):
        verified_house=verified_House(1,1,'Approve')
        approve_house.append(verified_house)
        verified_house=verified_House(2,4,'Approve')
        approve_house.append(verified_house)
        verified_house=verified_House(3,2,'Not approved')
        approve_house.append(verified_house)
        for home in home_details:
            for appo in approve_house:
                if(home.Home_id==appo.Home_id):
                    if(appo.status=='Approve'):
                        verifi_house.append(str(appo.verified_home_id))
                        verifi_house.append(home)
    def available_home_details(self):
        for i in range(1,len(verifi_house),2):
            print('selcted id',i)
            print('Home locality : ',verifi_house[i].Home_locality)
            print('Home city : ',verifi_house[i].Home_city)
            print('Home square_feet : ',verifi_house[i].Home_square_feet)
            print('Home type : ',verifi_house[i].Home_type)
            print('Home rent : ',verifi_house[i].Home_rent)
            print("********************")
class request(payment):
    def __init__(self,request_id=None,verified_home_id1=None,status=None):
        self.request_id=request_id
        self.verified_home_id1=verified_home_id1
        self.status=status
    def selected_home(self):
        self.sel=int(input('Enter your prefer home selcted id : '))
        if(self.sel==1):
            self.selcted=verifi_house[self.sel]
            self.selcted=request(None,self.sel,None)
            req_house.append(self.selcted)
        elif(self.sel==3):
            self.selcted=verifi_house[self.sel]
            self.selcted=request(None,self.sel,None)
            req_house.append(self.selcted)
    def requset_home(self):
        reqst_home=request(1,4,None)
        req_house.append(reqst_home)
        reqst_home=request(2,5,None)
        req_house.append(reqst_home)
        for i in req_house:
            ssel=input('Enter are you ok or not : ')
            if(ssel=='ok'):
                print('approve')
                print(i.verified_home_id1)
                if(i.verified_home_id1==self.sel):
                    self.add_to_card()
            else:
                print('rejected')
class history:
    def __init__(self,history_id=None,payment_id=None,verified_home_id1=None,user_id=None):
        self.history_id=history_id
        self.payment_id=payment_id
        self.verified_home_id1=verified_home_id1
        self.user_id=user_id
    def show_history(self):
        print(history)
if __name__=="__main__":
    user=user_profile(1,'Priya','priya@gmail.com','8072649175','Priya*2003','Theni','Owner')
    user.hardcodedata()
    user=user_profile(2,'Yoga','yoga@gmail.com','8072649190','yoga*2003','Selam','Tenant')
    user.hardcodedata()
    user=user_profile(3,'Mohitha','mohitha@gmail.com','8072649075','Mohitha*2003','Erode','Approver')
    user.hardcodedata()
    login_user=user.validate_login('yoga@gmail.com','yoga*2003')
    if login_user:
        print('successfully login!! ')
        home=Home_details(1,'Kodambakkam','Chennai','798','2BHK','Rs.6000/Month',1)
        home.hardcodedata()
        home=Home_details(2,'Goripalayam','Madurai','560','1BHK','Rs.5500/Month',3)
        home.hardcodedata()
        home=Home_details(4,'Antipatti','Theni','9060','9BHK','Rs.100000/Month',5)
        home.hardcodedata()
        if(login_user.user_role=='Owner'):
            user.welcome()
            home.choice()
            re=request()
            re.requset_home()
            
        elif(login_user.user_role=='Approver'):
            veri=verified_House()
            veri.veri_house()
        elif(login_user.user_role=='Tenant'):
            s=input('If you want to see home details enter ""yes"" : ')
            if(s=='yes'):
                veri=verified_House()
                veri.veri_house()
                veri.available_home_details()
                re=request()
                re.selected_home()
                re.requset_home()
                h=history()
                h.show_history()
    '''
    for i in verifi_house:
        print('>>>>>>>>>')
        print(i.Home_city)
    '''
    
            
              
            
        
