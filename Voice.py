from threading import Event, Thread
import pyttsx3


class Voice(object):
    def __init__(self, skip, play_beep):
        self.t = None
        self._running = False
        self.engine = pyttsx3.init()
        self.skip = skip
        #self.engine.connect('finished-utterance', self.onEnd)


def onEnd(self, name, completed):
    print('finishing : ', name, completed)
    self.stop()

    def on_finished_utterance(self, name, completed):
        print('END')

    t = Thread(target=self.killme, args=(self.engine), daemon=True)
    t.start()

    def process_speech(self, text):
        self.engine.say(str(text))
        self.engine.startLoop(False)
        while self._running:
            self.engine.iterate()

    def say(self, text, length=2):
        # check if thread is running
        if self.t and self._running:
            # stop it if it is
            self.stop()
        # iterate speech in a thread

        self.t = Thread(target=self.process_speech, args=(text,), daemon=True)
        self._running = True
        self.t.start()

        elapsed_seconds = 0
        poll_interval = .1
        while not self.skip.is_set() and elapsed_seconds < length:
            self.skip.wait(poll_interval)
            elapsed_seconds += poll_interval

    def stop(self):
        self._running = False
        try:
            self.engine.endLoop()
        except:
            pass
        try:
            self.t.join()
        except Exception as e:
            pass


skip = Event()
myVoice = Voice(skip, 0)
myVoice.say("test", 2)
myVoice.say("test two", 2)