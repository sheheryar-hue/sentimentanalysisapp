
# 🧠 Sentiment Analysis Web App

A beautiful and fully interactive **Sentiment Analysis App** built using **Streamlit**, hosted via **ngrok** in **Google Colab**. It uses a pre-trained ML model to predict whether user input has a **positive** or **negative** sentiment.

![App Screenshot](https://github.com/sheheryar-hue/sentimentanalysisapp/blob/main/Screenshot%202025-06-28%20222632.png)

---

## 🚀 Features

- 🎯 Predicts sentiment from raw user text
- 💡 Real-time input via web interface
- 🎨 Modern, animated glassmorphic UI
- 🔊 Audio feedback on predictions
- 🌐 Accessible from anywhere using ngrok tunnel

---

## 🛠 Requirements

- Google Colab
- `model.pkl` and `vectorizer.pkl` files
- Ngrok Auth Token (free from [ngrok.com](https://dashboard.ngrok.com/get-started/setup))

---

## 🔧 How to Launch the App (Google Colab)

> Follow these steps **exactly in order** every time:

### ✅ 1. Install required libraries

```python
!pip install streamlit pyngrok --quiet
```

### ✅ 2. Upload your model and vectorizer

```python
from google.colab import files
files.upload()  # Upload model.pkl and vectorizer.pkl
```

### ✅ 3. Save your Streamlit app code

Paste this in a cell:

```python
%%writefile app.py
# app.py
```

### ✅ 4. Run Streamlit server in the background

```python
!streamlit run app.py &>/content/logs.txt &
```

> 🕒 **Wait 5–10 seconds** before continuing to ensure Streamlit is ready.

### ✅ 5. Start Ngrok tunnel

```python
from pyngrok import ngrok
ngrok.set_auth_token("2yxmb7rtM6ndnIPhsvGpxolHVMe_4bEMPb28ZGS9LNXN3kThL") 

public_url = ngrok.connect(8501)
print("🌍 App is live at:", public_url)
```

### ✅ 6. Done!

Now click the URL from the output and enjoy your fully working web app.

---

## 🧪 Optional: Debug logs

If anything goes wrong:

```python
!tail -n 40 /content/logs.txt
```
## 👨‍💻 Author

**MUHAMMAD SHEHARYAR KP**  
📍 Kozhikode, India  
B.Tech AD,AWH KUTTIKATTOOR, KTU University

---

## 📢 License

MIT License. Free to use and modify.
