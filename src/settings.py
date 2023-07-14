class SystemInfo:
    """
    Attributes:
    cpu_percent_interval (float): The interval at which CPU load is measured, in seconds. By default, it is set to 0.1 seconds.
        Adjust this value to control the frequency of CPU load updates. Higher values result in slower updates, while lower values result in faster updates.

    Notes:
        - The `cpu_percent_interval` attribute determines the time interval at which the CPU load is measured.
        Adjust this value based on your desired frequency of CPU load updates.
    """

    cpu_percent_interval: float = 0.1  # Default 0.1 (if more - slower, less - faster)


class ScreenRecording:
    """
    A class representing screen recording functionality.

    Attributes:
        video_extension (str): The default video extension for recorded videos. By default, it is set to "mp4".
            FFmpeg supports other video formats as well, such as AVI, MKV, MOV, WMV, FLV, WebM, MPEG, 3GP, and TS.
        frame_rate (int): The frame rate at which the screen recording will be captured. By default, it is set to 30 frames per second (fps).
            You can modify this value to a smaller or larger frame rate depending on your requirements and system capabilities.
        monitor_resolution (str): The resolution of the monitor to be recorded. By default, it is set to "1920x1080".
            You can modify this value to match the desired monitor resolution for your screen recording.
    Usage:
    To use the `ScreenRecording` class, create an instance of the class and access its attributes and methods.
    Notes:
        - You can modify the `video_extension` attribute to set a different default video extension for your recordings.
        - The supported video formats depend on the availability and configuration of FFmpeg on your system.
        - The `frame_rate` attribute determines the number of frames per second captured in the screen recording.
          Adjust this value based on your desired output and system capabilities.
        - The `monitor_resolution` attribute determines the resolution of the monitor to be recorded.
          Modify this value to match the desired monitor resolution for your screen recording.
    """

    video_extension: str = "mp4"  # Default mp4, but FFmpeg supports other formats too:
    # .avi - Audio Video Interleave video container format.
    # .mkv - Matroska multimedia container format.
    # .mov - QuickTime multimedia container format.
    # .wmv - Windows Media Video format.
    # .flv - Flash Video format.
    # .webm - WebM multimedia container format.
    # .mpeg - MPEG video format.
    # .3gp - 3GPP multimedia container format.
    # .ts - MPEG Transport Stream container format.

    frame_rate: int = 30  # Default 30, but you can change this value to a smaller side or, if your system allows, to a larger one

    monitor_resolution: str = "1920x1080"  # Default 1920x1080, but you can try:
    # Standard Definition(SD):
    #
    # 640x480
    # 720x480
    # 720x576
    #
    # High Definition(HD):
    #
    # 1280x720(720p)
    # 1920x1080(1080p)
    #
    # Ultra High Definition(UHD) / 4K:
    #
    # 3840x2160
    # 4096x2160
    #
    # 5K:
    #
    # 5120x2880
    #
    # 8K:
    #
    # 7680x4320