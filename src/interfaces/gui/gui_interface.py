import tkinter as tk
from processes.screen_recording import ScreenRecorder
from system.system_interface import SystemInterface, ExtendedSystemInterface
from processes.screenshot import Screenshot
from settings import KeyBindings
import logging

logging.basicConfig(filename="screenshot.log", level=logging.INFO)


class GuiInterface:
    def __init__(self):
        """
        Initialize the GUI interface and set up initial configurations.
        """
        self.system_interface = SystemInterface()
        self.extended_system_interface = ExtendedSystemInterface()

        self.root = tk.Tk()
        self.root.title("System Monitor")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, font=("Courier", 12), justify=tk.LEFT)
        self.label.pack(padx=10, pady=10)

        self.topmost = False
        self.recording = False
        self.minimalize = False

        self.screenshot = Screenshot()

        self.create_menu()
        self.create_bindings()

    def create_menu(self) -> None:
        """
        Create the main menu bar for the application window.
        """
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.tools_menu = tk.Menu(self.menu, tearoff=False)
        self.tools_menu.add_command(label="Toggle Topmost", command=self.toggle_topmost)
        self.tools_menu.add_command(
            label="Start Recording", command=self.toggle_recording
        )
        self.tools_menu.add_command(
            label="Show Less/Show More", command=self.toggle_minimalize
        )
        self.tools_menu.add_command(
            label="Take Screenshot", command=self.take_screenshot
        )
        self.menu.add_cascade(label="Tools", menu=self.tools_menu)

    def create_bindings(self) -> None:
        """
        Bind keyboard shortcuts for the various commands.
        """
        self.root.bind_all(KeyBindings.topmost, self.toggle_topmost)
        self.root.bind_all(KeyBindings.start_recording, self.toggle_recording)
        self.root.bind_all(KeyBindings.minimalize, self.toggle_minimalize)
        self.root.bind_all(KeyBindings.screenshot, self.take_screenshot)

    def toggle_topmost(self, event=None) -> None:
        """
        Toggle whether the application window is always on top of all other windows.
        """
        self.topmost = not self.topmost
        self.root.attributes("-topmost", self.topmost)

    def toggle_recording(self, event=None) -> None:
        """
        Toggle screen recording on or off.
        """
        self.recording = not self.recording
        recording_label = "Start Recording" if not self.recording else "Stop Recording"
        self.tools_menu.entryconfig(1, label=recording_label)
        if self.recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self) -> None:
        """
        Start screen recording.
        """
        self.screen_recorder = ScreenRecorder()
        self.screen_recorder.start()

    def stop_recording(self) -> None:
        """
        Stop screen recording.
        """
        self.screen_recorder.stop()

    def toggle_minimalize(self, event=None) -> None:
        """
        Toggle whether to minimalize the display of system information.
        """
        self.minimalize = not self.minimalize
        minimalize_label = "Show Less" if not self.minimalize else "Show More"
        self.tools_menu.entryconfig(2, label=minimalize_label)

    def take_screenshot(self, event=None) -> None:
        """
        Take a screenshot of the current screen and log the action.
        """
        self.screenshot.take()
        logging.info("Screenshot taken.")

    def update_gui(self) -> None:
        """
        Update the system information displayed in the application window every second.
        """
        if self.minimalize:
            cpu_load = self.extended_system_interface.get_average_cpu_load()
            gpu_usage = self.extended_system_interface.get_gpu_usage_percentage()
            ram_usage = self.extended_system_interface.get_memory_usage_gb()
            text = (
                f"{cpu_load}\n{gpu_usage}\n{ram_usage}"
            )
        else:
            progress_bars = self.system_interface.get_progress_bars()
            text = "\n".join(progress_bars) + "\n"

        self.label.config(text=text)
        self.root.after(1000, self.update_gui)

    def run(self) -> None:
        """
        Start the Tkinter event loop to run the application.
        """
        self.update_gui()
        self.root.mainloop()
