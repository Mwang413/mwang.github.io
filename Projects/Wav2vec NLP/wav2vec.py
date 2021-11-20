def wav2vec_model(data):
  from logging import logProcesses
  import os
  os.environ["TRANSFORMERS_CACHE"] = "/Users/muduo/Documents/models/wav2vec2_large"

  import soundfile as sf
  import torch
  from datasets import load_dataset
  from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor


  # load pretrained model
  processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
  model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")

  librispeech_samples_ds = load_dataset("patrickvonplaten/librispeech_asr_dummy", "clean", split="validation")
  # load audio
  audio_input, sample_rate = sf.read(librispeech_samples_ds["file"])

  # pad input values and return pt tensor
  input_values = processor(audio_input, sampling_rate=sample_rate, return_tensors="pt").input_values

  # INFERENCE

  # retrieve logits & take argmax
  logits = model(input_values).logits
  predicted_ids = torch.argmax(logits, dim=-1)

  # transcribe
  transcription = processor.decode(predicted_ids[0])
  print(transcription)

  # FINE-TUNE

  target_transcription = "A MAN SAID TO THE UNIVERSE I EXIST"

  # encode labels
  with processor.as_target_processor():
    labels = processor(target_transcription, return_tensors="pt").input_ids

  # compute loss by passing labels
  loss = model(input_values, labels=labels).loss
  print(loss.backward())


