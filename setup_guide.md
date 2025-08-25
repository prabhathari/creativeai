# GenAI Chat Application - Complete Setup Guide

A full-stack AI chat application built with Python Flask, Google Gemini API, and React.

## 🏗️ Architecture Overview

```
Frontend (React)  →  Backend (Flask)  →  Gemini AI API
     ↓                    ↓                   ↓
- Modern UI          - REST API           - Text Generation
- Real-time chat     - Conversation       - Context Awareness
- Responsive         - CORS enabled       - Smart Responses
```

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+ (for development)
- Google AI API Key
- Modern web browser

## 🚀 Quick Start

### 1. Get Google AI API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy and save the key securely

### 2. Backend Setup

```bash
# Create project directory
mkdir genai-chat-app
cd genai-chat-app

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Create requirements.txt and install dependencies
pip install Flask==3.0.0 Flask-CORS==4.0.0 google-generativeai==0.3.2 python-dotenv==1.0.0 gunicorn==21.2.0

# Create environment file
echo "GOOGLE_API_KEY=your-actual-api-key-here" > .env

# Create app.py (copy the Flask backend code)
# Save the Flask backend code as app.py
```

### 3. Frontend Setup

```bash
# Create frontend directory
mkdir frontend
cd frontend

# Create index.html (copy the React frontend code)
# Save the React frontend code as index.html
```

### 4. Run the Application

```bash
# Terminal 1: Start Backend
cd genai-chat-app
python app.py

# Terminal 2: Serve Frontend (optional - can open HTML directly)
cd frontend
python -m http.server 3000
# Or simply open index.html in your browser
```

### 5. Access the Application

- Backend API: http://localhost:5000
- Frontend: Open `index.html` in your browser or http://localhost:3000

## 🔧 Configuration

### Environment Variables

Create a `.env` file in your project root:

```env
GOOGLE_API_KEY=your-actual-gemini-api-key
FLASK_ENV=development
FLASK_DEBUG=True
```

### API Endpoints

The Flask backend provides these endpoints:

- `GET /health` - Health check
- `POST /api/generate` - Simple text generation
- `POST /api/chat` - Contextual chat
- `GET /api/conversations` - List conversations
- `GET /api/conversations/<id>` - Get specific conversation
- `DELETE /api/conversations/<id>` - Clear conversation

## 🎨 Features

### Backend Features
- ✅ RESTful API with Flask
- ✅ Google Gemini AI integration
- ✅ Conversation management
- ✅ CORS enabled for cross-origin requests
- ✅ Error handling and logging
- ✅ Health check endpoint
- ✅ In-memory conversation storage

### Frontend Features
- ✅ Modern, responsive UI with glassmorphism design
- ✅ Real-time chat interface
- ✅ Multiple conversation support
- ✅ Message timestamps
- ✅ Loading indicators
- ✅ Error handling
- ✅ Backend status indicator
- ✅ Mobile-friendly design

## 🔒 Security Considerations

1. **API Key Security**: Never expose your API key in frontend code
2. **CORS Configuration**: Adjust CORS settings for production
3. **Input Validation**: Implement proper input sanitization
4. **Rate Limiting**: Consider implementing rate limiting for production
5. **Authentication**: Add user authentication for multi-user scenarios

## 🚢 Deployment Options

### Option 1: Local Development
- Use the setup above for local development and testing

### Option 2: Cloud Deployment

#### Backend (Heroku/Railway/Render)
```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy to your preferred platform
# Set GOOGLE_API_KEY as environment variable
```

#### Frontend (Netlify/Vercel/GitHub Pages)
- Deploy the HTML file to any static hosting service
- Update API_BASE_URL in the frontend to point to your deployed backend

### Option 3: Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  backend:
    build: .
    ports:
      - "5000:5000"
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
```

## 🧪 Testing

### Test Backend Endpoints

```bash
# Health check
curl http://localhost:5000/health

# Send a chat message
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, how are you?"}'
```

### Frontend Testing
- Open the HTML file in different browsers
- Test responsiveness on mobile devices
- Verify all features work correctly

## 🔧 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your Google AI API key is valid
   - Check the `.env` file is in the correct location
   - Verify the environment variable is loaded

2. **CORS Errors**
   - Make sure Flask-CORS is installed
   - Check that CORS is properly configured in the Flask app

3. **Frontend Can't Connect**
   - Verify backend is running on port 5000
   - Check the API_BASE_URL in the frontend code
   - Ensure no firewall is blocking the connection

4. **Dependencies Issues**
   - Make sure you're using the correct Python version
   - Try upgrading pip: `pip install --upgrade pip`
   - Use virtual environment to avoid conflicts

## 📈 Performance Optimization

1. **Backend Optimization**
   - Implement caching for repeated requests
   - Add database storage for conversations
   - Use connection pooling for API calls

2. **Frontend Optimization**
   - Implement message virtualization for large conversations
   - Add lazy loading for conversation history
   - Optimize bundle size with proper code splitting

## 🔄 Future Enhancements

- [ ] User authentication and authorization
- [ ] File upload and processing capabilities
- [ ] Voice input/output integration
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Real-time collaboration features
- [ ] Advanced AI model switching
- [ ] Message search and filtering
- [ ] Export conversation history
- [ ] Custom AI personality settings
- [ ] Integration with other AI models

## 📚 Additional Resources

- [Google AI Studio Documentation](https://ai.google.dev/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://reactjs.org/docs)
- [Gemini API Reference](https://ai.google.dev/api)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**Happy coding! 🚀** If you encounter any issues or have questions, feel free to reach out or create an issue in the repository.