import requests
import datetime 

class Userdata:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.url_base='https://travel.dbaid.shop/'
        # self.url_base='http://127.0.0.1:5000/'
        self.user_url=self.url_base + 'user/'+ self.user_id
        self.daily_url = self.url_base + 'dailyinfo/'+self.user_id

    def get_all_columns(self):
        data = {
        "meta": 1
        }
        headers = {'Content-Type': 'application/json'}  
        r = requests.get(self.user_url,json=data,headers=headers)
        # col_dict = r.json()
        # print(r.json())
        column_list = [item for item in r.json().values() if item != 'u_id']
        return column_list          
    def add_data(self, name: str = "test", gender: bool = True, age: float = 20,
                 weight: float = 60, height: float = 160, activity_level: float = 1.2):
        if gender :
            gender = '男'
        else:
            gender = '女'
        data = {
                "name": name,
                "gender": gender,
                "age": age,
                "weight": weight,
                "height": height,
                "activity_level": activity_level
        }
        r = requests.post(self.user_url,json=data)
        return r.json()

    def search_data(self, field: str, data):
        headers = {'Content-Type': 'application/json'}  
        data = {}
        r = requests.get(self.user_url,json=data,headers=headers)
        return r.json()            

    def update_data(self, field: str, data):
        data = {field : data}
        r = requests.put(self.user_url,json=data)
        return r.json()

    def delete_data(self):
        r = requests.delete(self.user_url)
        return r.json()
    
    

class Dailydata:

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.url_base='https://travel.dbaid.shop/'
        # self.url_base='http://127.0.0.1:5000/'
        self.user_url=self.url_base + 'user/'+ self.user_id
        self.daily_url = self.url_base + 'dailyinfo/'+self.user_id
        self.daily_all_url = self.url_base + 'useralldata/'+self.user_id    
    
    def add_data(self, food_name: str = None, food_calories: float = 0,
                 exercise_name: str = None, exercise_duration: float = 0, weight_target: float = 0,bmr_target: float = 0, calories_burned: float = 0):
        date = datetime.datetime.now().strftime("%y-%m-%d")
        time = datetime.datetime.now().strftime("%H:%M:%S")
        data = {
                "food_name" : food_name,
                "food_calories" : food_calories,
                "date": date,
                "time": time,
                "exercise_name": exercise_name,
                "exercise_duration": exercise_duration,
                "weight_target": weight_target,
                "bmr_target": bmr_target,
                "calories_burned": calories_burned                
        }
        r = requests.post(self.daily_url,json=data)
        return r.json()

    def search_data(self ,field: str, data):
        json_data = { "days_before" : 0 }
        r = requests.get(self.daily_url,json=json_data)
        return r.json()

    def search_all_data(self, field: str, data):
       r = requests.get(self.daily_all_url)
    #    user_daily_all = r.json()
    #    json_data = { "days_before" : 365 }
    #    r=requests.get(self.daily_url,json=json_data)
    #    user_daily_all.update({"daily_info" : r.json()})
       return r.json()

if __name__ == "__main__":
    user_id = "u_test12348"
    # user_id = 'aa'
    # user_id = "u_test12345"
    u=Userdata(user_id)
    # print(u.update_data('bmr', 1600))
    # print(u.delete_data())
    # d=Dailydata(user_id)
    # user = u.add_data(name="test", gender=True, age=20, weight=60, height=160, activity_level=1.2)
    print(u.search_data('aaa','bbb'))
    # print(u.get_all_columns())
    # dailyinfo = d.add_data(food_name = '漢堡',food_calories= 200)
    # dailyinfo = d.add_data(exercise_name = '爬山',exercise_duration= 200)
    # dailyinfo = d.search_all_data('aaa','bbb')
    # print(dailyinfo)
    


