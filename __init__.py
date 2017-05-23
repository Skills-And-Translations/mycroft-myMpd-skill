
from mpd import MPDClient
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.util import play_wav


__author__ = 'hersche'

logger = getLogger(__name__)


class MPDSkill(MycroftSkill):


    def __init__(self):
        super(MPDSkill, self).__init__(name="MPDSkill")

    def initialize(self):
        self.player = client = MPDClient()
        self.player.connect("192.168.43.240", 6600)
        playIntent = IntentBuilder("PlayIntent").require("PlayKeyword").build()
        self.register_intent(playIntent, self.handle_playIntent)
        pauseIntent = IntentBuilder("PauseIntent").require("PauseKeyword").build()
        self.register_intent(pauseIntent, self.handle_pauseIntent)
        stopIntent = IntentBuilder("StopIntent").require("StopKeyword").build()
        self.register_intent(stopIntent, self.handle_stopIntent)
        nextIntent = IntentBuilder("NextIntent").require("NextKeyword").build()
        self.register_intent(nextIntent, self.handle_nextIntent)
        previousIntent = IntentBuilder("PreviousIntent").require("LastKeyword").build()
        self.register_intent(previousIntent, self.handle_previousIntent)
        
        currentsongIntent = IntentBuilder("CurrentSongIntent").require("CurrentSongKeyword").build()
        self.register_intent(currentsongIntent, self.handle_currentsongIntent)
        
    def handle_currentsongIntent(self, message):
        try:
            songinfo = self.player.currentsong()
            self.speak("You listen song "+songinfo['track'].replace("/", " from ")+", "+songinfo['title']+" from "+songinfo['artist'])
        except:
            self.player = client = MPDClient()
            self.player.connect("192.168.43.240", 6600)
    
    def handle_previousIntent(self, message):
        try:
            self.player.previous()
            songinfo = self.player.currentsong()
            self.speak("Change to song "+songinfo['track'].replace("/", " from "))
        except:
            self.player = client = MPDClient()
            self.player.connect("192.168.43.240", 6600)
            
    def handle_nextIntent(self, message):
        try:
            self.player.next()
            songinfo = self.player.currentsong()
            self.speak("Change to song "+songinfo['track'].replace("/", " from "))
        except:
            self.player = client = MPDClient()
            self.player.connect("192.168.43.240", 6600)
        
    def handle_playIntent(self, message):
        self.speak("play")
        try:
            self.player.play()
        except:
            self.player = client = MPDClient()
            self.player.connect("192.168.43.240", 6600)
            
    def handle_pauseIntent(self, message):
        self.speak("make pause")
        try:
            self.player.pause()
        except:
            self.player = client = MPDClient()
            self.player.connect("192.168.43.240", 6600)
    def handle_stopIntent(self, message):
        self.speak("make stop")
        try:
            self.player.stop()
        except:
            self.player = client = MPDClient()
            self.player.connect("192.168.43.240", 6600)
            

def create_skill():
    return MPDSkill()
