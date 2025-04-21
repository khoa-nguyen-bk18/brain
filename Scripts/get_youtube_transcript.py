#!/usr/bin/env python3
import sys
import json
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

def save_transcript(transcript, output_file):
    if transcript:
        # Add .json extension if not present
        if not output_file.endswith('.json'):
            output_file = f"{output_file}.json"

        with open(output_file, 'w', encoding='utf-8') as f:
            # Save as JSON for structured data
            json.dump(transcript, f, indent=2)

        # Also save as plain text for easy reading
        txt_file = output_file.replace('.json', '.txt')
        with open(txt_file, 'w', encoding='utf-8') as f:
            for entry in transcript:
                f.write(f"[{entry['start']:.2f}] {entry['text']}\n")

        print(f"Transcript saved to {output_file} and {txt_file}")
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_youtube_transcript.py <youtube_video_id> [output_file]")
        sys.exit(1)

    video_id = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else f"../.temp/{video_id}_transcript.json"

    transcript = get_transcript(video_id)
    if save_transcript(transcript, output_file):
        print("Transcript downloaded successfully!")
    else:
        print("Failed to download transcript.")
        sys.exit(1)
