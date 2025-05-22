
# Pomodoro Timer ⏳

A simple and customizable Pomodoro timer to help boost productivity by balancing focused work sessions with strategic breaks. Styling Works dynamically based on browser theme

## 📌 Features
- **Start, stop, and resume** the Pomodoro timer.
- **Customizable intervals**:
  - Default **Work Session:** 25 minutes
  - Default **Short Break:** 5 minutes
  - Default **Long Break:** 15 minutes (after 4 work sessions)
- **Session tracking**: Keeps count of completed work sessions.
- **Current session display**: Shows whether you're in **Work**, **Short Break**, or **Long Break**.
- **Sound notification**: Alerts when a session ends.
- **Component based design**: Accessible and visually appealing on desktop and mobile and is light / dark theme compatible.

## 📂 File Structure
```text
📁 Pomodoro Timer
│── index.html   # Main HTML file
│── alarm.mp3    # Sound file
└── script.js # JavaScript file
```

## 🚀 Getting Started
1. Clone the repository:
   ```sh
   git clone https://github.com/petrusjohannesmaas/roadmap.sh
   cd pomodoro-timer
   ```
2. Open `index.html` in a browser.

## 🛠️ Customization
Modify the **default time intervals** in `script.js`:

```js
const workDuration = 25 * 60;      // 25 minutes
const shortBreakDuration = 5 * 60; // 5 minutes
const longBreakDuration = 15 * 60; // 15 minutes
```

---

## 🛠️ Future Enhancements

* Updated styling with icons
* Improve prompts for session type and break duration
* Add alarm options / notifications
* Themes
* User accounts to track sessions and settings

---
