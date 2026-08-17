"""
Speech-to-Text Module for MeetMind AI

This module converts audio files to text using Azure Cognitive Services Speech-to-Text SDK.
It reads Azure Speech credentials from environment variables and provides a simple interface
for transcribing audio files.
"""

import os
from typing import Optional


def get_speech_credentials() -> tuple[str, str]:
    """
    Retrieve Azure Speech credentials from environment variables.

    Returns:
        tuple: (api_key, region) for Azure Speech service

    Raises:
        ValueError: If required environment variables are not set
    """
    api_key = os.getenv("AZURE_SPEECH_KEY")
    region = os.getenv("AZURE_SPEECH_REGION")

    if not api_key or not region:
        raise ValueError(
            "Missing Azure Speech credentials. Please set AZURE_SPEECH_KEY and AZURE_SPEECH_REGION "
            "environment variables."
        )

    return api_key, region


def transcribe_audio(audio_file_path: str) -> str:
    """
    Transcribe an audio file to text using Azure Speech-to-Text service.

    Args:
        audio_file_path (str): Path to the audio file (supports .wav, .mp3, .m4a, etc.)

    Returns:
        str: Transcribed text from the audio file

    Raises:
        FileNotFoundError: If the audio file does not exist
        ValueError: If Azure credentials are missing or invalid
        RuntimeError: If transcription fails
    """
    # Validate audio file exists
    if not os.path.exists(audio_file_path):
        raise FileNotFoundError(f"Audio file not found: {audio_file_path}")

    # Get Azure credentials
    try:
        api_key, region = get_speech_credentials()
    except ValueError as e:
        raise ValueError(f"Credential error: {str(e)}")

    # Import Azure Speech SDK
    try:
        import azure.cognitiveservices.speech as speechsdk
    except ImportError:
        raise RuntimeError(
            "Azure Speech SDK not found. Please install it using: pip install azure-cognitiveservices-speech"
        )

    # Create speech config
    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)
    speech_config.speech_recognition_language = "en-US"

    # Create audio config from file
    try:
        audio_config = speechsdk.audio.AudioConfig(filename=audio_file_path)
    except Exception as e:
        raise RuntimeError(f"Failed to configure audio input: {str(e)}")

    # Create speech recognizer
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Perform transcription
    try:
        result = recognizer.recognize_once()
    except Exception as e:
        raise RuntimeError(f"Transcription service error: {str(e)}")

    # Handle recognition results
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        transcript = result.text
        if not transcript.strip():
            raise RuntimeError("Audio file was recognized but contains no recognizable speech")
        return transcript

    elif result.reason == speechsdk.ResultReason.NoMatch:
        raise RuntimeError(
            "No speech could be recognized. Please check the audio quality and language settings."
        )

    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation = result.cancellation_details
        raise RuntimeError(
            f"Transcription canceled. Reason: {cancellation.reason}. "
            f"Error details: {cancellation.error_details}"
        )

    else:
        raise RuntimeError(f"Unexpected recognition result: {result.reason}")


def transcribe_audio_with_details(audio_file_path: str) -> dict:
    """
    Transcribe an audio file and return transcript along with metadata.

    Args:
        audio_file_path (str): Path to the audio file

    Returns:
        dict: Dictionary containing:
            - 'transcript' (str): Transcribed text
            - 'file_path' (str): Input audio file path
            - 'status' (str): Status of transcription ('success' or 'error')
            - 'error_message' (str, optional): Error message if transcription failed

    Example:
        result = transcribe_audio_with_details('meeting.wav')
        if result['status'] == 'success':
            print(result['transcript'])
        else:
            print(result['error_message'])
    """
    try:
        transcript = transcribe_audio(audio_file_path)
        return {
            "transcript": transcript,
            "file_path": audio_file_path,
            "status": "success",
        }
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        return {
            "transcript": "",
            "file_path": audio_file_path,
            "status": "error",
            "error_message": str(e),
        }


def main(audio_file_path: str) -> Optional[str]:
    """
    Simple main function to transcribe an audio file.

    This is the entry point for converting audio to text. The returned transcript
    can be directly passed to the text_analysis.py pipeline.

    Args:
        audio_file_path (str): Path to the audio file to transcribe

    Returns:
        str: Transcribed text, or None if transcription failed

    Example:
        transcript = main("path/to/meeting_recording.wav")
        if transcript:
            print("Transcription successful!")
            print(transcript)
        else:
            print("Transcription failed!")
    """
    try:
        transcript = transcribe_audio(audio_file_path)
        print(f"✓ Transcription completed successfully")
        return transcript
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"✗ Transcription failed: {str(e)}")
        return None


if __name__ == "__main__":
    # Example usage
    import sys

    if len(sys.argv) < 2:
        print("Usage: python speech_to_text.py <audio_file_path>")
        print("\nExample: python speech_to_text.py meeting_recording.wav")
        sys.exit(1)

    audio_path = sys.argv[1]
    result = main(audio_path)

    if result:
        print("\n--- Transcription Result ---")
        print(result)
