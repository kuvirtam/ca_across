SEED = {
	# gui
	"title": "ca_Across", # название окна
	"size": (800, 600), # размер окна
	"gridcolor":(100,0,0), # цвет сетки
	"bgcolor": (0,0,0), # цвет фона
	"textcolor": (150,150,150), # цвет текста
	"color": (255,255,255), # цвет агентов
	"checkcolor": (255,0,0), # цвет контрольного агента
	"r": 1, # радиус агента

	# video
	"fps": 30, # скорость обновления окна
	"duration": 36000, # макс. количество кадров
	"video": False, # сохранение кадров папку
	"path": "models/m_04/video", # путь к папке для сохранения кадров

	# model
	"spawn": 10, # радиус появления агентов от центра
	"population": 1000, # количество агентов
	"multiply": True, # суммирование задетых вокруг агентов
}