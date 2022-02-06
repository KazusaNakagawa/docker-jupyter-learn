import os
import sys
import pathlib

import ffmpeg

from pydub import AudioSegment
import speech_recognition as sr


def convert_audio_file(dir_name='./audio', file_name=None, after_extent='wav'):
    """ 音声データを指定した拡張子に変換する
    
    params
    ------
      dir_name(str):       audio 格納ディレクトリ
      file_name(str):      変換対象ファイル名
      after_extent(str):   変換後の拡張子 default: 'wav'
    
    return
    ------
      after_file(str):                         変換処理後のファイル
      track(pydub.audio_segment.AudioSegment): 変換した音声データ
      
    """
    before_file = f"{dir_name}/{file_name}"
    before_extent = file_name.split('.')[-1]
    
    after_file = f"{dir_name}/{file_name.split('.')[0]}.{after_extent}"

    track = AudioSegment.from_file(before_file, format=before_extent)
    track.export(after_file, format=after_extent)
    
    return after_file, track


def export_audio_text(audio_file=None, language='ja-JP'):
    """ 読み込んだ audio データを全文テキスト出力する
    
    params
    ------
      audio_file(str): 拡張子は、wavのみ動作確認済
      language(str): テキスト出力する言語
    
    return
    ------
      テキスト出力
    
    """

    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    return recognizer.recognize_google(audio, language=language)
