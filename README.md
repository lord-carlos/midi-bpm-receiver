# MIDI Clock Receiver and bpm calculator

A Python tool to receive MIDI clock and calculate BPM, stability, and jitter.

## Installation

1. Install [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) and create a virtual port.
2. Setup environment:
```powershell
uv venv
uv pip install -r requirements.txt
```

## Usage

Run the script:
```powershell
uv run python .\midi_receiver.py
```

## Metrics

- **BPM**: Calculated tempo based on 24 MIDI clock ticks per beat.
- **Stability**: Percentage of clock consistency (100% is perfect).
- **Jitter**: Standard deviation of tick intervals as a percentage.
