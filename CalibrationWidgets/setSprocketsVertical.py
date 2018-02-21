from kivy.uix.widget                      import   Widget
from kivy.properties                      import   ObjectProperty

class SetSprocketsVertical(Widget):
    '''

    Provides a standard interface for making both sprockets point vertically

    '''
    data = ObjectProperty(None) #set externally
    readyToMoveOn   = ObjectProperty(None)

    def LeftCW(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/360.0;
        self.data.gcode_queue.put("G91 ")
        if self.data.config.get('Advanced Settings', 'chainOverSprocket') == 'Top':
            self.data.gcode_queue.put("B09 L"+str(degValue)+" ")
        else:
            self.data.gcode_queue.put("B09 L-"+str(degValue)+" ")
        self.data.gcode_queue.put("G90 ")

    def LeftCCW(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/360.0;
        self.data.gcode_queue.put("G91 ")
        if self.data.config.get('Advanced Settings', 'chainOverSprocket') == 'Top':
            self.data.gcode_queue.put("B09 L-"+str(degValue)+" ")
        else:
            self.data.gcode_queue.put("B09 L"+str(degValue)+" ")
        self.data.gcode_queue.put("G90 ")

    def RightCW(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/360.0;
        self.data.gcode_queue.put("G91 ")
        if self.data.config.get('Advanced Settings', 'chainOverSprocket') == 'Top':
            self.data.gcode_queue.put("B09 R-"+str(degValue)+" ")
        else:
            self.data.gcode_queue.put("B09 R"+str(degValue)+" ")
        self.data.gcode_queue.put("G90 ")

    def RightCCW(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/360.0;
        self.data.gcode_queue.put("G91 ")
        if self.data.config.get('Advanced Settings', 'chainOverSprocket') == 'Top':
            self.data.gcode_queue.put("B09 R"+str(degValue)+" ")
        else:
            self.data.gcode_queue.put("B09 R-"+str(degValue)+" ")
        self.data.gcode_queue.put("G90 ")

    def LeftCW5(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/72.0;
        self.data.gcode_queue.put("G91 ")
        if self.data.config.get('Advanced Settings', 'chainOverSprocket') == 'Top':
            self.data.gcode_queue.put("B09 L"+str(degValue)+" ")
        else:
            self.data.gcode_queue.put("B09 L-"+str(degValue)+" ")
        self.data.gcode_queue.put("G90 ")

    def LeftCCW5(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/72.0;
        self.data.gcode_queue.put("G91 ")
        if self.data.config.get('Advanced Settings', 'chainOverSprocket') == 'Top':
            self.data.gcode_queue.put("B09 L-"+str(degValue)+" ")
        else:
            self.data.gcode_queue.put("B09 L"+str(degValue)+" ")
        self.data.gcode_queue.put("G90 ")

    def RightCW5(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/72.0;
        self.data.gcode_queue.put("G91 ")
        if self.data.config.get('Advanced Settings', 'chainOverSprocket') == 'Top':
            self.data.gcode_queue.put("B09 R-"+str(degValue)+" ")
        else:
            self.data.gcode_queue.put("B09 R"+str(degValue)+" ")
        self.data.gcode_queue.put("G90 ")

    def RightCCW5(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/72.0;
        self.data.gcode_queue.put("G91 ")
        if self.data.config.get('Advanced Settings', 'chainOverSprocket') == 'Top':
            self.data.gcode_queue.put("B09 R"+str(degValue)+" ")
        else:
            self.data.gcode_queue.put("B09 R-"+str(degValue)+" ")
        self.data.gcode_queue.put("G90 ")

    def LeftCWpoint1(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/3600.0;
        self.data.gcode_queue.put("G91 ")
        if self.data.config.get('Advanced Settings', 'chainOverSprocket') == 'Top':
            self.data.gcode_queue.put("B09 L"+str(degValue)+" ")
        else:
            self.data.gcode_queue.put("B09 L-"+str(degValue)+" ")
        self.data.gcode_queue.put("G90 ")

    def LeftCCWpoint1(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/3600.0;
        self.data.gcode_queue.put("G91 ")
        if self.data.config.get('Advanced Settings', 'chainOverSprocket') == 'Top':
            self.data.gcode_queue.put("B09 L-"+str(degValue)+" ")
        else:
            self.data.gcode_queue.put("B09 L"+str(degValue)+" ")
        self.data.gcode_queue.put("G90 ")

    def RightCWpoint1(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/3600.0;
        self.data.gcode_queue.put("G91 ")
        if self.data.config.get('Advanced Settings', 'chainOverSprocket') == 'Top':
            self.data.gcode_queue.put("B09 R-"+str(degValue)+" ")
        else:
            self.data.gcode_queue.put("B09 R"+str(degValue)+" ")
        self.data.gcode_queue.put("G90 ")

    def RightCCWpoint1(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/3600.0;
        self.data.gcode_queue.put("G91 ")
        if self.data.config.get('Advanced Settings', 'chainOverSprocket') == 'Top':
            self.data.gcode_queue.put("B09 R"+str(degValue)+" ")
        else:
            self.data.gcode_queue.put("B09 R-"+str(degValue)+" ")
        self.data.gcode_queue.put("G90 ")

    def setZero(self):
        #mark that the sprockets are straight up
        self.data.gcode_queue.put("B06 L0 R0 ");
        self.carousel.load_next()
    
    def on_Enter(self):
        '''
        
        This function runs when the step is entered
        
        '''
        pass
    
    def on_Exit(self):
        '''
        
        This function run when the process is completed or quit is pressed
        
        '''
        print "compute calibration steps on exit"
        self.readyToMoveOn()