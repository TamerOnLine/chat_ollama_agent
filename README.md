# **tameronline-chat_ollama**

## 📝 **Overview**
`tameronline-chat_ollama` is an AI-powered project built on **LangChain** and **Ollama LLM**, designed to provide an intelligent agent capable of handling user queries related to weather updates, stock prices, and general responses.

## 🚀 **Features**
- **AI-Powered Agent**: Utilizes LangChain to create an intelligent agent that processes queries.
- **Multi-Tool Support**:
  - `weather_tool`: Fetches weather data from the OpenWeather API.
  - `stock_tool`: Retrieves stock prices using Yahoo Finance.
  - `custom_tool`: Handles general queries not covered by other tools.
- **Automated Virtual Environment Setup**: Supports **Windows**, **Linux**, and **macOS**.
- **GitHub Actions Integration**: Ensures smooth operation through **CI/CD pipelines**.

---

## 🔧 **Installation & Setup**

### **Prerequisites**
- **Python 3.6+**
- **Git** (for repository cloning)
- **VS Code** (optional)

### **Setup Steps**
#### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/TamerOnLine/chat_ollama.git
cd chat_ollama
```

#### 2️⃣ **Set Up the Virtual Environment & Install Dependencies**
##### 🔹 **Windows (Command Prompt)**
```cmd
activate_project.bat
```
##### 🔹 **Windows (PowerShell)**
```powershell
.\activate_project.ps1
```
##### 🔹 **Linux/macOS**
```bash
chmod +x activate_project.sh
./activate_project.sh
```

#### 3️⃣ **Run the Application**
```bash
python src/main.py
```

---

## 🏗 **Project Structure**
```
chat_ollama/
├── README.md                # Documentation
├── LICENSE                  # License file
├── activate_project.bat     # Windows CMD script
├── activate_project.ps1     # Windows PowerShell script
├── activate_project.sh      # Linux/macOS Bash script
├── requirements.txt         # Dependency list
├── src/                     # Source code
│   ├── main.py              # Main application
│   ├── agent/               # AI agent logic
│   │   ├── __init__.py
│   │   ├── agent.py         # Agent implementation
│   ├── model/
│   │   ├── __init__.py
│   │   ├── ollama_model.py  # Ollama model integration
│   ├── tools/               # Additional tools
│   │   ├── custom_tool.py   # General response tool
│   │   ├── stock_tool.py    # Stock price tool
│   │   ├── weather_tool.py  # Weather data tool
├── tests/                   # Unit tests
│   ├── test_custom_tool.py
│   ├── test_main.py
│   ├── test_ollama_model.py
│   ├── test_stock_tool.py
│   ├── test_weather_tool.py
└── .github/workflows/       # CI/CD Integration
    ├── ci.yml
    ├── main.yml
```

---

## 🛠 **Usage**
### **1️⃣ Run the Main Application**
After installing dependencies, you can start the app with:
```bash
python src/main.py
```
This allows users to ask about weather updates or stock prices.

### **2️⃣ Run an Individual Script**
```bash
python src/agent/agent.py
```

### **3️⃣ Run Tests**
```bash
pytest tests/
```

---

## ❓ **Troubleshooting**
| Issue | Solution |
|---------|---------|
| Python not found | Ensure **Python 3.6+** is installed and added to the system path. |
| Virtual environment activation failure | Delete the `venv` directory and rerun the activation script. |
| Permission issues on macOS/Linux | Use `chmod +x activate_project.sh` before execution. |

---

## 🤝 **Contributing**
- Feel free to submit **pull requests** or report **issues** on the [GitHub repository](https://github.com/TamerOnLine/chat_ollama).

---

## 📄 **License**
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for more details.

---

## 🔗 **Additional Resources**
- [GitHub Repository](https://github.com/TamerOnLine/chat_ollama)
- [LangChain Documentation](https://python.langchain.com)
- [Ollama LLM](https://ollama.com)

---

🚀 Enjoy using this AI-powered agent! Have any improvements in mind? 😊

