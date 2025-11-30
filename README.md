# 📺 YouTube Timestamp & ID Toolkit

A lightweight Python toolkit designed to simplify sharing specific moments in YouTube videos. This project helps you instantly **extract unique Video IDs** and **generate deep-linked URLs** that start at your exact desired timestamp.

---

## 🌟 Features

-   **🆔 Smart ID Extraction**: Instantly strips away URL clutter to find the unique 11-character Video ID from standard links, Shorts, and mobile shares.
-   **⏱️ Precision Timestamps**: Converts human-readable time (`HH:MM:SS`) into exact deep-links.
-   **⚡ Fast & Simple**: Runs directly in your terminal with zero complex dependencies.

---

## ⚙️ Prerequisites

You need Python 3 installed on your computer to run these scripts.

-   **Python 3.x**: [Download Official Installer](https://www.python.org/downloads/)

---

## 🚀 How to Use

This tool works in a simple **3-step workflow**. Follow the commands below to generate your link.

### Step 1: Extract the Video ID
First, use the helper script to find the correct ID for your video.

1.  Run the ID finder script:
    ```
    python yt_id.py
    ```
2.  Paste your YouTube link when prompted.
3.  **Copy** the Video ID displayed in the output (e.g., `qZ3o1ojDQOg`).

### Step 2: Configure the Generator
Before generating the link, you need to tell the app which video to target.

1.  Open the `app.py` file in any text editor.
2.  Locate the print statement at the bottom of the file.
3.  **Replace** the old ID with the new one you just copied:

    ```
    # Change THIS:
    print(f"https://youtu.be/OLD_ID_HERE?t={total_seconds}")

    # To THIS:
    print(f"https://youtu.be/qZ3o1ojDQOg?t={total_seconds}")
    ```
4.  Save the file.

### Step 3: Generate the Link
Now, run the app with your desired timestamp in `HH:MM:SS` format.

**Syntax:**

```
python app.py 00:00:00

```

**Example:**
To create a link starting at **1 hour, 4 minutes, and 20 seconds**:
python app.py 01:04:20


---

## 📂 Project Files

| File | Description |
| :--- | :--- |
| [**yt_id.py**](yt_id.py) | Script that parses YouTube URLs to extract the Video ID. |
| [**app.py**](app.py) | Main script that calculates seconds and generates the final link. |

---

## 🤝 Contributing

Contributions are welcome! If you want to improve the code (e.g., automate Step 2 so you don't have to edit the file manually), feel free to fork the repo.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📝 License

This project is open source and available for personal and educational use 
