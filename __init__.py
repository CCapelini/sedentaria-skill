from mycroft import MycroftSkill, intent_file_handler


class Sedentaria(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sedentaria.intent')
    def handle_sedentaria(self, message):
        self.speak_dialog('sedentaria')


def create_skill():
    return Sedentaria()

