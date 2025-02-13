# This Python file uses the following encoding: utf-8
import os, random
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from mutagen.wavpack import WavPack
import screens


class media_player_tab:
    def __init__(self):
        self.ui = screens.main_screen_ui
        self.mediaPlayer = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.audioOutput.setVolume(0.5)

        self.has_selected_track = False
        self.is_muted = False
        self.is_shuffled = False
        self.repeat_mode = 0  # 0 = No Repeat, 1 = Repeat All, 2 = Repeat One
        self.original_playlist = []

        self.media_tab = self.ui.screen_tabs.findChild(QtWidgets.QWidget, "media_tab")
        self.audioselect_list = self.media_tab.findChild(QtWidgets.QListWidget, "audioselect_list")
        self.filename = self.media_tab.findChild(QtWidgets.QLabel, "filename")
        self.song_cover = self.media_tab.findChild(QtWidgets.QLabel, "song_cover")
        self.audio_file_progress_slidebar = self.media_tab.findChild(QtWidgets.QSlider, "audio_file_progress_slidebar")
        self.label_current_duration = self.media_tab.findChild(QtWidgets.QLabel, "label_current_duration")
        self.label_total_time = self.media_tab.findChild(QtWidgets.QLabel, "label_total_time")
        self.shuffle_button = self.media_tab.findChild(QtWidgets.QPushButton, "shuffle_button")
        self.previous_button = self.media_tab.findChild(QtWidgets.QPushButton, "previous_button")
        self.rewind_button = self.media_tab.findChild(QtWidgets.QPushButton, "rewind_button")
        self.stop_button = self.media_tab.findChild(QtWidgets.QPushButton, "stop_button")
        self.playpause_button = self.media_tab.findChild(QtWidgets.QPushButton, "playpause_button")
        self.forward_button = self.media_tab.findChild(QtWidgets.QPushButton, "forward_button")
        self.next_button = self.media_tab.findChild(QtWidgets.QPushButton, "next_button")
        self.repeat_button = self.media_tab.findChild(QtWidgets.QPushButton, "repeat_button")
        self.mute_unmute_button = self.media_tab.findChild(QtWidgets.QPushButton, "mute_unmute_button")
        self.volume_slider = self.media_tab.findChild(QtWidgets.QSlider, "volume_slider")

        # Connecting buttons to functions
        self.playpause_button.clicked.connect(self.toggle_play_pause)
        self.stop_button.clicked.connect(self.stop_audio)
        self.mute_unmute_button.clicked.connect(self.toggle_mute)
        self.volume_slider.valueChanged.connect(self.change_volume)
        self.audioselect_list.itemDoubleClicked.connect(self.play_selected_file)
        self.previous_button.clicked.connect(self.play_previous)
        self.forward_button.clicked.connect(self.forward_audio)
        self.rewind_button.clicked.connect(self.rewind_audio)
        self.next_button.clicked.connect(self.play_next)
        self.shuffle_button.clicked.connect(self.toggle_shuffle)
        self.repeat_button.clicked.connect(self.toggle_repeat)

        # Connecting media player signals
        self.mediaPlayer.positionChanged.connect(self.update_position)
        self.mediaPlayer.durationChanged.connect(self.update_duration)
        self.mediaPlayer.mediaStatusChanged.connect(self.check_media_status)
        self.audio_file_progress_slidebar.sliderReleased.connect(self.set_position)
        self.audio_file_progress_slidebar.sliderPressed.connect(self.pause_while_seeking)

        self.load_media_files()

    #load media files
    def load_media_files(self):
         media_dir = "media"
         if not os.path.exists(media_dir):
             os.makedirs(media_dir)

         self.audioselect_list.clear()
         self.original_playlist = []
         for file in os.listdir(media_dir):
             if file.endswith(".mp3") or file.endswith(".wav"):
                 self.original_playlist.append(file)
                 self.audioselect_list.addItem(file)

    #play selected media file
    def play_selected_file(self):
        selected_item = self.audioselect_list.currentItem()
        if selected_item:
            file_path = os.path.abspath(os.path.join("media", selected_item.text()))
            self.filename.setText(selected_item.text())
            self.mediaPlayer.setSource(QtCore.QUrl.fromLocalFile(file_path))
            self.mediaPlayer.play()
            self.playpause_button.setIcon(QtGui.QIcon(":/mediaplayer/icons/mediaplayer/pause.png"))
            self.has_selected_track = True
            self.set_song_cover(file_path)

    #Play/Pause functionality
    def toggle_play_pause(self):
        if not self.has_selected_track and self.audioselect_list.count() > 0:
            self.audioselect_list.setCurrentRow(0)
            self.play_selected_file()
            return

        if self.mediaPlayer.playbackState() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            self.playpause_button.setIcon(QtGui.QIcon(":/mediaplayer/icons/mediaplayer/play.png"))
        else:
            self.mediaPlayer.play()
            self.playpause_button.setIcon(QtGui.QIcon(":/mediaplayer/icons/mediaplayer/pause.png"))

    #stop player
    def stop_audio(self):
        self.mediaPlayer.stop()
        self.playpause_button.setIcon(QtGui.QIcon(":/mediaplayer/icons/mediaplayer/play.png"))

    #mute/unmute function
    def toggle_mute(self):
        self.is_muted = not self.is_muted
        self.audioOutput.setMuted(self.is_muted)
        icon_path = ":/mediaplayer/icons/mediaplayer/mute.png" if self.is_muted else ":/mediaplayer/icons/mediaplayer/unmute.png"
        self.mute_unmute_button.setIcon(QtGui.QIcon(icon_path))

    #change volume function
    def change_volume(self, value):
        self.audioOutput.setVolume(value / 100)
        self.mute_unmute_button.setIcon(QtGui.QIcon(":/mediaplayer/icons/mediaplayer/mute.png" if value == 0 else ":/mediaplayer/icons/mediaplayer/unmute.png"))


    #toggle shuffle functionality
    def toggle_shuffle(self):
        current_item = self.audioselect_list.currentItem()
        if current_item:
            current_track = current_item.text()
        else:
            current_track = None

        if self.is_shuffled:
            self.is_shuffled = False
            self.audioselect_list.clear()
            self.audioselect_list.addItems(self.original_playlist)
            self.shuffle_button.setIcon(QtGui.QIcon(":/mediaplayer/icons/mediaplayer/shuffle_disabled.png"))
        else:
            self.is_shuffled = True
            shuffled_playlist = self.original_playlist[:]
            random.shuffle(shuffled_playlist)
            if current_track in shuffled_playlist:
                shuffled_playlist.remove(current_track)
                shuffled_playlist.insert(0, current_track)
            self.audioselect_list.clear()
            self.audioselect_list.addItems(shuffled_playlist)
            self.shuffle_button.setIcon(QtGui.QIcon(":/mediaplayer/icons/mediaplayer/shuffle_enabled.png"))

        # Keep the current track selected
        if current_track:
            items = self.audioselect_list.findItems(current_track, QtCore.Qt.MatchExactly)
            if items:
                self.audioselect_list.setCurrentItem(items[0])

    #toggle repeat function for repeating songs
    def toggle_repeat(self):
        if self.repeat_mode == 0:
            self.repeat_mode = 1  # Repeat all
            self.repeat_button.setIcon(QtGui.QIcon(":/mediaplayer/icons/mediaplayer/repeat_enabled.png"))
        elif self.repeat_mode == 1:
            self.repeat_mode = 2  # Repeat one track
            self.repeat_button.setIcon(QtGui.QIcon(":/mediaplayer/icons/mediaplayer/repeat_one.png"))
        else:
            self.repeat_mode = 0  # No repeat
            self.repeat_button.setIcon(QtGui.QIcon(":/mediaplayer/icons/mediaplayer/repeat_disabled.png"))

    #check media player status
    def check_media_status(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            if self.repeat_mode == 2:  # Repeat current track
                self.mediaPlayer.play()
            else:
                current_row = self.audioselect_list.currentRow()
                if current_row < self.audioselect_list.count() - 1:
                    self.audioselect_list.setCurrentRow(current_row + 1)
                    self.play_selected_file()
                elif self.repeat_mode == 1:  # Repeat all
                    self.audioselect_list.setCurrentRow(0)
                    self.play_selected_file()

    #play next function
    def play_next(self):
        if self.repeat_mode == 2:  # Repeat one mode, restart current track
            self.mediaPlayer.setPosition(0)
            self.mediaPlayer.play()
        else:
            current_row = self.audioselect_list.currentRow()
            if current_row < self.audioselect_list.count() - 1:
                self.audioselect_list.setCurrentRow(current_row + 1)
                self.play_selected_file()
            elif self.repeat_mode == 1:  # Repeat all mode, go back to first track
                self.audioselect_list.setCurrentRow(0)
                self.play_selected_file()



    #play previous function
    def play_previous(self):
        if self.repeat_mode == 2:  # Repeat one mode, restart current track
            self.mediaPlayer.setPosition(0)
            self.mediaPlayer.play()
        else:
            current_row = self.audioselect_list.currentRow()
            if current_row > 0:
                self.audioselect_list.setCurrentRow(current_row - 1)
                self.play_selected_file()
            elif self.repeat_mode == 1:  # Repeat all mode, go to last track
                last_index = self.audioselect_list.count() - 1
                self.audioselect_list.setCurrentRow(last_index)
                self.play_selected_file()

    #set time format for the playing media
    def format_time(self, ms):
        seconds = (ms // 1000) % 60
        minutes = (ms // 60000) % 60
        hours = (ms // 3600000)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    #update duration for the playing media
    def update_duration(self, duration):
        self.audio_file_progress_slidebar.setMaximum(duration)
        self.label_total_time.setText(self.format_time(duration))

    #update slider position for the duration of the playing media
    def update_position(self, position):
        self.audio_file_progress_slidebar.setValue(position)
        self.label_current_duration.setText(self.format_time(position))

    #pause the audio while seeking a certain point
    def pause_while_seeking(self):
        self.mediaPlayer.pause()

    #set current playing media position
    def set_position(self):
        position = self.audio_file_progress_slidebar.value()
        self.mediaPlayer.setPosition(position)
        self.mediaPlayer.play()

    #forward current playing media position
    def forward_audio(self):
        self.mediaPlayer.setPosition(min(self.mediaPlayer.duration(), self.mediaPlayer.position() + 5000))

    #rewind current playing media position
    def rewind_audio(self):
        self.mediaPlayer.setPosition(max(0, self.mediaPlayer.position() - 5000))

    #set song cover to prview while playing the current media
    def set_song_cover(self, file_path):
        """Extracts cover art from the audio file and sets it in QLabel. Uses a default image if no cover is found."""
        cover_data = None

        if file_path.lower().endswith('.mp3'):
            try:
                audio = MP3(file_path, ID3=ID3)
                for tag in audio.tags.values():
                    if isinstance(tag, APIC):  # Find album art
                        cover_data = tag.data
                        break
            except Exception as e:
                print(f"Error extracting MP3 cover: {e}")

        elif file_path.lower().endswith('.wav'):
            try:
                audio = WavPack(file_path)
                if hasattr(audio, 'pictures') and audio.pictures:
                    cover_data = audio.pictures[0].data
            except Exception as e:
                print(f"Error extracting WAV cover: {e}")

        pixmap = QtGui.QPixmap()

        if cover_data:
            pixmap.loadFromData(QtCore.QByteArray(cover_data))
        else:
            # Load a default image when no cover is found
            pixmap.load(":/song_cover/images/default_cover.jpeg")

        self.song_cover.setPixmap(pixmap)
        self.song_cover.setScaledContents(True)  # Scale image to fit QLabel

