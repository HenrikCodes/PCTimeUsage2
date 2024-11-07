# Windows 11 Activity Tracker

#### Video Demo: [Link to Demonstration Video](<https://youtu.be/wSM72Oa0dPM)

### Overview
**Windows 11 Activity Tracker** is a tool designed to monitor and visualize user activity across different applications on Windows 11. The program tracks the time spent in each application, records keystrokes, and calculates the distance the mouse has moved, providing users with an insightful breakdown of their daily activity.

### Features
- **Program Usage Tracking**: Automatically monitors the time spent in each active application.
- **Interactive UI**: Includes a simple, intuitive UI with a bar graph and stopwatch for real-time tracking. Hovering over each bar reveals detailed time statistics for the corresponding program.
- **Customizable Program Names**: When an unrecognized program is detected, the user is prompted to assign a name, ensuring clarity in tracking and reporting.

### Getting Started
To set up and start using Windows 11 Activity Tracker:
1. Clone the repository or download the source files.
2. Install any dependencies listed in `requirements.txt`.
3. Run the main script to begin tracking.

### Future Enhancements
- **Automatic Update**: Update the timer every second, not just on application change.
- **Detailed Reports**: Generate daily, weekly, or monthly reports.
- **Customization Options**: Allow users to categorize and filter tracked applications.
- **Additional Visualizations**: Expand on the current UI to include pie charts, heatmaps, etc., for a more comprehensive overview.


### Components
- **`dataM.py`**: Manages data collection and formatting. It captures the activity data, saves it, and reformats it to fit the structure required for the bar graph display.
- **`Keylistener.py`**: Tracks the number of user keyboard inputs (key presses), without recording the actual keystrokes for privacy.
- **`mousetracker.py`**: Tracks mouse activity, including clicks and movement, to gauge overall user interaction.
- **`window1.py`**: Displays a bar graph visualizing the collected data. It includes mouseover tooltips and a stopwatch. When an unknown program is opened, a dialog box is shown for user input.
- **`WindowTracker.py`**: Tracks the active process using the `win32gui` library, ensuring correct application names are retrieved based on specified settings.
