from flask import Flask, redirect, render_template_string

app = Flask(__name__)

NEW_URL = "https://renote-fr.onrender.com"

PAGE = """
<!DOCTYPE html>
<html lang='fr'>
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <title>Renote — Nouvelle adresse</title>
  <meta http-equiv='refresh' content='5;url={{ new_url }}'>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: Inter, Arial, sans-serif;
      background: linear-gradient(135deg, #eff6ff, #f8fbff 55%, #eef4ff);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .card {
      background: white;
      border-radius: 24px;
      padding: 40px 36px;
      max-width: 520px;
      width: 100%;
      box-shadow: 0 20px 60px rgba(37,99,235,0.12);
      text-align: center;
    }
    .icon { font-size: 56px; margin-bottom: 20px; }
    h1 { font-size: 24px; color: #0f172a; margin-bottom: 12px; }
    p { color: #5f6b7a; font-size: 15px; line-height: 1.6; margin-bottom: 20px; }
    .new-url {
      background: #eef4ff;
      border: 1px solid #bfdbfe;
      border-radius: 12px;
      padding: 14px 20px;
      font-size: 17px;
      font-weight: 800;
      color: #1d4ed8;
      margin-bottom: 24px;
      word-break: break-all;
    }
    .btn {
      display: inline-block;
      background: linear-gradient(90deg, #1d4ed8, #2563eb);
      color: white;
      text-decoration: none;
      padding: 14px 28px;
      border-radius: 14px;
      font-weight: 700;
      font-size: 16px;
      box-shadow: 0 10px 24px rgba(37,99,235,0.22);
    }
    .btn:hover { opacity: 0.9; }
    .countdown {
      margin-top: 20px;
      color: #94a3b8;
      font-size: 13px;
    }
    .countdown span { font-weight: 700; color: #1d4ed8; }
  </style>
</head>
<body>
  <div class='card'>
    <div class='icon'>🔗</div>
    <h1>Pronote a changé de nom et de URL! c'est maintenant Renote!</h1>
    <p>
      Rien ne change pour toi — même site, mêmes identifiants, même contenu.<br>
      Mets à jour ton favori avec la nouvelle adresse :
    </p>
    <div class='new-url'>renote-fr.onrender.com</div>
    <a href='{{ new_url }}' class='btn'>👉 Aller sur le nouveau site</a>
    <div class='countdown'>Redirection automatique dans <span id='timer'>5</span> secondes...</div>
  </div>
  <script>
    var t = 5;
    var el = document.getElementById('timer');
    var interval = setInterval(function() {
      t--;
      el.textContent = t;
      if (t <= 0) {
        clearInterval(interval);
        window.location.href = '{{ new_url }}';
      }
    }, 1000);
  </script>
</body>
</html>
"""

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template_string(PAGE, new_url=NEW_URL)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
