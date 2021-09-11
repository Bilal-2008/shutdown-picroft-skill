from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from os import system

class ShutdownSkill(MycroftSkill):
    def __init__(self):
        super().__init__()
    def initialize(self):
        my_setting = self.settings.get('my_setting')
    @intent_handler('ShutdownIntent.intent')
    def handle_shutdown(self, message):
        system("sudo shutdown -h now")
    @intent_handler('RebootIntent.intent')
    def handle_reboot(self, message):
        system("sudo reboot")
    def stop(self):
        pass

def create_skill():
    return ShutdownSkill()
