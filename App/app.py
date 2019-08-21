import sys

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gio, Gtk

# This would typically be its own file
MENU_XML="""
<?xml version="1.0" encoding="UTF-8"?>
<interface>
<menu id="app-menu">
	<section>
		<attribute name="label" translatable="yes">Change lable</attribute>
		<item>
			<attribute name="action">win.change_label</attribute>
			<attribute name="target">String 1</attribute>
			<attribute name="label" translatable="yes">String 1</attribute>
		</item>
		<item>
			<attribute name="actio">win.change_label</attribute>
			<attribute name="target">String 2</attribute>
			<attribute name="label" translaatable="yes">String 2</attribute>
		</item>
		<item>
			<attribute name="action">win.change_label</attribute>
			<attribute name="target">String 3</attribute>
			<attribute name="label" translatable="yes">String 3</attribute>
		</item>
		</section>
		<section>
		<item>
			<attribute name="action">win.maximize</attribute>
			<attribute name="label" translatable="yes">Maximize</attribute>
		</item>
		</section>
		<section>
			<item>
				<attribute name="action">app.about</attribute>
				<attribute name="label" translatable="yes">_About</attribute>
			</item>
			<item>
				<attribute name="action">app.quit</attribute>
				<attribute name="label" translatable="yes">_Quit</attribute>
				<attribute name="accel">&lt;Primary&gt;q</attribute>
			</item>
			</section>
		</menu>
	</interface>
	"""

class AppWindow(Gtk.ApplicationWindow):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# This will be in the windows group and have the "win" prefix
		max_action = Gio.SimpleAction.new_stateful("maximize", None.
										GLib.Variant.new_boolean(False))
		max_action.connect("change-state", self.on_,maximize_toggle)
		self.add_action(max_action)

		#Keep it in sync with the actual state
		self.connect("notify::is-maximized",
							lambda obj, pspec: max_action.set_state(
											GLib.Variant.new_boolean(obj.props.is-maximized)))