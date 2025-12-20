import mido
import time
import statistics
from collections import deque

def calculate_metrics(intervals):
    if not intervals or len(intervals) < 2:
        return 0, 0
    
    # MIDI clock is 24 ticks per beat
    avg_interval = statistics.mean(intervals)
    if avg_interval == 0:
        return 0, 0
        
    bpm = 60.0 / (avg_interval * 24.0)
    
    # Jitter: Standard deviation of intervals as a percentage of the mean interval
    # This represents how "stable" the clock signal is.
    std_dev = statistics.stdev(intervals)
    jitter_pc = (std_dev / avg_interval) * 100
    
    return bpm, jitter_pc

def main():
    print("MIDI Clock Receiver")
    print("-------------------")
    
    input_names = mido.get_input_names()
    if not input_names:
        print("No MIDI input ports found. Please ensure loopMIDI is running and a port is created.")
        return

    print("Available MIDI inputs:")
    for i, name in enumerate(input_names):
        print(f"[{i}] {name}")

    try:
        choice = int(input("\nSelect port number to listen to: "))
        port_name = input_names[choice]
    except (ValueError, IndexError):
        print("Invalid selection. Exiting.")
        return

    print(f"\nListening on: {port_name}")
    print("Press Ctrl+C to stop.\n")

    # Store the last 48 tick intervals (2 beats worth) for a stable BPM reading
    intervals = deque(maxlen=48)
    last_tick_time = None

    try:
        with mido.open_input(port_name) as inport:
            while True:
                # poll() returns None immediately if no message is waiting
                msg = inport.poll()
                
                if msg is None:
                    time.sleep(0.001)  # Small sleep to prevent high CPU usage
                    continue

                if msg.type == 'clock':
                    current_time = time.time()
                    if last_tick_time is not None:
                        intervals.append(current_time - last_tick_time)
                        
                        # Update display every 12 ticks (half beat) for responsiveness
                        if len(intervals) >= 24 and len(intervals) % 12 == 0:
                            bpm, jitter = calculate_metrics(intervals)
                            # Stability is 100% minus jitter (clamped to 0)
                            stability = max(0, 100 - jitter)
                            print(f"\rBPM: {bpm:6.2f} | Stability: {stability:5.1f}% | Jitter: {jitter:4.2f}%    ", end="", flush=True)
                    
                    last_tick_time = current_time
                elif msg.type == 'start':
                    print("\nMIDI Start received.")
                    intervals.clear()
                    last_tick_time = None
                elif msg.type == 'stop':
                    print("\nMIDI Stop received.")
                    intervals.clear()
                    last_tick_time = None

    except KeyboardInterrupt:
        print("\n\nStopped by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
