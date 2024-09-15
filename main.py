import os
import madmom
import sys

def prepare():
    # create a dummy file
    os.makedirs('temp', exist_ok=True)
    with open('temp/dummy.txt', 'w') as f:
        f.write('Hello, world!')

def do_chord_identification(input_path, output_path):
    # test if the dummy file exists
    with open('temp/dummy.txt', 'r') as f:
        assert f.read() == 'Hello, world!'

    proc = madmom.audio.chroma.DeepChromaProcessor()
    decode = madmom.features.chords.DeepChromaChordRecognitionProcessor()

    chroma = proc(input_path)
    chords = decode(chroma)
    # save the output
    with open(output_path, 'w') as f:
        for onset, duration, label in chords:
            f.write(f'{onset} {duration} {label}\n')

if __name__ == '__main__':
    task_name = sys.argv[1]
    if task_name == 'prepare':
        prepare()
    elif task_name == 'do_chord_identification':
        input_path = sys.argv[2]
        output_path = sys.argv[3]
        do_chord_identification(input_path, output_path)
    else:
        raise ValueError(f'Unknown task: {task_name}')