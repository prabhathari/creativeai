# 🤖 GenAI Chat Application

A simple AI chat application powered by Google's Gemini AI. Built with Flask backend and React frontend, ready to run with Docker.

![Docker](https://img.shields.io/badge/docker-ready-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-green.svg)

## ✨ Features

- 💬 **AI Chat**: Powered by Google Gemini AI
- 🎨 **Clean UI**: Simple, responsive interface
- 🐳 **Docker Ready**: One-command setup
- 🔒 **Secure**: You provide your own API key

## 🚀 Quick Start

### Prerequisites

- Docker installed on your computer
- Google Gemini API key ([Get one free here](https://makersuite.google.com/app/apikey))

### Option 1: Run with Docker Compose (Full App)

```bash
# 1. Download the files
git clone https://github.com/your-username/genai-chat-app
cd genai-chat-app

# 2. Start the application
# Windows (PowerShell):
$env:GEMINI_API_KEY="your-api-key-here"
docker-compose up -d

# Linux/Mac:
GEMINI_API_KEY="your-api-key-here" docker-compose up -d

# 3. Open your browser
# Chat Interface: http://localhost:3000
# Backend API: http://localhost:5000
```

### Option 2: Run from Docker Hub (API Only)

```bash
# Windows (PowerShell):
docker run -d -p 5000:5000 -e GEMINI_API_KEY="your-api-key" prabhathari/genai-chat-app

# Linux/Mac:
docker run -d -p 5000:5000 -e GEMINI_API_KEY="your-api-key" prabhathari/genai-chat-app

# Access API at: http://localhost:5000
```

## 🛠️ Local Development (Without Docker)

```bash
# 1. Setup Python environment
python -m venv .venv

# Windows:
.venv\Scripts\activate

# Linux/Mac:
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirement.txt

# 3. Set your API key
# Windows (PowerShell):
$env:GEMINI_API_KEY="your-api-key"

# Linux/Mac:
export GEMINI_API_KEY="your-api-key"

# 4. Run the server
python app.py

# 5. Open react_frontend.html in your browser
```

## 📁 Project Files

```
genai-chat-app/
├── app.py                 # Flask backend server
├── react_frontend.html    # React frontend (single file)
├── requirement.txt        # Python dependencies
├── Dockerfile            # Docker setup
├── docker-compose.yml    # Multi-container setup
└── README.md             # This file
```

## 🔌 API Usage

### Send a Chat Message
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello AI!"}'
```

### Health Check
```bash
curl http://localhost:5000/health
```

### Clear Chat History
```bash
curl -X DELETE http://localhost:5000/api/chat
```

## 🐛 Troubleshooting

### "API Key not found" error
Make sure you set the environment variable correctly:

**Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY="your-actual-api-key"
docker-compose up -d
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY="your-actual-api-key"
docker-compose up -d
```

### Port already in use
```bash
# Use different ports
docker run -p 5001:5000 -e GEMINI_API_KEY="your-key" prabhathari/genai-chat-app
```

### Can't connect to backend
Update the API URL in `react_frontend.html`:
```javascript
const API_BASE_URL = 'http://localhost:5000'; // Make sure this matches your backend port
```

## 🛑 Stop the Application

```bash
# If using docker-compose
docker-compose down

# If using docker run
docker stop <container-name>
```

## 📦 Docker Hub

**Image:** `prabhathari/genai-chat-app`

Pull the latest version:
```bash
docker pull prabhathari/genai-chat-app:latest
```

## 🔗 Get Your API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key and use it in the commands above

**Note:** Keep your API key private and never commit it to version control!

## 🤝 Contributing

Found a bug or want to add a feature? 
1. Fork the repo
2. Make your changes
3. Submit a pull request

## 📄 License

MIT License - feel free to use this code for your own projects!

---

**🎉 Enjoy chatting with AI!**

Questions? Open an issue on GitHub or check the troubleshooting section above.