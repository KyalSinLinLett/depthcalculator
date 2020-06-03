from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.popup import Popup
from functools import partial
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

import time

class Core(BoxLayout):

		Window.clearcolor = (.4, .7, .8, 0)

		number = NumericProperty()

		def __init__(self, **kwargs):
			super(Core, self).__init__(**kwargs)

			self.bigbox = BoxLayout(orientation='vertical')

			#-------------InfoBtn-----------------#
			
			self.infoBtn = Button(on_press=self.show_info_popup, size_hint=(.2,.5), pos_hint={'center_x':.9})
			self.infoBtn.background_normal = "info.png"
			self.infoBtn.background_down = "info.png"
			self.bigbox.add_widget(self.infoBtn)

			#-------------InfoBtn-----------------#

			#-------------Title-------------------#
			
			self.bigbox.add_widget(Label(text="[color=#f3ff05][font=AtariSmall][b]DEPTH CALCULATOR[/b][/font][/color]", markup=True, font_size='40sp'))

			#-------------Title-------------------#



			#-------------Labels1-----------------#

			self.labelbox1 = BoxLayout(orientation='vertical')
		
			self.time = Label(text='[font=AtariSmall]Interval(s)[/font]' , markup=True, font_size='30sp')
			self.time_res = Label(text='[b][font=AtariSmall]-[/font][/b]' , markup=True, font_size='35sp')
			self.dist = Label(text='[font=AtariSmall]Distance(m)[/font]' , markup=True, font_size='30sp')
			self.dist_res = Label(text='[b][font=AtariSmall]-[/font][/b]' , markup=True, font_size='35sp')

			self.labelbox1.add_widget(self.time)
			self.labelbox1.add_widget(self.time_res)
			self.labelbox1.add_widget(self.dist)
			self.labelbox1.add_widget(self.dist_res)

			self.bigbox.add_widget(self.labelbox1)

			#-------------Labels1-----------------#

			#-------------Line--------------------#

			#self.bigbox.add_widget(Label(text="[font=AtariSmall]-----------------------[/font]", markup=True, font_size='20sp'))

			#-------------Line--------------------#

			#-------------Silly Info--------------#
			
			self.infoBox = BoxLayout(orientation='vertical')

			self.random_info = Label(text="[font=AtariSmall]Light would have travelled: [/font]", markup=True, font_size='17sp')
			self.silly_info = Label(text="", markup=True)
			self.infoBox.add_widget(self.random_info)
			self.infoBox.add_widget(self.silly_info)

			self.bigbox.add_widget(self.infoBox)

			#-------------Silly Info--------------#

			#-------------Buttons-----------------#
			self.btnbox = BoxLayout(orientation='horizontal', spacing=2	)

			self.startBtn = Button(on_press=self.start, size_hint=(.25,.5))
			self.startBtn.background_normal = "start.png"
			self.startBtn.background_down = "start.png"
		
			self.stopBtn  = Button(on_press=self.stop, size_hint=(.25,.5))
			self.stopBtn.background_normal = "stop.png"
			self.stopBtn.background_down = "stop.png"
		

			self.clearBtn = Button(on_press=self.clear, size_hint=(.25,.5))
			self.clearBtn.background_normal = "reset.png"
			self.clearBtn.background_down = "reset.png"

			
			self.btnbox.add_widget(self.startBtn)
			self.btnbox.add_widget(self.stopBtn)
			self.btnbox.add_widget(self.clearBtn)

			self.bigbox.add_widget(self.btnbox)

			#-------------Buttons-----------------#
			
			self.add_widget(self.bigbox)

			# Clock.schedule_interval(self.increment_time, .1)
			self.increment_time(0)

		def show_info_popup(self, button):

			# info_sound = SoundLoader.load("info.wav")
			# if info_sound:
			# 	info_sound.play()
			# 	time.sleep(0.1)
			# 	info_sound.unload()

			self.layout = GridLayout(cols=1, padding=1)

			self.popuplabel = Label(markup=True, size=(.5,.5), halign='left', valign='middle')
			self.popuplabel.text = "[font=AtariSmall]Welcome, decendents of Newton!\n\nHow to use? \nAll you gotta do is \ndrop something from a certain height, \npress the START button, \nwhen it reaches the ground, \nhit the STOP button. \nTa-da!! You got a rough estimate \nof the depth/height.\n\nFORMULA:\nh=ut+0.5gt^2[/font]"
			self.closeBtn = Button(size_hint=(.05, .2))
			self.closeBtn.background_normal = "close.png"
			self.closeBtn.background_down = "close.png"

			self.layout.add_widget(self.popuplabel)
			self.layout.add_widget(self.closeBtn)

			popup = Popup(title="Info for geeks like me!", content=self.layout)
			popup.open()

			self.closeBtn.bind(on_press=popup.dismiss)

		def increment_time(self, interval):
			self.number += .1

		def start(self, instance):
			Clock.unschedule(self.increment_time)
			Clock.schedule_interval(self.increment_time, .1)
			self.time_res.text = "[font=AtariSmall]...[/font]"
			self.dist_res.text = "[font=AtariSmall]...[/font]"
			self.silly_info.text = "[font=AtariSmall]...[/font]"
			# start_sound = SoundLoader.load('start.wav')	
			# if start_sound:
			# 	start_sound.play()
			# 	time.sleep(0.1)
			# 	start_sound.unload()

		def stop(self, instance):
			Clock.unschedule(self.increment_time)

			# stop_sound = SoundLoader.load('stop.wav')	
			# if stop_sound:
			# 	stop_sound.play()
			# 	time.sleep(0.1)
			# 	stop_sound.unload()

			interval = round(self.number, 4)
			self.time_res.text = "[color=#0b7dfe][font=AtariSmall][size=35sp]" + str(interval) + "[/size][/font][/color]"
			dist = float((0.5 * 9.80665) * (pow(interval, 2)))
			self.dist_res.text = "[color=#0b7dfe][font=AtariSmall][size=35sp]" + str(round(dist, 2)) + "[/size][/font][/color]"
			
			dist_light_travelled = interval * 299972
			self.silly_info.text = "[size=25sp][font=AtariSmall][color=#e76900]"+str(round(dist_light_travelled, 2))+" km[/color][/font][/size]"

			self.number = 0

		def clear(self, instance):
			Clock.unschedule(self.increment_time)
			self.time_res.text = "[b][font=AtariSmall]-[/font][/b]"
			self.dist_res.text = "[b][font=AtariSmall]-[/font][/b]"
			self.silly_info.text = "[b][font=AtariSmall]-[/font][/b]"
			# reset_sound = SoundLoader.load('reset.wav')	
			# if reset_sound:
			# 	reset_sound.play()
			# 	time.sleep(0.1)
			# 	reset_sound.unload()


class DepthCalc(App):
	def build(self):
		return Core()


if __name__ == "__main__":
	DepthCalc().run()