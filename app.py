from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from datetime import datetime
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Configure Gemini API - try both environment variable names
API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)

# Initialize Gemini model - use the model that works for you
try:
    model = genai.GenerativeModel('models/gemma-3-27b-it')
    print("✅ Using Gemma 3 model")
except Exception as e:
    try:
        model = genai.GenerativeModel('gemini-pro')
        print("✅ Using Gemini Pro model")
    except Exception as e2:
        model = genai.GenerativeModel('gemini-1.5-flash')
        print("✅ Using Gemini 1.5 Flash model")

# In-memory storage for conversation history
conversations = {}

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'GenAI Flask Backend'
    })

@app.route('/api/generate', methods=['POST'])
def generate_text():
    """Generate text using Gemini AI"""
    try:
        data = request.get_json()
        
        if not data or 'prompt' not in data:
            return jsonify({'error': 'Prompt is required'}), 400
        
        prompt = data['prompt']
        conversation_id = data.get('conversation_id', 'default')
        
        # Get or create conversation history
        if conversation_id not in conversations:
            conversations[conversation_id] = []
        
        # Add user message to history
        conversations[conversation_id].append({
            'role': 'user',
            'content': prompt,
            'timestamp': datetime.now().isoformat()
        })
        
        # Generate response using Gemini
        response = model.generate_content(prompt)
        
        if not response.text:
            return jsonify({'error': 'Failed to generate response'}), 500
        
        # Add AI response to history
        ai_response = {
            'role': 'assistant',
            'content': response.text,
            'timestamp': datetime.now().isoformat()
        }
        conversations[conversation_id].append(ai_response)
        
        return jsonify({
            'response': response.text,
            'conversation_id': conversation_id,
            'message_count': len(conversations[conversation_id])
        })
        
    except Exception as e:
        logger.error(f"Error generating text: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/conversations/<conversation_id>', methods=['GET'])
def get_conversation(conversation_id):
    """Get conversation history"""
    try:
        if conversation_id not in conversations:
            return jsonify({'messages': []})
        
        return jsonify({
            'conversation_id': conversation_id,
            'messages': conversations[conversation_id]
        })
        
    except Exception as e:
        logger.error(f"Error fetching conversation: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/conversations/<conversation_id>', methods=['DELETE'])
def clear_conversation(conversation_id):
    """Clear conversation history"""
    try:
        if conversation_id in conversations:
            del conversations[conversation_id]
        
        return jsonify({'message': 'Conversation cleared successfully'})
        
    except Exception as e:
        logger.error(f"Error clearing conversation: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/conversations', methods=['GET'])
def list_conversations():
    """List all conversation IDs"""
    try:
        return jsonify({
            'conversations': list(conversations.keys()),
            'total': len(conversations)
        })
        
    except Exception as e:
        logger.error(f"Error listing conversations: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/chat', methods=['POST'])
def chat_with_context():
    """Chat with conversation context"""
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        message = data['message']
        conversation_id = data.get('conversation_id', 'default')
        system_prompt = data.get('system_prompt', '')
        
        # Get conversation history
        if conversation_id not in conversations:
            conversations[conversation_id] = []
        
        # Build context from conversation history
        context = ""
        if system_prompt:
            context += f"System: {system_prompt}\n\n"
        
        # Add recent conversation history (last 10 messages)
        recent_messages = conversations[conversation_id][-10:]
        for msg in recent_messages:
            role = "Human" if msg['role'] == 'user' else "Assistant"
            context += f"{role}: {msg['content']}\n"
        
        # Add current message
        context += f"Human: {message}\nAssistant:"
        
        # Generate response
        response = model.generate_content(context)
        
        if not response.text:
            return jsonify({'error': 'Failed to generate response'}), 500
        
        # Save messages to conversation history
        conversations[conversation_id].append({
            'role': 'user',
            'content': message,
            'timestamp': datetime.now().isoformat()
        })
        
        conversations[conversation_id].append({
            'role': 'assistant',
            'content': response.text,
            'timestamp': datetime.now().isoformat()
        })
        
        return jsonify({
            'response': response.text,
            'conversation_id': conversation_id,
            'message_count': len(conversations[conversation_id])
        })
        
    except Exception as e:
        logger.error(f"Error in chat: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Check if API key is configured
   
    
    print("🚀 Starting GenAI Flask Backend...")
    print("📝 Available endpoints:")
    print("   GET  /health - Health check")
    print("   POST /api/generate - Generate text")
    print("   POST /api/chat - Chat with context")
    print("   GET  /api/conversations - List conversations")
    print("   GET  /api/conversations/<id> - Get conversation")
    print("   DELETE /api/conversations/<id> - Clear conversation")
    
    app.run(debug=True, host='0.0.0.0', port=5000)