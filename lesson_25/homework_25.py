import datetime
from pathlib import Path


def parse_log_line(line):
    print(line)
    timestamp_str = line.strip()
    timestamp_str = timestamp_str[53:61]
    print(timestamp_str)
    return datetime.datetime.strptime(timestamp_str, "%H:%M:%S")

def process_heartbeat_logs(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
        previous_timestamp = None
        for line in infile:
            current_timestamp = parse_log_line(line)
            if previous_timestamp is not None:
                time_diff = (current_timestamp - previous_timestamp).total_seconds()

                if 30 < time_diff < 32:
                    outfile.write(f"WARNING: Heartbeat interval is {time_diff} seconds at {current_timestamp}\n")
                elif time_diff >= 32:
                    outfile.write(f"ERROR: Heartbeat interval is {time_diff} seconds at {current_timestamp}\n")

            previous_timestamp = current_timestamp

if __name__ == "__main__":

    input_log_file = Path(__file__).parent.parent / "ideas_for_test/heartbeat/hblog"
    output_log_file = "hb.log"
    process_heartbeat_logs(input_log_file, output_log_file)