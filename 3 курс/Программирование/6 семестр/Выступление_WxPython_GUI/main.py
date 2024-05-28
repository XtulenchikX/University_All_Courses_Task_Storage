import wx
import requests
import json

API = 'Your_API'

class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='TestGUI', size=(500, 400))
        panel = wx.Panel(self)

        self.header = wx.StaticText(panel, label='Погода по городам')
        self.city_text = wx.TextCtrl(panel)
        self.result_text = wx.TextCtrl(panel,
                                       style=wx.TE_MULTILINE | wx.TE_READONLY
                                       | wx.VSCROLL)

        search_button = wx.Button(panel, label='Поиск')
        search_button.Bind(wx.EVT_BUTTON, self.on_search)

        self.temp_checkbox = wx.CheckBox(panel, label='Температура')
        self.temp_min_checkbox = wx.CheckBox(panel, label='Температура min')
        self.temp_max_checkbox = wx.CheckBox(panel, label='Температура max')
        self.feels_like_checkbox = wx.CheckBox(panel, label='Ощущается как')
        self.humidity_checkbox = wx.CheckBox(panel, label='Влажность')
        self.wind_speed_checkbox = wx.CheckBox(panel, label='Скорость ветра')
        self.lon_checkbox = wx.CheckBox(panel, label='Долгота')
        self.lat_checkbox = wx.CheckBox(panel, label='Широта')

        self.font_slider = wx.Slider(panel,
                                     value=12,
                                     minValue=8,
                                     maxValue=24,
                                     style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)
        self.font_slider.Bind(wx.EVT_SCROLL, self.on_font_change)

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(self.header, 0, wx.ALIGN_CENTRE_HORIZONTAL | wx.ALL, 5)

        sizer.Add(self.city_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(search_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.result_text, 1, wx.EXPAND | wx.ALL, 5)

        checkbox_sizer = wx.FlexGridSizer(rows=3, cols=3, hgap=5, vgap=5)
        checkbox_sizer.AddGrowableCol(0)
        checkbox_sizer.Add(self.temp_checkbox, 0, wx.EXPAND)
        checkbox_sizer.Add(self.feels_like_checkbox, 0, wx.EXPAND)
        checkbox_sizer.Add(self.lon_checkbox, 0, wx.EXPAND)
        checkbox_sizer.Add(self.temp_min_checkbox, 0, wx.EXPAND)
        checkbox_sizer.Add(self.humidity_checkbox, 0, wx.EXPAND)
        checkbox_sizer.Add(self.lat_checkbox, 0, wx.EXPAND)
        checkbox_sizer.Add(self.temp_max_checkbox, 0, wx.EXPAND)
        checkbox_sizer.Add(self.wind_speed_checkbox, 0, wx.EXPAND)

        sizer.Add(checkbox_sizer, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizer.Add(self.font_slider, 0, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(sizer)

    def on_search(self, event):
        city = self.city_text.GetValue()
        if city:
            weather_info = self.get_weather(city)
            self.result_text.SetValue(weather_info)

    def get_weather(self, city):
        res = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric'
        )
        data = json.loads(res.text)

        info = ""
        if self.temp_checkbox.GetValue():
            temp = data['main']['temp']
            info += f"🌡️ Температура: {temp} °C\n"
        if self.temp_min_checkbox.GetValue():
            temp_min = data['main']['temp_min']
            info += f"🌡️ Температура min: {temp_min} °C\n"
        if self.temp_max_checkbox.GetValue():
            temp_max = data['main']['temp_max']
            info += f"🌡️ Температура max: {temp_max} °C\n"
        if self.feels_like_checkbox.GetValue():
            feels_like_temp = data['main']['feels_like']
            info += f"🌡️ Ощущается как: {feels_like_temp}°C\n"
        if self.humidity_checkbox.GetValue():
            humidity = data['main']['humidity']
            info += f"💦 Влажность: {humidity}\n"
        if self.wind_speed_checkbox.GetValue():
            wind_speed = data['wind']['speed']
            info += f"🌬 Скорость ветра: {wind_speed} м/c\n"
        if self.lon_checkbox.GetValue():
            lon = data['coord']['lon']
            info += f"Долгота: {lon}\n"
        if self.lat_checkbox.GetValue():
            lat = data['coord']['lat']
            info += f"Широта: {lat}\n"

        return info

    def on_font_change(self, event):
        font_size = self.font_slider.GetValue()
        font = self.result_text.GetFont()
        font.SetPointSize(font_size)
        self.result_text.SetFont(font)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
