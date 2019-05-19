from .camera import Camera

class IPCamera(Camera):
    def __init__(self, type, uri):
        super.__init__(type, uri)

        self.VIDEO_STREAM = "http://%s/videostream.cgi?user=admin&pwd=%s"
        self.SET_RESOLUTION = "http://%s/camera_control.cgi?param=%d&value=%d&user=admin&pwd=%s"
        self.SET_PT = "http://%s/decoder_control.cgi?command=%d&onestep=0&user=admin&pwd=%s"

        self.VGA_RESOLUTION = 0
        self.QVGA_RESOLUTION = 1

        self.PTZ_UP = 0
        self.PTZ_UP_STOP = 1
        self.PTZ_DOWN = 2
        self.PTZ_DOWN_STOP = 3
        self.PTZ_LEFT = 4
        self.PTZ_LEFT_STOP = 5
        self.PTZ_RIGHT = 6
        self.PTZ_RIGHT_STOP = 7
        self.PTZ_LEFT_UP = 90
        self.PTZ_RIGHT_UP = 91
        self.PTZ_LEFT_DOWN = 92
        self.PTZ_RIGHT_DOWN = 93
        self.PTZ_CENTER = 25
        self.PTZ_STOP = 1

    def 
    def setResolution(self, resolution):
        pass

    def setPTZ(self, move_direction, stop_direction):
        pass
