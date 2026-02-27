from flask import Flask

# 1. إعداد التطبيق
app = Flask(__name__)

# 2. تصميم واجهة موقع VIPO
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>VIPO DARK KINGDOM</title>
    </head>
    <body style="background-color: #0d1117; color: #ff3e3e; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding-top: 100px;">
        <h1 style="font-size: 50px; text-shadow: 2px 2px #000;">😈 VIPO DARK KINGDOM 😈</h1>
        <p style="color: #c9d1d9; font-size: 22px;">Welcome to the future of Gaming & Coding.</p>
        <div style="margin-top: 30px; padding: 20px; border: 1px solid #30363d; display: inline-block; border-radius: 10px;">
            <h2 style="color: #58a6ff;">Current Project: $1000 Goal</h2>
            <p style="color: #8b949e;">Status: Development Phase</p>
        </div>
        <footer style="position: fixed; bottom: 20px; width: 100%; color: #484f58;">
            © 2026 VIPO - Built with Python & Dark Logic
        </footer>
    </body>
    </html>
    """

# 3. تشغيل المحرك
if __name__ == "__main__":
    print("🚀 السيرفر شغال الآن.. اضغط على الرابط في الأسفل!")
    app.run(host='0.0.0.0', port=5000, debug=True)
    