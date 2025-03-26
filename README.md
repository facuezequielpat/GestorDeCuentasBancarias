# 📝 README - Banking Management System with Flask and MySQL
## 📌 Project Description
This project is a **banking management system** developed with:

- **Flask** (Python web framework)

- **MySQL** (relational database)

- **Bootstrap** (frontend design)

It allows basic banking operations such as:

- Registering new customers

- Processing deposits and withdrawals

- Checking account balances

- Viewing transaction history

- Editing and deleting accounts

## 🛠️ Technologies Used

| Technology        | Purpose |
|-------------------|---------|
|![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)| _Backend programming language_
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)| _Web framework_
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)| _Database management_
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)| _UI design_
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)| _Web structure_
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)| _Template engine_



 <!DOCTYPE html>
<html lang="en">
<body>
    <p>
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
        <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
        <img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
        <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
    </p>
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#database-setup">Database Setup</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
        <li><a href="#license">License</a></li>
    </ul>
    <h2 id="features">Features</h2>
    <ul class="feature-list">
        <li>✅ User account management</li>
        <li>💰 Deposit/withdrawal processing</li>
        <li>📊 Balance calculation</li>
        <li>🕵️ Transaction history tracking</li>
        <li>🔄 CRUD operations</li>
    </ul>
    <h2 id="installation">Installation</h2>
    <pre><code>git clone https://github.com/yourusername/banking-system.git
cd banking-system
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
pip install -r requirements.txt</code></pre>
    <h2 id="database-setup">Database Setup</h2>
    <ol>
        <li>Create MySQL database:
            <pre><code>CREATE DATABASE banco;</code></pre>
        </li>
        <li>Import schema:
            <pre><code>mysql -u username -p banco < Banco.sql</code></pre>
        </li>
    </ol>
    <h2 id="usage">Usage</h2>
    <pre><code>python app.py</code></pre>
    <p>Access at: <a href="http://localhost:3000">http://localhost:3000</a></p>
    <h2 id="project-structure">Project Structure</h2>
    <pre>banking-system/
├── app.py
├── Banco.sql
├── templates/
│   ├── layout.html
│   ├── Index.html
│   ├── editarUsuario.html
│   └── historial.html
└── requirements.txt</pre>
    <h2 id="license">License</h2>
    <p>MIT © <a href="https://github.com/yourusername">Your Name</a></p>
</body>
</html>
