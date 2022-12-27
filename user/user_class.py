import json
import webbrowser
import os
import time
from passwort_manager.hash_imput import hash_in
from sourse.sql_probe import add_to_tabel, create_table, print_tabel


class User:
    def __init__(self, name, password=None):
        self.name = name
        self.lower_name = name.lower()
        self.password = password
        self.rank = None
        self.lang = None
        self.plot = None
        self.accs = None

    def load_user(self):
        with open(r'../user/'+ self.lower_name + '/' + self.lower_name +'.json') as directory:
            user_data = json.load(directory)
        self.password = user_data["user"]["password"]
        self.rank = user_data["user"]["rank"]
        self.lang = user_data["user"]["language"]
        self.plot = user_data["data_stats"]["last_plot"]
        self.accs = user_data["user"]["accs"]

    def load_tmp_for_user(self):
        os.makedirs(r'../user/'+ self.lower_name)
        f = open(r'../user/' + self.lower_name + '/' + self.lower_name + '.json', 'x')
        f.close()
        with open(r'../user/user_tmp/username_tmp.json', 'r') as tamplate:
            data = json.load(tamplate)

        time.sleep(0.3)

        with open(r'../user/'+ self.lower_name+ '/'+ self.lower_name+'.json', 'r+') as user_json:
            #vvv = json.load(user_json)
            #vvv.update(data)
            user_json.write(json.dumps(data, indent=4))

        time.sleep(0.3)

        create_table(self)

    def save_plot(self, last_plot):
        with open(r'../user/'+ self.lower_name +'/'+ self.lower_name +'.json', 'r+') as last_plot_data:
            dada = json.load(last_plot_data)
            dada["data_stats"]["last_plot"] = last_plot
        with open(r'../user/'+ self.lower_name +'/'+ self.lower_name +'.json', 'r+') as last_plot_data_2:
            json.dump(dada, last_plot_data_2, indent=4)


    def append_data_json(self, amount, date, info):
        with open(r'../user/'+ self.lower_name +'/data.json', 'r+') as raw_append_data:
            convert_append_data = json.load(raw_append_data)
            tmp = {"paymentx": {"amount": amount,"money": 210,"date": date,"reason": info}}
            convert_append_data["paymentx"] = tmp
            #raw_append_data.write(json.dump(convert_append_data, raw_append_data, indent=4))
            convert_append_data.update(convert_append_data, indent=4)
            json.dump(convert_append_data, raw_append_data)

    def append_data_sql(self, amount, date, info):
        add_to_tabel(self.lower_name, (amount, date, info))

    def print_data(self):
        print_tabel(self)

    



# webbrowser.open(r'C:\Users\Felix\VS Code Projekts\Buchhaltung\web\buch_in_web.html', new=new)
# webbrowser.open(r'C:\Users\Felix\VS Code Projekts\Buchhaltung\web\in_web.html', new=new)


# user1 = User('user/felix.json', 'Felix', 'xxxxxx')
# d1 = user1.datei
# n1 = user1.name
# p1 = user1.password

# with open('user/felix.json') as luser_datei:
#     data = json.load(luser_datei)

# data["User"]["datei"] = d1
# data["User"]["name"] = n1
# data["User"]["password"] = p1

# with open('user/felix.json', 'w') as user_datei:
#     user_datei.write(json.dumps(data, indent=4))
# kommentae