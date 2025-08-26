import sys

def parse_log_line(line: str) -> dict:
    log_date, log_time, log_lvl, *args = line.split(" ")
    log_args = [str(arg) for arg in args]
    log_msg = " ".join(log_args)
    return {
            "date": log_date,
            "time": log_time,
            "level": log_lvl,
            "message": log_msg,
            }

def load_logs(file_path: str) -> list:
    try:
        with open(file_path,
                  "r", encoding="utf-8") as file:  
            logs_list = [parse_log_line(line) for line in file]
            return logs_list
    except FileNotFoundError:
        print("FileNotFoundError")
        return None
    except UnicodeDecodeError:
        print("UnicodeDecodeError")
        return None
    except Exception as e:
        print(f"other: {e}")
        return None

def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    result = []
    for log in logs:
        if log["level"] == level:
            result.append(f"{log["date"]} {log["time"]} - {log["message"]}")
        pass
    return result

def count_logs_by_level(logs: list) -> dict:
    counted_logs = {}
    for log in logs:
        level = log["level"]
        if level in counted_logs:
            counted_logs[level] += 1
        else:
            counted_logs[level] = 1
    return counted_logs

def display_log_counts(counts: dict): #count_logs_by_level
    result = "Log level     | Count\n\
--------------|------"
    for level in counts:
        space = 14 - len(level)
        line = f"\n{level}" + " " * space + f"| {counts.get(level)}"
        result += line
    return result

#temp solution
log_levels = ["info", "debug", "error", "warning"]

def main():
    if sys.argv.__len__() > 1:
        last_argv = sys.argv[sys.argv.__len__() - 1]
        if last_argv.casefold() in log_levels:
            loaded_logs = load_logs(sys.argv[sys.argv.__len__() - 2])
            counted_logs = count_logs_by_level(loaded_logs)
            alogs = filter_logs_by_level(loaded_logs, last_argv)
            print(display_log_counts(counted_logs))
            print(f"\nLog details for the '{last_argv.upper()}' level:")
            for alog in alogs:
                print(alog.strip("\n"))
        else:
            loaded_logs = load_logs(last_argv)
            counted_logs = count_logs_by_level(loaded_logs)
            print(display_log_counts(counted_logs))

#invoking:
#python task3.py ./path/to/logfile.log

#additional:
#python task3.py ./path/to/logfile.log error

if __name__ == "__main__":
    main()
