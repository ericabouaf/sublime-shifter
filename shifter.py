import sublime, sublime_plugin

class shifterCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command('set_build_system', {
      'file': 'Packages/shifter/shifter.sublime-build'
    })
    self.window.run_command('build')
