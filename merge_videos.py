#!/usr/bin/env python3
#coding=utf-8

import os
import json
import subprocess
import re

def sanitize_filename(filename):
    """Remove invalid characters from filename"""
    # Remove or replace invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove leading/trailing spaces and dots
    filename = filename.strip(' .')
    return filename

def get_unique_filename(base_dir, title):
    """Generate unique filename by adding numbers if duplicate exists"""
    title = sanitize_filename(title)
    base_filename = title
    output_file = os.path.join(base_dir, f'{base_filename}.mp4')

    counter = 1
    while os.path.exists(output_file):
        base_filename = f"{title}_{counter}"
        output_file = os.path.join(base_dir, f'{base_filename}.mp4')
        counter += 1

    return output_file

def find_matching_directories(base_dir):
    """Find directories with entry.json and 80/audio.m4s, 80/video.m4s structure"""
    matches = []
    for root, dirs, files in os.walk(base_dir):
        if 'entry.json' in files:
            # Check if 80 directory exists and contains audio.m4s and video.m4s
            audio_path = os.path.join(root, '80', 'audio.m4s')
            video_path = os.path.join(root, '80', 'video.m4s')
            if os.path.exists(audio_path) and os.path.exists(video_path):
                matches.append(root)
    return matches

def merge_audio_video(audio_path, video_path, output_path):
    """Use ffmpeg to merge audio and video files"""
    cmd = [
        'ffmpeg',
        '-i', video_path,
        '-i', audio_path,
        '-c', 'copy',
        '-y',  # Overwrite output file if exists
        output_path
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error merging files: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    base_dir = os.getcwd()  # Use current working directory
    output_dir = base_dir  # Output to current directory

    print(f"Searching for matching directories in: {base_dir}")
    matches = find_matching_directories(base_dir)

    if not matches:
        print("No matching directories found!")
        return

    print(f"Found {len(matches)} matching directories")

    for i, match in enumerate(matches, 1):
        print(f"\nProcessing {i}/{len(matches)}: {os.path.basename(match)}")

        try:
            # Read entry.json
            entry_file = os.path.join(match, 'entry.json')
            with open(entry_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Handle the format "1|{json_data}"
                if '|' in content:
                    json_content = content.split('|', 1)[1]
                else:
                    json_content = content
                entry_data = json.loads(json_content)

            # Get title
            title = entry_data.get('title', f'video_{i}')
            print(f"Title: {title}")

            # Get file paths
            audio_path = os.path.join(match, '80', 'audio.m4s')
            video_path = os.path.join(match, '80', 'video.m4s')

            # Generate unique output filename
            output_path = get_unique_filename(output_dir, title)

            print(f"Merging to: {os.path.basename(output_path)}")

            # Merge files
            if merge_audio_video(audio_path, video_path, output_path):
                print(f"✅ Successfully created: {os.path.basename(output_path)}")
            else:
                print(f"❌ Failed to create: {os.path.basename(output_path)}")

        except Exception as e:
            print(f"❌ Error processing {match}: {e}")

    print("\n🎉 Processing complete!")

if __name__ == "__main__":
    main()

