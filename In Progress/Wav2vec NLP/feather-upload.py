"make sure to run in shell"

from dataclasses import dataclass
import feather as ftr
from transformers.utils.dummy_flax_objects import FlaxCLIPModel
from wav2vec import wav2vec_model  # import the code which runs your model
from w2v2dev import wav2vec2

def init():
    # We want a File.Upload component, which only accepts image types
    uploader = ftr.File.Upload(types=["audio"])
    return uploader

# 👉 STEP 2: Define the first step.
# @ftr.step(title="wav2vec_transcription", description="Upload an audio file to have it transcribed")
def run_model(uploader):
    audio_files = uploader.get(format ="raw")
    wav2vec2(audio_files)
    # audio_input, sample_rate = sf.read(audio_data[0])
    # print(audio_input)
    # print(audio_data[0], audio_data[0])
    # transcriptions = wav2vec_model(audio_data) # [cat, dog]
    # output_audio = ftr.Audio.View(audio, transcriptions)
    # return ftr.File.Download(files=output_audio, output_filenames=output_audio)
        
# 👉 STEP 3: Bundle your files.
# You need to tell feather what code and weights files your model needs to run. 
# __file__ refers to this current file. We also need to explicitly add this to the bundle
if __name__ == "__main__":
    code_files, model_files = ftr.helpers.get_all_files_from_curr_dir(
                                                include_model_extensions=None, exclude_model_extensions=None)
    bundle = ftr.bundle(code_files=code_files, model_files=model_files)

    # 👉 STEP 4: Build and publish! 
    # The "name" here will be used as an identifier to your model on the feather website.
        # Any new models you publish with the same "name" will overwrite what is currently there
    # Once you run this script, you'll see a local preview through which you can test and publish your model
    ftr.build(name="Audio to Text Transcriptor", init=init, steps=[run_model], file_bundle=bundle)