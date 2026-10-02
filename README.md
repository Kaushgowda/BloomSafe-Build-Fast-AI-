# AI Performance Coach

AI Performance Coach is a browser-based practice and performance coaching application designed for interviews, vivas, speeches, negotiations, and project demonstrations.

The application combines browser-based speech, camera, and screen capabilities with a Python backend and optional AI services to provide users with real-time practice, analysis, and personalized feedback.

## Project Overview

The AI Performance Coach allows users to practice communication and presentation skills through an interactive web interface.

The application supports multiple practice modes, including:

- Interview practice
- Viva practice
- Speech practice
- Negotiation practice
- Project demonstration practice
- Pressure Mode with unexpected questions and curveballs
- Resume-based interview questions
- Real-time speaking analysis
- Performance reports and improvement drills
- Camera-based presentation checks
- Screen sharing for project demonstration practice

The project is designed with a flexible architecture where the core functionality can operate locally, while optional AI services can be configured when API access is available.

### Offline Features

The core functionality does not require an external API key. These features run locally on the user's computer and do not send the data to an external AI service.

Available offline features include:

- Interview, viva, negotiation, speech, and demo modes
- Pressure Mode
- Live speaking pace tracking
- Filler-word detection
- Hedge-word detection
- Pause tracking
- Speaking timer
- Target speaking length
- Resume processing from DOCX, DOC, TXT, pasted text, and supported text PDFs
- Questions generated from the user's resume, projects, and skills
- Rule-based content analysis
- Hook and signposting detection
- Closing detection
- Evidence and ownership analysis
- Detection of repeated ideas
- Camera self-view
- Local lighting and movement checks
- Scored performance reports
- Personalized practice drills

These features are designed to continue working even when no AI API is configured.

### Optional AI Features

The application can optionally connect to external AI providers to provide more advanced analysis.

Depending on the configured provider, AI features can include:

- Adaptive follow-up questions based on the user's responses
- AI-generated review of speech structure and content
- More detailed performance feedback
- Eye-contact analysis
- Posture and presentation analysis
- Camera snapshot analysis
- Screen-aware project demonstration review
- Processing of scanned or unusually encoded PDF documents
- More dynamic and personalized coaching

The application can be configured to use supported AI services such as:

- Google Gemini
- OpenAI-compatible APIs
- Anthropic Claude
- Groq
- Ollama for local AI models

## Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript
- Web Speech API
- Browser Speech Synthesis API
- Screen Capture API (`getDisplayMedia`)
- Browser Camera APIs

### Backend

- Python
- Python Standard Library HTTP Server
- HTTP APIs
- Environment variable configuration
- Local file processing

### AI / LLM Integration

The application supports optional integration with:

- Google Gemini
- OpenAI-compatible AI services
- Anthropic Claude
- Groq
- Ollama

The available AI functionality depends on the configured provider and its supported capabilities.

### Resume Processing

The application supports resume processing from:

- DOCX
- DOC
- TXT
- Pasted text
- Most text-based PDF files

AI services can additionally be used for processing scanned or unusually encoded PDF documents when supported by the selected provider.

## Setup and Installation

### Requirements

- Python 3.8 or newer
- Google Chrome or Microsoft Edge
- Microphone for voice features
- Camera for camera-based features
- Browser permission for microphone and camera access

No external Python packages are required for the basic offline version.

### 1. Download or Clone the Project

Download or clone the project repository and open the project folder in VS Code or another code editor.

### 2. Open the Project Directory

```bash
cd ai-performance-coach
