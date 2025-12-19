# MIDI BPM Receiver

A Python tool to receive MIDI clock and calculate BPM, stability, and jitter.

## Installation

1. On windows install [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) and create a virtual port.
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

## Example output

```
MIDI Clock Receiver
-------------------
Available MIDI inputs:
[0] XONE 96 2 0
[1] Partner 96 2 1
[2] loopMIDI Port 2

Select port number to listen to: 2

Listening on: loopMIDI Port 2
Press Ctrl+C to stop.

BPM: 130.00 | Stability:  98.8% | Jitter: 1.21%    
MIDI Stop received.

MIDI Start received.
BPM: 130.26 | Stability:  78.6% | Jitter: 21.43%   
```