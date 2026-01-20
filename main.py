import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk, ImageDraw
import math

class AnimalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Животные России по регионам")
        self.root.geometry("1100x750")
        
        # Данные о животных по всем регионам с улучшенными цветами
        self.regions_data = {
            "Московская область": {
                "Лось": {
                    "facts": [
                        "Ежедневно съедает до 50 кг растительности — как целый стог сена!",
                        "Рога есть только у самцов, они сбрасывают их каждую зиму, а весной отращивают новые.",
                        "Отлично плавает и может нырять на глубину до 5 метров."
                    ],
                    "status": "Обычный вид в подмосковных лесах",
                    "color1": "#8B4513",  # Коричневый для тела
                    "color2": "#D2691E",  # Более светлый для деталей
                    "bg_color": "#E8F5E9"  # Светло-зеленый фон леса
                },
                "Лисица": {
                    "facts": [
                        "Охотится, используя магнитное поле Земли",
                        "Пушистый хвост служит 'одеялом' в морозы",
                        "Может слышать мышиный писк за 100 метров под снегом"
                    ],
                    "status": "Частый гость на окраинах городов",
                    "color1": "#FF8C00",  # Ярко-оранжевый
                    "color2": "#FFA500",  # Оранжевый
                    "bg_color": "#FFF3E0"  # Светло-оранжевый фон
                },
                "Ёж обыкновенный": {
                    "facts": [
                        "За ночь может пройти до 3 км в поисках пищи",
                        "На иголках может жить до 1000 клещей одновременно",
                        "Умеет плавать и лазать по сетчатым заборам"
                    ],
                    "status": "Обитает в парках и лесопарках",
                    "color1": "#556B2F",  # Темно-оливковый
                    "color2": "#6B8E23",  # Оливковый
                    "bg_color": "#F1F8E9"  # Очень светлый зеленый
                }
            },
            "Краснодарский край": {
                "Дельфин афалина": {
                    "facts": [
                        "Дельфины 'дразнят' ядовитую рыбу фугу для получения наркотического эффекта",
                        "Спят с одним открытым глазом",
                        "Имеют индивидуальные имена-сигналы"
                    ],
                    "status": "Обитатель Черного моря",
                    "color1": "#4682B4",  # Стальной синий
                    "color2": "#87CEEB",  # Небесно-голубой
                    "bg_color": "#E3F2FD"  # Очень светлый синий (море)
                },
                "Кавказский зубр": {
                    "facts": [
                        "Последний дикий бык Европы, весом до тонны",
                        "У зубров есть свой 'детский сад'",
                        "Зимой разгребают снег диаметром до 3 метров"
                    ],
                    "status": "Редкий вид в Кавказском заповеднике",
                    "color1": "#654321",  # Темно-коричневый
                    "color2": "#8B4513",  # Коричневый
                    "bg_color": "#F5F5DC"  # Бежевый (горные луга)
                }
            },
            "Иркутская область": {
                "Байкальская нерпа": {
                    "facts": [
                        "Единственное млекопитающее озера Байкал",
                        "Может нырять на глубину до 300 метров",
                        "Детеныши рождаются в снежных норах"
                    ],
                    "status": "Эндемик Байкала",
                    "color1": "#708090",  # Серый
                    "color2": "#A9A9A9",  # Темно-серый
                    "bg_color": "#E0F2F1"  # Светлый голубой (байкальский лед)
                },
                "Сибирская косуля": {
                    "facts": [
                        "Совершает миграции до 500 км",
                        "Может развивать скорость до 60 км/ч",
                        "Самцы сбрасывают рога в ноябре"
                    ],
                    "status": "Многочисленный вид тайги",
                    "color1": "#D2691E",  # Шоколадный
                    "color2": "#CD853F",  # Перу
                    "bg_color": "#F1F8E9"  # Светло-зеленый (тайга)
                }
            },
            "Сахалинская область": {
                "Калан": {
                    "facts": [
                        "Использует камни как орудия труда",
                        "Самый густой мех в животном мире",
                        "Детенышей держат на животе"
                    ],
                    "status": "Краснокнижный морской хищник",
                    "color1": "#2F4F4F",  # Темный грифельно-серый
                    "color2": "#696969",  # Тускло-серый
                    "bg_color": "#E0F7FA"  # Очень светлый голубой (океан)
                },
                "Белоплечий орлан": {
                    "facts": [
                        "Самая тяжелая хищная птица России",
                        "Строит гнезда до 3 метров в диаметре",
                        "Питается почти исключительно рыбой"
                    ],
                    "status": "Гнездится только на Дальнем Востоке",
                    "color1": "#000000",  # Черный
                    "color2": "#2F4F4F",  # Темный грифельно-серый
                    "bg_color": "#FFFDE7"  # Светло-желтый (скалы)
                }
            },
            "Крым": {
                "Крымский олень": {
                    "facts": [
                        "Рога самцов достигают 12 кг",
                        "Рев слышен за 5 км",
                        "Могут пить солоноватую воду"
                    ],
                    "status": "Эндемичный подвид, символ Крыма",
                    "color1": "#8B4513",  # Коричневый
                    "color2": "#A0522D",  # Сиена
                    "bg_color": "#FFF3E0"  # Светло-оранжевый (крымские горы)
                },
                "Степной сурок": {
                    "facts": [
                        "Спит 8-9 месяцев в году",
                        "Свистят при опасности с разной частотой",
                        "Роют норы до 5 метров глубиной"
                    ],
                    "status": "Обитатель крымских степей",
                    "color1": "#A0522D",  # Сиена
                    "color2": "#D2691E",  # Шоколадный
                    "bg_color": "#F5F5DC"  # Бежевый (степь)
                }
            }
        }
        
        # Словарь городов
        self.city_to_region = {
            "Москва": "Московская область",
            "Подольск": "Московская область", 
            "Коломна": "Московская область",
            "Химки": "Московская область",
            "Краснодар": "Краснодарский край",
            "Сочи": "Краснодарский край",
            "Новороссийск": "Краснодарский край",
            "Анапа": "Краснодарский край",
            "Иркутск": "Иркутская область",
            "Ангарск": "Иркутская область",
            "Братск": "Иркутская область",
            "Усть-Илимск": "Иркутская область",
            "Южно-Сахалинск": "Сахалинская область",
            "Холмск": "Сахалинская область",
            "Корсаков": "Сахалинская область",
            "Симферополь": "Крым",
            "Севастополь": "Крым",
            "Ялта": "Крым"
        }
        
        # Список для хранения ссылок на изображения
        self.photos = []
        
        # Создаем GUI
        self.create_gui()
        
        # Загружаем первый регион
        self.show_region("Московская область")
    
    def draw_elk(self, color1, color2, bg_color):
        """Создает красивое изображение лося"""
        img = Image.new('RGB', (500, 400), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Рисуем простой фон (лес)
        for i in range(10):
            x = i * 50
            draw.line([(x, 400), (x, 350 - i*10)], fill="#228B22", width=2)
        
        # Тело (эллипс с градиентом)
        body_coords = [150, 150, 350, 280]
        draw.ellipse(body_coords, fill=color1, outline="black", width=2)
        
        # Добавляем текстуру на тело
        for i in range(5):
            x = 170 + i * 30
            y = 180 + (i % 2) * 20
            draw.ellipse([x, y, x+10, y+5], fill=color2, outline=None)
        
        # Шея
        draw.ellipse([300, 130, 380, 210], fill=color1, outline="black", width=2)
        
        # Голова
        head_coords = [350, 140, 420, 200]
        draw.ellipse(head_coords, fill=color1, outline="black", width=2)
        
        # Ветвистые рога
        # Левый рог
        draw.line([380, 140, 360, 80], fill="#8B4513", width=8)
        draw.line([360, 80, 340, 50], fill="#8B4513", width=6)
        draw.line([360, 80, 370, 60], fill="#8B4513", width=6)
        draw.line([340, 50, 330, 30], fill="#8B4513", width=4)
        draw.line([340, 50, 350, 40], fill="#8B4513", width=4)
        
        # Правый рог
        draw.line([390, 140, 410, 80], fill="#8B4513", width=8)
        draw.line([410, 80, 430, 50], fill="#8B4513", width=6)
        draw.line([410, 80, 400, 60], fill="#8B4513", width=6)
        draw.line([430, 50, 440, 30], fill="#8B4513", width=4)
        draw.line([430, 50, 420, 40], fill="#8B4513", width=4)
        
        # Уши
        draw.polygon([(370, 160), (365, 145), (375, 145)], fill=color1, outline="black", width=1)
        draw.polygon([(400, 160), (395, 145), (405, 145)], fill=color1, outline="black", width=1)
        
        # Глаза
        draw.ellipse([375, 170, 385, 180], fill="white", outline="black", width=1)
        draw.ellipse([405, 170, 415, 180], fill="white", outline="black", width=1)
        draw.ellipse([378, 173, 382, 177], fill="black")
        draw.ellipse([408, 173, 412, 177], fill="black")
        
        # Ноздри
        draw.ellipse([390, 190, 395, 195], fill="black")
        draw.ellipse([400, 190, 405, 195], fill="black")
        
        # Ноги с копытами
        leg_positions = [(180, 280), (220, 280), (280, 280), (320, 280)]
        for x, y in leg_positions:
            draw.rectangle([x, y, x+20, y+80], fill=color1, outline="black", width=2)
            draw.rectangle([x, y+80, x+20, y+100], fill="#2F4F4F", outline="black", width=2)  # Копыта
        
        # Хвост
        draw.ellipse([140, 220, 160, 240], fill=color1, outline="black", width=1)
        
        # Надпись
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 28)
            draw.text((250, 330), "ЛОСЬ", fill="#8B0000", anchor="mt", font=font, stroke_width=1, stroke_fill="white")
        except:
            draw.text((230, 330), "ЛОСЬ", fill="#8B0000", anchor="mt")
        
        # Солнце на небе
        draw.ellipse([50, 50, 100, 100], fill="#FFD700", outline="#FF8C00", width=2)
        
        return img
    
    def draw_fox(self, color1, color2, bg_color):
        """Создает красивое изображение лисы"""
        img = Image.new('RGB', (500, 400), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Рисуем закатное небо
        for i in range(5):
            y = i * 80
            color = "#FF" + format(200 - i*30, '02x') + "00"
            draw.rectangle([0, y, 500, y+80], fill=color, outline=None)
        
        # Пушистый хвост (самая яркая часть)
        for i in range(8):
            radius = 50 - i * 5
            draw.ellipse([100-i*2, 180-i*2, 100+radius, 180+radius], 
                        fill=color1, outline=color2, width=1)
        
        # Тело
        body_coords = [200, 180, 350, 280]
        draw.ellipse(body_coords, fill=color1, outline="black", width=2)
        
        # Добавляем меховую текстуру
        for i in range(10):
            x = 220 + i * 10
            y = 200 + (i % 3) * 10
            draw.line([(x, y), (x+5, y+5)], fill=color2, width=2)
        
        # Голова (остроконечная)
        draw.polygon([(350, 220), (400, 200), (400, 240)], fill=color1, outline="black", width=2)
        
        # Уши
        draw.polygon([(390, 195), (400, 170), (410, 195)], fill=color1, outline="black", width=1)
        draw.polygon([(410, 195), (420, 170), (430, 195)], fill=color1, outline="black", width=1)
        
        # Глаза (хитрые)
        draw.ellipse([370, 215, 380, 225], fill="white", outline="black", width=1)
        draw.ellipse([410, 215, 420, 225], fill="white", outline="black", width=1)
        draw.ellipse([373, 218, 377, 222], fill="#FF4500")
        draw.ellipse([413, 218, 417, 222], fill="#FF4500")
        
        # Нос
        draw.ellipse([395, 235, 405, 245], fill="black")
        
        # Усы
        for i in range(3):
            draw.line([(395, 240), (380 - i*5, 230 + i*5)], fill="white", width=1)
            draw.line([(405, 240), (420 + i*5, 230 + i*5)], fill="white", width=1)
        
        # Лапы
        for i, x in enumerate([220, 260, 300, 340]):
            draw.ellipse([x, 280, x+20, 300], fill=color1, outline="black", width=1)
            draw.ellipse([x+5, 300, x+15, 320], fill="#2F4F4F", outline="black", width=1)
        
        # Надпись
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 28)
            draw.text((250, 330), "ЛИСИЦА", fill="#8B0000", anchor="mt", font=font, stroke_width=1, stroke_fill="white")
        except:
            draw.text((230, 330), "ЛИСИЦА", fill="#8B0000", anchor="mt")
        
        # Луна на небе
        draw.ellipse([400, 50, 450, 100], fill="#F0F8FF", outline="#C0C0C0", width=2)
        
        return img
    
    def draw_hedgehog(self, color1, color2, bg_color):
        """Создает красивое изображение ежа"""
        img = Image.new('RGB', (500, 400), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Рисуем лесную подстилку
        for i in range(20):
            x = i * 25
            draw.line([(x, 400), (x+10, 350)], fill="#8B4513", width=1)
        
        # Тело (полукруг)
        body_coords = [150, 150, 350, 300]
        draw.ellipse(body_coords, fill=color1, outline="black", width=2)
        
        # Иголки (много треугольников)
        for i in range(15):
            angle = i * 24  # 360/15
            rad = math.radians(angle)
            x_center = 250
            y_center = 200
            
            # Координаты для треугольника-иголки
            x1 = x_center + 100 * math.cos(rad)
            y1 = y_center + 100 * math.sin(rad)
            x2 = x_center + 120 * math.cos(rad + 0.2)
            y2 = y_center + 120 * math.sin(rad + 0.2)
            x3 = x_center + 120 * math.cos(rad - 0.2)
            y3 = y_center + 120 * math.sin(rad - 0.2)
            
            draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill="#696969", outline="black", width=1)
        
        # Мордочка
        draw.ellipse([350, 200, 420, 270], fill="#DEB887", outline="black", width=2)
        
        # Глаза
        draw.ellipse([370, 230, 380, 240], fill="white", outline="black", width=1)
        draw.ellipse([390, 230, 400, 240], fill="white", outline="black", width=1)
        draw.ellipse([372, 233, 378, 237], fill="black")
        draw.ellipse([392, 233, 398, 237], fill="black")
        
        # Нос
        draw.ellipse([410, 250, 420, 260], fill="black")
        
        # Улыбка
        draw.arc([370, 255, 410, 275], start=0, end=180, fill="black", width=2)
        
        # Лапки
        for x in [180, 220, 280, 320]:
            draw.ellipse([x, 300, x+20, 320], fill=color1, outline="black", width=1)
            draw.ellipse([x+5, 320, x+15, 335], fill="#8B4513", outline="black", width=1)
        
        # Яблоко (ёжик несет яблоко)
        draw.ellipse([100, 200, 140, 240], fill="#FF0000", outline="#8B0000", width=2)
        draw.line([(120, 190), (120, 200)], fill="#228B22", width=3)
        draw.ellipse([118, 185, 122, 189], fill="#228B22")
        
        # Листики на земле
        for i in range(10):
            x = 50 + i * 40
            y = 350 + (i % 2) * 20
            draw.ellipse([x, y, x+15, y+10], fill="#228B22", outline=None)
        
        # Надпись
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 28)
            draw.text((250, 350), "ЁЖ", fill="#006400", anchor="mt", font=font, stroke_width=1, stroke_fill="white")
        except:
            draw.text((240, 350), "ЁЖ", fill="#006400", anchor="mt")
        
        return img
    
    def draw_dolphin(self, color1, color2, bg_color):
        """Создает красивое изображение дельфина"""
        img = Image.new('RGB', (500, 400), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Рисуем волны
        for i in range(10):
            y = 300 + i * 5
            draw.line([(0, y), (500, y + math.sin(i)*10)], fill="#1E90FF", width=2)
        
        # Тело дельфина (изогнутое)
        # Основное тело
        draw.ellipse([100, 150, 400, 250], fill=color1, outline="black", width=2)
        
        # Голова
        draw.polygon([(400, 200), (450, 180), (450, 220)], fill=color1, outline="black", width=2)
        
        # Хвост
        draw.polygon([(100, 200), (60, 170), (60, 230)], fill=color1, outline="black", width=2)
        
        # Спинной плавник
        draw.polygon([(250, 150), (270, 100), (290, 150)], fill=color1, outline="black", width=2)
        
        # Боковые плавники
        draw.polygon([(200, 250), (180, 280), (220, 280)], fill=color1, outline="black", width=2)
        draw.polygon([(300, 250), (280, 280), (320, 280)], fill=color1, outline="black", width=2)
        
        # Глаз
        draw.ellipse([430, 195, 440, 205], fill="white", outline="black", width=1)
        draw.ellipse([432, 197, 438, 203], fill="black")
        
        # Улыбка
        draw.arc([410, 210, 450, 230], start=0, end=180, fill="black", width=2)
        
        # Дыхало
        draw.ellipse([420, 180, 430, 190], fill="black")
        
        # Добавляем блики на теле
        draw.ellipse([300, 180, 350, 200], fill=color2, outline=None)
        
        # Брызги воды
        for i in range(20):
            x = 450 + (i % 3) * 10
            y = 180 - (i // 2) * 5
            draw.ellipse([x, y, x+3, y+3], fill="#87CEEB", outline=None)
        
        # Надпись
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 28)
            draw.text((250, 320), "ДЕЛЬФИН", fill="#00008B", anchor="mt", font=font, stroke_width=1, stroke_fill="white")
        except:
            draw.text((230, 320), "ДЕЛЬФИН", fill="#00008B", anchor="mt")
        
        # Солнце над водой
        draw.ellipse([400, 50, 450, 100], fill="#FFD700", outline="#FF8C00", width=3)
        
        return img
    
    def draw_bison(self, color1, color2, bg_color):
        """Создает красивое изображение зубра"""
        img = Image.new('RGB', (500, 400), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Рисуем горный фон
        for i in range(3):
            x = i * 150
            draw.polygon([(x, 400), (x+75, 300 - i*20), (x+150, 400)], fill="#808080", outline="black", width=1)
        
        # Мощное тело
        body_coords = [150, 180, 350, 300]
        draw.ellipse(body_coords, fill=color1, outline="black", width=3)
        
        # Голова
        head_coords = [300, 150, 420, 230]
        draw.ellipse(head_coords, fill=color1, outline="black", width=3)
        
        # Рога (массивные)
        # Левый рог
        draw.line([340, 170, 320, 130], fill="#2F4F4F", width=10)
        draw.line([320, 130, 310, 100], fill="#2F4F4F", width=8)
        
        # Правый рог
        draw.line([380, 170, 400, 130], fill="#2F4F4F", width=10)
        draw.line([400, 130, 410, 100], fill="#2F4F4F", width=8)
        
        # Грива (густая)
        for i in range(15):
            y = 150 + i * 5
            draw.line([(300, y), (280, y-10)], fill=color2, width=4)
        
        # Глаза
        draw.ellipse([350, 190, 360, 200], fill="white", outline="black", width=1)
        draw.ellipse([370, 190, 380, 200], fill="white", outline="black", width=1)
        draw.ellipse([352, 193, 358, 197], fill="#8B0000")
        draw.ellipse([372, 193, 378, 197], fill="#8B0000")
        
        # Ноздри
        draw.ellipse([390, 210, 395, 215], fill="black")
        draw.ellipse([400, 210, 405, 215], fill="black")
        
        # Ноги (толстые)
        leg_positions = [(180, 300), (220, 300), (280, 300), (320, 300)]
        for x, y in leg_positions:
            draw.rectangle([x, y, x+25, y+80], fill=color1, outline="black", width=2)
            draw.rectangle([x, y+80, x+25, y+100], fill="#2F4F4F", outline="black", width=3)  # Копыта
        
        # Хвост
        draw.line([150, 240, 120, 250], fill=color1, width=8)
        draw.ellipse([115, 245, 125, 255], fill=color1)
        
        # Надпись
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 28)
            draw.text((250, 330), "КАВКАЗСКИЙ ЗУБР", fill="#8B0000", anchor="mt", font=font, stroke_width=1, stroke_fill="white")
        except:
            draw.text((200, 330), "КАВКАЗСКИЙ ЗУБР", fill="#8B0000", anchor="mt")
        
        return img
    
    def draw_seal(self, color1, color2, bg_color):
        """Создает красивое изображение нерпы"""
        img = Image.new('RGB', (500, 400), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Рисуем ледяные глыбы
        for i in range(5):
            x = i * 100
            draw.ellipse([x, 300, x+80, 350], fill="#ADD8E6", outline="#87CEEB", width=2)
        
        # Тело нерпы (торпедообразное)
        body_coords = [150, 180, 350, 280]
        draw.ellipse(body_coords, fill=color1, outline="black", width=2)
        
        # Голова
        head_coords = [350, 210, 420, 260]
        draw.ellipse(head_coords, fill=color1, outline="black", width=2)
        
        # Глаза (большие и темные)
        draw.ellipse([370, 230, 380, 240], fill="white", outline="black", width=1)
        draw.ellipse([390, 230, 400, 240], fill="white", outline="black", width=1)
        draw.ellipse([372, 233, 378, 237], fill="#000080")
        draw.ellipse([392, 233, 398, 237], fill="#000080")
        
        # Усы
        for i in range(5):
            draw.line([(360, 250), (340 - i*3, 245 + i*2)], fill="white", width=1)
            draw.line([(360, 250), (340 - i*3, 255 - i*2)], fill="white", width=1)
        
        # Ноздри
        draw.ellipse([375, 255, 380, 260], fill="black")
        draw.ellipse([385, 255, 390, 260], fill="black")
        
        # Ласты
        # Передние
        draw.ellipse([170, 230, 220, 260], fill=color1, outline="black", width=1)
        draw.ellipse([280, 230, 330, 260], fill=color1, outline="black", width=1)
        
        # Задние
        draw.polygon([(150, 230), (130, 220), (130, 240)], fill=color1, outline="black", width=1)
        
        # Пятна на теле
        spots = [(200, 220), (250, 200), (300, 220), (220, 250)]
        for x, y in spots:
            draw.ellipse([x, y, x+20, y+20], fill=color2, outline="black", width=1)
        
        # Отверстие во льду
        draw.ellipse([400, 280, 480, 340], fill="#00008B", outline="#000080", width=3)
        
        # Надпись
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 28)
            draw.text((250, 320), "БАЙКАЛЬСКАЯ НЕРПА", fill="#000080", anchor="mt", font=font, stroke_width=1, stroke_fill="white")
        except:
            draw.text((200, 320), "БАЙКАЛЬСКАЯ НЕРПА", fill="#000080", anchor="mt")
        
        # Снежинки в воздухе
        for i in range(20):
            x = (i * 25) % 500
            y = (i * 20) % 200
            draw.line([(x, y), (x+3, y+3)], fill="white", width=1)
            draw.line([(x+3, y), (x, y+3)], fill="white", width=1)
        
        return img
    
    def draw_roe_deer(self, color1, color2, bg_color):
        """Создает красивое изображение косули"""
        img = Image.new('RGB', (500, 400), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Рисуем таежный лес на заднем плане
        for i in range(10):
            x = i * 50
            draw.polygon([(x, 400), (x+25, 250 - (i%3)*30), (x+50, 400)], fill="#228B22", outline="#006400", width=1)
        
        # Изящное тело
        body_coords = [180, 180, 320, 260]
        draw.ellipse(body_coords, fill=color1, outline="black", width=2)
        
        # Шея
        draw.ellipse([300, 160, 360, 220], fill=color1, outline="black", width=2)
        
        # Голова
        head_coords = [340, 170, 400, 210]
        draw.ellipse(head_coords, fill=color1, outline="black", width=2)
        
        # Уши (длинные и заостренные)
        draw.polygon([(360, 170), (355, 150), (365, 150)], fill=color1, outline="black", width=1)
        draw.polygon([(380, 170), (375, 150), (385, 150)], fill=color1, outline="black", width=1)
        
        # Рожки (маленькие, ветвистые)
        # Левый рог
        draw.line([360, 170, 360, 160], fill="#8B4513", width=4)
        draw.line([360, 160, 355, 155], fill="#8B4513", width=3)
        draw.line([360, 160, 365, 155], fill="#8B4513", width=3)
        
        # Правый рог
        draw.line([380, 170, 380, 160], fill="#8B4513", width=4)
        draw.line([380, 160, 375, 155], fill="#8B4513", width=3)
        draw.line([380, 160, 385, 155], fill="#8B4513", width=3)
        
        # Глаза (большие и выразительные)
        draw.ellipse([365, 185, 375, 195], fill="white", outline="black", width=1)
        draw.ellipse([385, 185, 395, 195], fill="white", outline="black", width=1)
        draw.ellipse([368, 188, 372, 192], fill="#8B0000")
        draw.ellipse([388, 188, 392, 192], fill="#8B0000")
        
        # Ноздри
        draw.ellipse([370, 200, 375, 205], fill="black")
        draw.ellipse([380, 200, 385, 205], fill="black")
        
        # Ноги (тонкие и изящные)
        leg_positions = [(200, 260), (230, 260), (270, 260), (300, 260)]
        for x, y in leg_positions:
            draw.rectangle([x, y, x+15, y+90], fill=color1, outline="black", width=1)
            draw.rectangle([x, y+90, x+15, y+100], fill="#2F4F4F", outline="black", width=2)  # Копытца
        
        # Хвостик (маленький)
        draw.ellipse([170, 240, 180, 250], fill=color1)
        
        # Белое пятно на задней части
        draw.ellipse([180, 220, 210, 250], fill=color2, outline=None)
        
        # Надпись
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 28)
            draw.text((250, 330), "СИБИРСКАЯ КОСУЛЯ", fill="#006400", anchor="mt", font=font, stroke_width=1, stroke_fill="white")
        except:
            draw.text((210, 330), "СИБИРСКАЯ КОСУЛЯ", fill="#006400", anchor="mt")
        
        return img
    
    def draw_sea_otter(self, color1, color2, bg_color):
        """Создает красивое изображение калана (морской выдры)"""
        img = Image.new('RGB', (500, 400), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Рисуем океанские волны
        for i in range(8):
            y = 300 + i * 10
            amplitude = 20 * math.sin(i * 0.5)
            draw.line([(0, y), (500, y + amplitude)], fill="#4169E1", width=3)
        
        # Тело калана (длинное и гибкое)
        body_coords = [150, 200, 350, 280]
        draw.ellipse(body_coords, fill=color1, outline="black", width=2)
        
        # Голова
        head_coords = [350, 210, 420, 260]
        draw.ellipse(head_coords, fill=color1, outline="black", width=2)
        
        # Уши (маленькие)
        draw.ellipse([360, 215, 370, 225], fill=color1, outline="black", width=1)
        draw.ellipse([380, 215, 390, 225], fill=color1, outline="black", width=1)
        
        # Глаза
        draw.ellipse([370, 235, 380, 245], fill="white", outline="black", width=1)
        draw.ellipse([390, 235, 400, 245], fill="white", outline="black", width=1)
        draw.ellipse([372, 238, 378, 242], fill="#8B4513")
        draw.ellipse([392, 238, 398, 242], fill="#8B4513")
        
        # Нос
        draw.ellipse([405, 250, 415, 260], fill="black")
        
        # Лапы с перепонками
        # Передние лапы
        draw.ellipse([200, 230, 240, 270], fill=color1, outline="black", width=1)
        draw.ellipse([260, 230, 300, 270], fill=color1, outline="black", width=1)
        
        # Задние лапы
        draw.ellipse([150, 250, 190, 290], fill=color1, outline="black", width=1)
        
        # Хвост (длинный)
        draw.ellipse([130, 230, 170, 270], fill=color1, outline="black", width=1)
        
        # Камень в лапах (каланы используют камни как инструменты)
        draw.ellipse([250, 180, 280, 210], fill="#696969", outline="#2F4F4F", width=2)
        
        # Морская ракушка
        draw.ellipse([270, 190, 290, 210], fill="#FFE4C4", outline="#DEB887", width=1)
        
        # Надпись
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 28)
            draw.text((250, 320), "КАЛАН", fill="#000080", anchor="mt", font=font, stroke_width=1, stroke_fill="white")
        except:
            draw.text((240, 320), "КАЛАН", fill="#000080", anchor="mt")
        
        # Водоросли на дне
        for i in range(10):
            x = i * 50
            draw.line([(x, 400), (x+10, 320)], fill="#228B22", width=3)
            draw.ellipse([x+5, 315, x+15, 325], fill="#228B22", outline=None)
        
        return img
    
    def draw_eagle(self, color1, color2, bg_color):
        """Создает красивое изображение белоплечего орлана"""
        img = Image.new('RGB', (500, 400), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Рисуем скалистый берег
        for i in range(5):
            x = i * 100
            draw.polygon([(x, 400), (x+50, 300 - i*30), (x+100, 400)], fill="#A9A9A9", outline="#696969", width=2)
        
        # Тело орлана
        body_coords = [200, 150, 300, 250]
        draw.ellipse(body_coords, fill=color1, outline="black", width=2)
        
        # Крылья (распростертые)
        # Левое крыло
        draw.polygon([(200, 200), (100, 100), (50, 200), (200, 250)], fill=color1, outline="black", width=2)
        
        # Правое крыло
        draw.polygon([(300, 200), (400, 100), (450, 200), (300, 250)], fill=color1, outline="black", width=2)
        
        # Белые плечи (характерная черта)
        draw.ellipse([180, 160, 220, 200], fill="white", outline="black", width=1)
        draw.ellipse([280, 160, 320, 200], fill="white", outline="black", width=1)
        
        # Голова
        head_coords = [250, 100, 310, 160]
        draw.ellipse(head_coords, fill=color1, outline="black", width=2)
        
        # Клюв (мощный, желтый)
        draw.polygon([(280, 130), (330, 140), (280, 150)], fill="#FFD700", outline="#B8860B", width=2)
        
        # Глаза (острые)
        draw.ellipse([270, 130, 280, 140], fill="white", outline="black", width=1)
        draw.ellipse([290, 130, 300, 140], fill="white", outline="black", width=1)
        draw.ellipse([272, 132, 278, 138], fill="#FF4500")
        draw.ellipse([292, 132, 298, 138], fill="#FF4500")
        
        # Лапы с когтями
        draw.line([(250, 250), (240, 300)], fill="#FFD700", width=5)
        draw.line([(250, 250), (260, 300)], fill="#FFD700", width=5)
        
        # Когти
        for i in range(3):
            draw.line([(240, 300), (235 - i*3, 310 + i*5)], fill="#B8860B", width=2)
            draw.line([(260, 300), (265 + i*3, 310 + i*5)], fill="#B8860B", width=2)
        
        # Хвост (веерообразный)
        draw.polygon([(200, 250), (250, 300), (300, 250)], fill=color1, outline="black", width=2)
        
        # Рыба в когтях (орлан питается рыбой)
        draw.ellipse([230, 280, 270, 310], fill="#87CEEB", outline="#4682B4", width=1)
        draw.polygon([(270, 295), (290, 290), (290, 300)], fill="#87CEEB", outline="#4682B4", width=1)
        
        # Надпись
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 24)
            draw.text((250, 330), "БЕЛОПЛЕЧИЙ ОРЛАН", fill="#000080", anchor="mt", font=font, stroke_width=1, stroke_fill="white")
        except:
            draw.text((200, 330), "БЕЛОПЛЕЧИЙ ОРЛАН", fill="#000080", anchor="mt")
        
        # Облака в небе
        for i in range(3):
            x = 50 + i * 150
            draw.ellipse([x, 50, x+60, 80], fill="white", outline="#D3D3D3", width=1)
        
        return img
    
    def draw_crimean_deer(self, color1, color2, bg_color):
        """Создает красивое изображение крымского оленя"""
        img = Image.new('RGB', (500, 400), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Рисуем крымские горы
        draw.polygon([(0, 400), (100, 200), (200, 400)], fill="#696969", outline="#2F4F4F", width=2)
        draw.polygon([(150, 400), (250, 250), (350, 400)], fill="#808080", outline="#696969", width=2)
        draw.polygon([(300, 400), (400, 280), (500, 400)], fill="#A9A9A9", outline="#808080", width=2)
        
        # Статное тело
        body_coords = [180, 200, 320, 300]
        draw.ellipse(body_coords, fill=color1, outline="black", width=2)
        
        # Шея
        draw.ellipse([300, 180, 360, 240], fill=color1, outline="black", width=2)
        
        # Голова
        head_coords = [340, 190, 400, 230]
        draw.ellipse(head_coords, fill=color1, outline="black", width=2)
        
        # Величественные рога
        # Основание рогов
        draw.line([360, 190, 360, 170], fill="#8B4513", width=6)
        draw.line([380, 190, 380, 170], fill="#8B4513", width=6)
        
        # Ветви левого рога
        draw.line([360, 170, 340, 150], fill="#8B4513", width=5)
        draw.line([340, 150, 320, 130], fill="#8B4513", width=4)
        draw.line([340, 150, 350, 130], fill="#8B4513", width=4)
        draw.line([360, 170, 370, 140], fill="#8B4513", width=5)
        draw.line([370, 140, 380, 120], fill="#8B4513", width=4)
        
        # Ветви правого рога
        draw.line([380, 170, 400, 150], fill="#8B4513", width=5)
        draw.line([400, 150, 420, 130], fill="#8B4513", width=4)
        draw.line([400, 150, 390, 130], fill="#8B4513", width=4)
        draw.line([380, 170, 390, 140], fill="#8B4513", width=5)
        draw.line([390, 140, 400, 120], fill="#8B4513", width=4)
        
        # Уши
        draw.polygon([(370, 200), (365, 185), (375, 185)], fill=color1, outline="black", width=1)
        draw.polygon([(390, 200), (385, 185), (395, 185)], fill=color1, outline="black", width=1)
        
        # Глаза
        draw.ellipse([365, 210, 375, 220], fill="white", outline="black", width=1)
        draw.ellipse([385, 210, 395, 220], fill="white", outline="black", width=1)
        draw.ellipse([367, 213, 373, 217], fill="#8B0000")
        draw.ellipse([387, 213, 393, 217], fill="#8B0000")
        
        # Ноздри
        draw.ellipse([375, 225, 380, 230], fill="black")
        draw.ellipse([385, 225, 390, 230], fill="black")
        
        # Ноги
        leg_positions = [(200, 300), (230, 300), (270, 300), (300, 300)]
        for x, y in leg_positions:
            draw.rectangle([x, y, x+20, y+70], fill=color1, outline="black", width=2)
            draw.rectangle([x, y+70, x+20, y+80], fill="#2F4F4F", outline="black", width=2)
        
        # Хвост
        draw.ellipse([170, 280, 180, 290], fill=color1)
        
        # Надпись
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 28)
            draw.text((250, 330), "КРЫМСКИЙ ОЛЕНЬ", fill="#8B0000", anchor="mt", font=font, stroke_width=1, stroke_fill="white")
        except:
            draw.text((220, 330), "КРЫМСКИЙ ОЛЕНЬ", fill="#8B0000", anchor="mt")
        
        # Кипарисы (характерные для Крыма)
        for i in range(3):
            x = 50 + i * 150
            draw.polygon([(x, 400), (x+10, 250), (x+20, 400)], fill="#006400", outline="#004d00", width=1)
        
        return img
    
    def draw_marmot(self, color1, color2, bg_color):
        """Создает красивое изображение степного сурка"""
        img = Image.new('RGB', (500, 400), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Рисуем степной пейзаж
        for i in range(20):
            y = 350 + (i % 2) * 10
            draw.line([(i*25, y), (i*25+20, y-5)], fill="#8B4513", width=2)
        
        # Пухлое тело сурка
        body_coords = [200, 180, 300, 280]
        draw.ellipse(body_coords, fill=color1, outline="black", width=2)
        
        # Голова
        head_coords = [280, 190, 340, 230]
        draw.ellipse(head_coords, fill=color1, outline="black", width=2)
        
        # Уши (круглые)
        draw.ellipse([290, 185, 300, 195], fill=color1, outline="black", width=1)
        draw.ellipse([310, 185, 320, 195], fill=color1, outline="black", width=1)
        
        # Глаза (маленькие)
        draw.ellipse([295, 205, 300, 210], fill="black")
        draw.ellipse([315, 205, 320, 210], fill="black")
        
        # Нос
        draw.ellipse([305, 215, 315, 225], fill="black")
        
        # Усы
        for i in range(4):
            draw.line([(305, 220), (290 - i*3, 210 + i*2)], fill="white", width=1)
            draw.line([(315, 220), (330 + i*3, 210 + i*2)], fill="white", width=1)
        
        # Лапы
        # Передние лапы (сурки часто стоят столбиком)
        draw.ellipse([240, 280, 260, 300], fill=color1, outline="black", width=1)
        draw.ellipse([280, 280, 300, 300], fill=color1, outline="black", width=1)
        
        # Задние лапы
        draw.ellipse([220, 260, 240, 280], fill=color1, outline="black", width=1)
        
        # Сурок стоит на задних лапах
        draw.line([(250, 280), (250, 320)], fill=color1, width=15)
        draw.line([(290, 280), (290, 320)], fill=color1, width=15)
        
        # Стопы
        draw.ellipse([240, 320, 260, 340], fill=color1, outline="black", width=1)
        draw.ellipse([280, 320, 300, 340], fill=color1, outline="black", width=1)
        
        # Хвост (пушистый)
        draw.ellipse([190, 230, 210, 250], fill=color1, outline="black", width=1)
        
        # Нора сурка
        draw.ellipse([100, 300, 180, 350], fill="#8B4513", outline="#654321", width=3)
        
        # Сурок держит цветок (степной)
        draw.line([(330, 210), (350, 180)], fill="#228B22", width=3)
        draw.ellipse([345, 170, 355, 180], fill="#FF69B4", outline="#C71585", width=1)
        
        # Надпись
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 28)
            draw.text((250, 350), "СТЕПНОЙ СУРОК", fill="#8B4513", anchor="mt", font=font, stroke_width=1, stroke_fill="white")
        except:
            draw.text((220, 350), "СТЕПНОЙ СУРОК", fill="#8B4513", anchor="mt")
        
        # Солнце над степью
        draw.ellipse([400, 50, 450, 100], fill="#FFD700", outline="#FF8C00", width=3)
        
        return img
    
    def create_animal_image(self, animal_name, color1, color2, bg_color):
        """Создает изображение животного по его названию"""
        if animal_name == "Лось":
            return self.draw_elk(color1, color2, bg_color)
        elif animal_name == "Лисица":
            return self.draw_fox(color1, color2, bg_color)
        elif animal_name == "Ёж обыкновенный":
            return self.draw_hedgehog(color1, color2, bg_color)
        elif animal_name == "Дельфин афалина":
            return self.draw_dolphin(color1, color2, bg_color)
        elif animal_name == "Кавказский зубр":
            return self.draw_bison(color1, color2, bg_color)
        elif animal_name == "Байкальская нерпа":
            return self.draw_seal(color1, color2, bg_color)
        elif animal_name == "Сибирская косуля":
            return self.draw_roe_deer(color1, color2, bg_color)
        elif animal_name == "Калан":
            return self.draw_sea_otter(color1, color2, bg_color)
        elif animal_name == "Белоплечий орлан":
            return self.draw_eagle(color1, color2, bg_color)
        elif animal_name == "Крымский олень":
            return self.draw_crimean_deer(color1, color2, bg_color)
        elif animal_name == "Степной сурок":
            return self.draw_marmot(color1, color2, bg_color)
        else:
            # Резервное изображение
            img = Image.new('RGB', (500, 400), color=bg_color)
            draw = ImageDraw.Draw(img)
            draw.ellipse([150, 150, 350, 300], fill=color1, outline="black", width=2)
            try:
                from PIL import ImageFont
                font = ImageFont.truetype("arial.ttf", 28)
                draw.text((250, 350), animal_name.upper(), fill="#8B0000", anchor="mt", font=font, stroke_width=1, stroke_fill="white")
            except:
                draw.text((200, 350), animal_name, fill="#8B0000", anchor="mt")
            return img
    
    def create_gui(self):
        """Создает интерфейс"""
        # Заголовок
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="🦌 Животные России по регионам 🦊",
            font=("Arial", 26, "bold"),
            bg='#2c3e50',
            fg='white'
        ).pack(expand=True)
        
        # Основной контейнер
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Левая панель - выбор региона
        left_panel = tk.Frame(main_frame, width=280, bg='#34495e', relief=tk.RAISED, bd=2)
        left_panel.pack(side=tk.LEFT, fill=tk.Y)
        left_panel.pack_propagate(False)
        
        tk.Label(
            left_panel,
            text="🌍 ВЫБОР РЕГИОНА",
            font=("Arial", 18, "bold"),
            bg='#2c3e50',
            fg='white',
            pady=15
        ).pack(fill=tk.X)
        
        # Кнопки регионов с иконками
        regions_frame = tk.Frame(left_panel, bg='#34495e')
        regions_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        region_icons = {
            "Московская область": "🏰",
            "Краснодарский край": "🌴",
            "Иркутская область": "🏔️",
            "Сахалинская область": "🌊",
            "Крым": "☀️"
        }
        
        for region in self.regions_data.keys():
            icon = region_icons.get(region, "📍")
            btn = tk.Button(
                regions_frame,
                text=f"{icon} {region}",
                command=lambda r=region: self.show_region(r),
                font=("Arial", 12, "bold"),
                width=30,
                pady=12,
                bg='#3498db',
                fg='white',
                relief=tk.RAISED,
                cursor="hand2",
                activebackground='#2980b9',
                bd=3
            )
            btn.pack(pady=6)
        
        # Поиск по городу
        search_frame = tk.Frame(left_panel, bg='#34495e', pady=20)
        search_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            search_frame,
            text="🔍 ПОИСК ПО ГОРОДУ:",
            font=("Arial", 14, "bold"),
            bg='#34495e',
            fg='white'
        ).pack(anchor=tk.W, pady=(0, 8))
        
        self.city_var = tk.StringVar()
        city_combo = ttk.Combobox(
            search_frame,
            textvariable=self.city_var,
            values=list(self.city_to_region.keys()),
            state="readonly",
            font=("Arial", 12),
            height=8
        )
        city_combo.pack(fill=tk.X, pady=(0, 10))
        city_combo.bind('<<ComboboxSelected>>', self.on_city_selected)
        
        # Информация
        info_frame = tk.Frame(left_panel, bg='#2c3e50', relief=tk.SUNKEN, bd=1, pady=10)
        info_frame.pack(fill=tk.X, padx=10, pady=20)
        
        tk.Label(
            info_frame,
            text="ℹ️ Все изображения\nсоздаются программой\nв реальном времени",
            font=("Arial", 10),
            bg='#2c3e50',
            fg='#ecf0f1',
            justify=tk.CENTER
        ).pack(pady=5)
        
        # Правая панель - информация
        right_panel = tk.Frame(main_frame, bg='white')
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Заголовок региона
        self.region_header = tk.Frame(right_panel, bg='#2c3e50', height=70)
        self.region_header.pack(fill=tk.X)
        self.region_header.pack_propagate(False)
        
        self.region_label = tk.Label(
            self.region_header,
            text="ВЫБЕРИТЕ РЕГИОН",
            font=("Arial", 22, "bold"),
            bg='#2c3e50',
            fg='white'
        )
        self.region_label.pack(expand=True)
        
        # Вкладки с животными
        self.notebook = ttk.Notebook(right_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Статус бар
        status_frame = tk.Frame(self.root, bg='#2c3e50', height=35)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="Готов к работе • Изображения генерируются программой • Все животные нарисованы кодом",
            font=("Arial", 10),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        self.status_label.pack(expand=True)
    
    def show_region(self, region_name):
        """Показывает животных выбранного региона"""
        print(f"\n🖼️ Генерация изображений для региона: {region_name}")
        
        # Очищаем старые ссылки
        self.photos = []
        
        # Обновляем заголовок
        self.region_label.config(text=region_name.upper())
        self.status_label.config(text=f"Регион: {region_name} • Рисунки создаются в реальном времени")
        
        # Очищаем вкладки
        for tab in self.notebook.tabs():
            self.notebook.forget(tab)
        
        # Получаем данные региона
        if region_name not in self.regions_data:
            self.show_error(f"Регион '{region_name}' не найден")
            return
        
        animals = self.regions_data[region_name]
        
        # Создаем вкладку для каждого животного
        for animal_name, data in animals.items():
            # Создаем фрейм для вкладки
            tab_frame = tk.Frame(self.notebook, bg='#f5f5f5')
            
            # Генерируем изображение животного
            img = self.create_animal_image(animal_name, data["color1"], data["color2"], data["bg_color"])
            
            # Конвертируем для Tkinter
            photo = ImageTk.PhotoImage(img)
            
            # Сохраняем ссылку
            self.photos.append(photo)
            
            # Верхняя часть с изображением
            image_frame = tk.Frame(tab_frame, bg='#f5f5f5')
            image_frame.pack(fill=tk.BOTH, expand=True, pady=15)
            
            img_label = tk.Label(image_frame, image=photo, bg='#f5f5f5')
            img_label.image = photo
            img_label.pack()
            
            # Нижняя часть с информацией
            info_frame = tk.Frame(tab_frame, bg='white', relief=tk.RAISED, bd=1)
            info_frame.pack(fill=tk.X, padx=20, pady=(0, 15))
            
            # Название животного
            name_frame = tk.Frame(info_frame, bg='#2c3e50')
            name_frame.pack(fill=tk.X, pady=(0, 10))
            
            tk.Label(
                name_frame,
                text=animal_name.upper(),
                font=("Arial", 20, "bold"),
                bg='#2c3e50',
                fg='white',
                pady=12
            ).pack()
            
            # Статус
            status_frame = tk.Frame(info_frame, bg='white', padx=20)
            status_frame.pack(fill=tk.X, pady=(0, 15))
            
            tk.Label(
                status_frame,
                text="📌 Статус:",
                font=("Arial", 14, "bold"),
                bg='white'
            ).pack(side=tk.LEFT)
            
            status_text = tk.Label(
                status_frame,
                text=data['status'],
                font=("Arial", 13, "italic"),
                bg='white',
                fg='#2c3e50',
                wraplength=500
            )
            status_text.pack(side=tk.LEFT, padx=10)
            
            # Интересные факты
            facts_frame = tk.LabelFrame(
                info_frame,
                text="🐾 ИНТЕРЕСНЫЕ ФАКТЫ",
                font=("Arial", 16, "bold"),
                bg='white',
                fg='#2c3e50'
            )
            facts_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
            
            facts_text = scrolledtext.ScrolledText(
                facts_frame,
                wrap=tk.WORD,
                font=("Arial", 12),
                bg='white',
                relief=tk.FLAT,
                height=6
            )
            facts_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Добавляем факты
            for fact in data['facts']:
                facts_text.insert(tk.END, f"• {fact}\n\n")
            
            facts_text.config(state=tk.DISABLED)
            
            # Добавляем вкладку
            self.notebook.add(tab_frame, text=animal_name)
    
    def show_error(self, message):
        """Показывает сообщение об ошибке"""
        error_frame = tk.Frame(self.notebook, bg='white')
        
        tk.Label(
            error_frame,
            text="⚠️ ОШИБКА",
            font=("Arial", 28, "bold"),
            bg='white',
            fg='#e74c3c'
        ).pack(pady=30)
        
        tk.Label(
            error_frame,
            text=message,
            font=("Arial", 16),
            bg='white',
            fg='#2c3e50'
        ).pack(pady=20)
        
        self.notebook.add(error_frame, text="Ошибка")
    
    def on_city_selected(self, event):
        """Обработчик выбора города"""
        city = self.city_var.get()
        if city in self.city_to_region:
            region = self.city_to_region[city]
            self.show_region(region)
            self.status_label.config(text=f"Город: {city} → Регион: {region} • Рисунки создаются в реальном времени")
        else:
            self.show_error(f"Город '{city}' не найден в базе данных")

def main():
    root = tk.Tk()
    app = AnimalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()