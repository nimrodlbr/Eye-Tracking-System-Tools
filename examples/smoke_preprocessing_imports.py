from eye_tracking_system_tools.preprocessing.blocksync import BlockSync
from eye_tracking_system_tools.preprocessing.oerecording import OERecording

def main():
    print("Imported BlockSync from:", BlockSync.__module__)
    print("Imported OERecording from:", OERecording.__module__)
    print("OK: imports succeeded")

if __name__ == "__main__":
    main()
