
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
        self.url = "192.168.8.104"
        self.port = 6600
        self.player.connect(self.url, self.port)
        self.language = self.config_core.get('lang')[0:2]
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
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            songinfo = self.player.currentsong()
            if self.language=="de":
                self.speak("Du hoerst "+songinfo['track'].replace("/", " from ")+", "+songinfo['title']+" von "+songinfo['artist'])
            else:
                self.speak("You listen song "+songinfo['track'].replace("/", " from ")+", "+songinfo['title']+" from "+songinfo['artist'])
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
    
    def handle_previousIntent(self, message):
        try:
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            self.player.previous()
            songinfo = self.player.currentsong()
            if self.language=="de":
                self.speak("Wechsle zu lied "+songinfo['track'].replace("/", " von "))
            else:
                self.speak("Change to song "+songinfo['track'].replace("/", " from "))
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            
    def handle_nextIntent(self, message):
        try:
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            self.player.next()
            songinfo = self.player.currentsong()
            if self.language=="de":
                self.speak("Wechsle zu lied "+songinfo['track'].replace("/", " von "))
            else:
                self.speak("Change to song "+songinfo['track'].replace("/", " from "))
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
        
    def handle_playIntent(self, message):
        if self.language=="de":
            self.speak("Spiele")
        else:
            self.speak("play")
        try:
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            self.player.play()
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            
    def handle_playArtistIntent(self, message):
        artist1 = message.data.get("artistWord")
        try:
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            self.player.clear()
            self.player.searchadd('Artist',artist1)
            if self.language=="de":
                self.speak("Ok, spiele musik von "+artist1)
            else:
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
            if self.language=="de":
                self.speak("Ok, ich spiele das lied "+artist1)
            else:
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
            if self.language=="de":
                self.speak("Ok, ich spiele das album "+artist1)
            else:
                self.speak("Ok, i play album "+artist1)
            self.player.play()
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)

            
    def handle_pauseIntent(self, message):
        if self.language=="de":
            self.speak("Pausiere")
        else:
            self.speak("Make pause")
        try:
            self.player.pause()
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
    def handle_stopIntent(self, message):
        if self.language=="de":
            self.speak("Halte an")
        else:
            self.speak("Make stop")
        try:
            self.player.stop()
        except:
            self.speak(self.reconnectMsg)
            self.player = client = MPDClient()
            self.player.connect(self.url, self.port)
            

def create_skill():
    return MPDSkill()
