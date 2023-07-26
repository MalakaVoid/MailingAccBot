class States:
    OptionMenu = False
    MessageMailing = False
    GroupAdding = False
    def get_state(self):
        if self.OptionMenu == True:
            return "option_menu_state"
        elif self.MessageMailing == True:
            return "get_message_to_mail_state"
        elif self.GroupAdding == True:
            return "get_group_to_add_state"
        else:
            return "None"
    def option_menu_state(self):
        self.end_states()
        self.OptionMenu = True
    def get_message_to_mail_state(self):
        self.end_states()
        self.MessageMailing = True
    def get_group_to_add_state(self):
        self.end_states()
        self.GroupAdding = True
    def end_states(self):
        self.OptionMenu = False
        self.MessageMailing = False
        self.GroupAdding = False