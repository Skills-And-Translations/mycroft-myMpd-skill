
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
        self.player = MPDClient()
        self.url = "192.168.8.102"
        self.port = 6600
        self.player.connect(self.url, self.port)
        self.reconnectMsg = "Have to reconnect, please try again"
        playArtistIntent = IntentBuilder("PlayArtistIntent").require("PlayArtistKeyword").require("artistWord").build()
        self.register_intent(playArtistIntent, self.handle_playArtistIntent)
        playAlbumIntent = IntentBuilder("PlayAlbumIntent").require("PlayAlbumKeyword").require("albumWord").build()
        self.register_intent(playAlbumIntent, self.handle_playAlbumIntent)
        playSongIntent = IntentBuilder("PlaySongIntent").require("PlaySongKeyword").require("songWord").build()
        self.register_intent(playSongIntent, self.handle_playSongIntent)
        playIntent = IntentBuilder("PlayIntent").require("Play3333Keyword").build()
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
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
    
    def handle_previousIntent(self, message):
        try:
            self.player.previous()
            songinfo = self.player.currentsong()
            self.speak("Change to song "+songinfo['track'].replace("/", " from "))
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            
    def handle_nextIntent(self, message):
        try:
            self.player.next()
            songinfo = self.player.currentsong()
            self.speak("Change to song "+songinfo['track'].replace("/", " from "))
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
        
    def handle_playIntent(self, message):
        self.speak("play")
        try:
            self.player.play()
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            
    def handle_playArtistIntent(self, message):
        artist1 = message.data.get("artistWord")
        try:
            self.player.clear()
            self.player.searchadd('Artist',artist1)
            self.speak("Ok, i play music from "+artist1)
            self.player.play()
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            
            
    def handle_playSongIntent(self, message):
        artist1 = message.data.get("songWord")
        try:
            self.player.clear()
            self.player.searchadd('Title',artist1)
            self.speak("Ok, i play song "+artist1)
            self.player.play()
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            
    def handle_playAlbumIntent(self, message):
        artist1 = message.data.get("albumWord")
        try:
            self.player.clear()
            self.player.searchadd('Album',artist1)
            self.speak("Ok, i play album "+artist1)
            self.player.play()
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)

            
    def handle_pauseIntent(self, message):
        self.speak("make pause")
        try:
            self.player.pause()
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
    def handle_stopIntent(self, message):
        self.speak("make stop")
        try:
            self.player.stop()
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            

def create_skill():
    return MPDSkill()
