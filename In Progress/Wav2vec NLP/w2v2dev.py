from logging import error, logProcesses
import os
from re import I

from transformers.file_utils import is_torch_onnx_dict_inputs_support_available
os.environ["TRANSFORMERS_CACHE"] = "/Users/muduo/Documents/models/wav2vec2_large"

import soundfile as sf
import torch
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor


def mp3tovec(mp3_file, normalized=False):
    import ffprobe
    import ffmpeg
    import pydub 
    import numpy as np
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(mp3_file)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
        print(y)
    if normalized:
        print(a.frame_rate, np.float32(y) / 2**15)
        return a.frame_rate, np.float32(y) / 2**15
    else:
        print(a.frame_rate, y)
        return a.frame_rate, y



class wav2vec2(object):
    def __init__(self, audio_files):
        self.audio_files = audio_files
        self.workit()

    def parse_file_type(self, file_name):
        import os
        split_tup = os.path.splitext(file_name)
        file_extension = split_tup[1]
        return file_extension

    def workit(self):
        for i in range(len(self.audio_files)):
             # try:
                audio_file_name = self.audio_files[i]["name"]
                audio_data = self.audio_files[i]["data"]
                processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
                model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
                self.file_extension = self.parse_file_type(audio_file_name)
                if self.file_extension == ".mp3":
                    # try:
                        print (mp3tovec(audio_data))
                    # except Exception as e:
                    #     print (e)
            #    else:
            #         try:
            #             import soundfile as sf
            #             audio_input = []
            #             sample_rate = []
            #             for i in range(len(self.audio_files["file"])):
            #                 thingnamagiga = sf.read(self.audio_files["file"][i])
            #                 audio_input.append(thingnamagiga[0])
            #                 sample_rate.append(thingnamagiga[1])
            #             print (f"audio input length: {len(audio_input)}")
            #             input_values = []
            #             for i in range(len(audio_input)):
            #                 input_values.append(processor(audio_input[i], sampling_rate=sample_rate[i], return_tensors="pt").input_values)
            #             logits = [model(i).logits for i in input_values]
            #             predicted_ids = torch.argmax(logits, dim=-1)
            #             transcription = processor.decode(predicted_ids[0])
            #             print(transcription)
            #             # # Training section
            #             # with processor.as_target_processor():
            #             #     labels = processor(target_transcription, return_tensors="pt").input_ids

            #             # # compute loss by passing labels
            #             # loss = model(input_values, labels=labels).loss
            #             # print(loss.backward())
            #         except Exception as e:
            #             print(e)
            # except Exception as e:
            #     print(e)
