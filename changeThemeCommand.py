import sublime, sublime_plugin, functools
import os,time

class SwitchthemeCommand(sublime_plugin.TextCommand):

	def findThemesInPath(self, themesName, path, go):
		files = os.listdir(path)
		for f in files:
			if os.path.isfile(path + '/' + f):
				if str(f).endswith('tmTheme'):
					themesName.append(path + '/' + f)
			else:
				if go:
					self.findThemesInPath(themesName, path + '/' + f, False)
				
	def getThemesName(self):
		themes = []
		packages_path = sublime.packages_path()
		self.findThemesInPath(themes, packages_path, True)
		themesName = []
		for themeName in themes:
			themesName.append(themeName.replace(packages_path, 'Packages'))
		return themesName

	def changeColorful(self, themesName):
		s = sublime.load_settings("Preferences.sublime-settings")
		currentTheme = s.get('color_scheme')
		index = themesName.index(currentTheme)
		newTheme = themesName[(index+1)%len(themesName)] 
		s.set('color_scheme', newTheme)
		sublime.save_settings("Preferences.sublime-settings")
		#callback = functools.partial(self.changeColorful(themesName))

	
	def run(self, edit):
		self.changeColorful(self.getThemesName())
