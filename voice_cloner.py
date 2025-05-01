from TTS.api import TTS
import os

def clone_voice(voice_sample_path, text_to_synthesize, output_path, language="en"):
    # Check if GPU is available
    use_gpu = True
    try:
        import torch
        use_gpu = torch.cuda.is_available()
    except ImportError:
        use_gpu = False

    # Initialize the TTS model
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=use_gpu)

    # Generate and save audio
    tts.tts_to_file(
        text=text_to_synthesize,
        speaker_wav=voice_sample_path,
        language=language,
        file_path=output_path
    )
    print(f" Voice cloning completed! File saved at: {output_path}")


if __name__ == "__main__":
    # Update these paths to local file paths
    voice_sample = r"replace with path of voice sample "
    output = r"replace with the output file "
    
    text = (
        "put the text that you want to clone"
    )

    clone_voice(voice_sample, text, output)
