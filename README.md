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
    </ul>
    <h2 id="features">Features</h2>
    <ul class="feature-list">
        <li>✅ User account management</li>
        <li>💰 Deposit/withdrawal processing</li>
        <li>📊 Balance calculation</li>
        <li>🕵️ Transaction history tracking</li>
        <li>🔄 CRUD operations</li>
    </ul>
    <h2 id="Instructions">Setup Instructions</h2>
    <ol>
     <li>Setting Up a Virtual Environment:
         <pre><code>git clone https://github.com/facuezequielpat/GestorDeCuentasBancarias
cd GestorDeCuentasBancarias
python -m venv venv</code></pre>
     </li>
     <li>Activate Virtual Environment (From CMD):
         <pre><code>source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows</code></pre>
     </li>
     <li>Install Frameworks:
         <pre><code>pip install flask flask_mysqldb</code></pre>
     </li>
     <li>Configure database:
<ul><li>Execute Banco.sql script in MySQL</li>
<li>Verify credentials in app.py (lines 12-15)</li></ul>
     <br>
     </li>
     <li>Run the application:
      <pre><code>python app.py</code></pre>
     </li>
     <li>Access the application:<br>
      Open in browser: <pre><a href="http://localhost:3000">http://localhost:3000</a></pre>
     </li>
    </ol>
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
    <p>MIT © <a href="https://github.com/facuezequielpat">Facundo Ezequiel Patiño</a></p>
</body>
</html>
