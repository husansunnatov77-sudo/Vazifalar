import random
names = ["Abdulazizbek Orifjonov", "Abdulloh Nozimov", "Azizbek Tulegenov", "Behruz Bozorov", 
         "Behruz Ilhomov", "Behruz Kurbonov", "Bobur Ikromjonov","Darmanbek Shamuratov", 
         "Foziljon Mo'minov", "Farrux G'aniboyev", "Jamoliddin Murodullayev", "Muhammadbobur Mansurov",
         "Muhammadali Xoshimov", "Muhammadmuso Qodirov", "Madinaxon Maxmudova", "Madinabonu Axmadjonova",
         "Mohinur Nosirjonova","Og'abek Hasanov", "Rano Yo'ldasheva","Umidjon Murotov","Xusan Sunnatov",
         "Yahyo Ikromov","Zamir Tuygunov","Shamsiddin Xusanov","Shohjahon Soatov","Sherxon Sunnatov"]

def random_name(names_list):
    index = random.randint(0, len(names_list) - 1)
    return names_list.pop(index)

def start():
    while names:
        input("Enter bosing → keyingi talaba tanlanadi")
        print("Tanlangan talaba:", random_name(names))

start()

