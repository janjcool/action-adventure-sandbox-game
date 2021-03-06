import pygame

class events_dict:
    def __init__(self, entity_variables, config_options, config_rects, button_class = None):
        self.entity_variables = entity_variables
        self.entity_variables.event_dict = {}
        self.config_options = config_options
        self.config_rects = config_rects
        self.button_class = button_class
        
        self.main()
        
    def main(self):
        no_movement = False
        no_ctrl = False
        no_space = False
        
        for event in self.entity_variables.events:
            if event.type == pygame.QUIT:
                self.entity_variables.event_dict['exit'] = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 1 is left, 2 is middle, 3 is right mouse button.
                    if event.button == 1:
                        if self.config_options.displayer_choser == "game":
                            # `event.pos` is the mouse position.
                            if self.config_rects.test_rect.collidepoint(event.pos):
                                self.entity_variables.event_dict['test'] = True
                                
                        if self.config_options.displayer_choser == "MainMenu":
                            if self.config_rects.start_button.collidepoint(event.pos):
                                self.entity_variables.event_dict['start button'] = True
                            if self.config_rects.exit_button.collidepoint(event.pos):
                                self.entity_variables.event_dict['exit'] = True
                            if self.config_rects.settings_button.collidepoint(event.pos):
                                self.entity_variables.event_dict['settings'] = True
                                
                        if self.config_options.displayer_choser == "GameMenu":
                            if self.config_rects.game_button.collidepoint(event.pos):
                                self.entity_variables.event_dict['game button'] = True
                            if self.config_rects.mainMenu_button.collidepoint(event.pos):
                                self.entity_variables.event_dict['MainMenu button'] = True
                            
            elif event.type == pygame.KEYDOWN:
                if event.key == self.button_class.forward_key:
                    self.entity_variables.event_dict['w_down'] = True
                    no_movement = True
                elif event.key == self.button_class.back_key:
                    self.entity_variables.event_dict['s_down'] = True
                    no_movement = True
                elif event.key == self.button_class.left_key:
                    self.entity_variables.event_dict['a_down'] = True
                    no_movement = True
                elif event.key == self.button_class.right_key:
                    self.entity_variables.event_dict['d_down'] = True
                    no_movement = True

                elif event.key == self.button_class.esc_key:
                    self.entity_variables.event_dict['escape_down'] = True
                
                elif event.key == self.button_class.crouch_key:
                    self.entity_variables.event_dict['ctrl_down'] = True
                    no_ctrl = True     
                elif event.key == self.button_class.space_key:
                    self.entity_variables.event_dict['space_down'] = True
                    no_space = True
                elif event.key == self.button_class.backspace_key:
                    self.entity_variables.event_dict['exit'] = True
        
            elif event.type == pygame.KEYUP:
                if event.key == self.button_class.forward_key:
                    self.entity_variables.event_dict['w_down'] = False
                    no_movement = True
                elif event.key == self.button_class.back_key:
                    self.entity_variables.event_dict['s_down'] = False
                    no_movement = True
                elif event.key == self.button_class.left_key:
                    self.entity_variables.event_dict['a_down'] = False
                    no_movement = True
                elif event.key == self.button_class.right_key:
                    self.entity_variables.event_dict['d_down'] = False
                    no_movement = True
                elif event.key == self.button_class.crouch_key:
                    self.entity_variables.event_dict['ctrl_down'] = False
                    no_ctrl = True
                elif event.key == self.button_class.space_key:
                    self.entity_variables.event_dict['space_down'] = False
                    no_space = True
            
        if no_movement != True:
            self.entity_variables.event_dict['movement_event_happened'] = False
        if no_ctrl != True:
            self.entity_variables.event_dict['ctrl_event_happened'] = False
        if no_space != True:
            self.entity_variables.event_dict['space_event_happened'] = False