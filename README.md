# 📿 Jewellery Store Web Application

This is a simple e-commerce web application built with **Flask** and **MongoDB**, designed for an online jewellery store.  
It provides product listing, cart functionality, checkout, and basic content pages.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## ✨ Features
- 🛒 View jewellery products
- ➕ Add products to cart
- 📦 Checkout and store orders in MongoDB
- 📄 Category and blog pages
- 📬 Contact form support

---

## ⚙️ Tech Stack
- **Backend:** Python, Flask
- **Database:** MongoDB
- **Frontend:** HTML, CSS (with Jinja2 templates)

---

## 📂 Project Structure
\`\`\`
├── app.py                # Main Flask application
├── templates/            # HTML templates (home, product, category, etc.)
├── static/               # CSS, images, and JS files
└── README.md             # Project description
\`\`\`

---

## 🚀 How to Run
> Make sure you have Python and MongoDB installed.

\`\`\`bash
# Clone the repository
git clone https://github.com/yourusername/jewellery-store.git
cd jewellery-store

# Install dependencies
pip install -r requirements.txt

# Start MongoDB locally (if not already running)
mongod

# Run the Flask app
python app.py
\`\`\`

Then open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛠 Configuration
- Replace \`your_secret_key\` in \`app.py\` with a secure key.
- Update MongoDB connection string if needed:
\`\`\`python
client = MongoClient('mongodb://localhost:27017/')
\`\`\`

---

## ✏️ Contribution
Feel free to fork this repository, raise issues, and submit pull requests.

---

## 📃 License
This project is open-source and free to use under the [MIT License](LICENSE).
