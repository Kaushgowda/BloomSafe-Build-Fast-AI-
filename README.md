AI Performance Coach

AI Performance Coach is a browser-based practice and performance coaching application designed for interviews, vivas, speeches, negotiations, and project demonstrations.

The application combines browser-based speech, camera, and screen capabilities with a Python backend and optional AI services to provide users with real-time practice, analysis, and personalized feedback.

Project Overview
Offline Features

The core functionality does not require an external API key. These features run locally on the user's computer and do not send the data to an external AI service.

Available offline features include:

Interview, viva, negotiation, speech, and demo modes
Pressure Mode
Live speaking pace tracking
Filler-word detection
Hedge-word detection
Pause tracking
Speaking timer
Target speaking length
Resume processing from DOCX, DOC, TXT, pasted text, and supported text PDFs
Questions generated from the user's resume, projects, and skills
Rule-based content analysis
Hook and signposting detection
Closing detection
Evidence and ownership analysis
Detection of repeated ideas
Camera self-view
Local lighting and movement checks
Scored performance reports
Personalized practice drills

These features are designed to continue working even when no AI API is configured.

Optional AI Features

The application can optionally connect to external AI providers to provide more advanced analysis.

Depending on the configured provider, AI features can include:

Adaptive follow-up questions based on the user's responses
AI-generated review of speech structure and content
More detailed performance feedback
Eye-contact analysis
Posture and presentation analysis
Camera snapshot analysis
Screen-aware project demonstration review
Processing of scanned or unusually encoded PDF documents
More dynamic and personalized coaching

The application can be configured to use services such as:

Google Gemini
OpenAI-compatible APIs
Groq
Anthropic Claude
Ollama for local AI models
The main goal of AI Performance Coach is to help users practice communication and presentation skills in a realistic environment.

The application supports multiple practice modes, including:

Interview practice
Viva practice
Speech practice
Negotiation practice
Project demonstration practice
Pressure Mode with unexpected questions and curveballs
Resume-based interview questions
Real-time speaking analysis
Performance reports and improvement drills
Camera-based presentation checks
Screen sharing for project demonstration practice

API Availability Notice

Some optional AI-powered features could not be fully demonstrated during development because the required third-party API keys were temporarily unavailable.

In particular, access to the following services was temporarily unavailable:

Google Gemini API
OpenAI API
Groq API

As a result, features that specifically depend on these external AI services may not be available in the current demonstration environment.

This does not affect the core offline functionality of the application. The application was designed so that many of its main practice, tracking, resume-processing, camera, and rule-based analysis features continue to work without an API key.

The limitation is related to temporary API availability and is not a limitation of the overall application architecture.

If valid API credentials are provided, the corresponding optional AI features can be enabled through the environment configuration.

Technologies Used
Frontend
HTML5
CSS3
JavaScript
Web Speech API
Browser Speech Synthesis API
Screen Capture API (getDisplayMedia)
Browser Camera APIs
Backend
Python
Python Standard Library HTTP Server
Environment variable configuration
Local file processing
AI Integration

The application supports optional integration with:

Google Gemini
OpenAI-compatible AI services
Groq
Anthropic Claude
Ollama
Resume Processing

The application supports resume processing from:

DOCX
DOC
TXT
Pasted text
Most text-based PDF files

AI services can additionally be used for processing scanned or unusually encoded documents when supported by the selected provider.

Setup and Installation
Requirements
Python 3.8 or newer
Google Chrome or Microsoft Edge
Microphone for voice features
Camera for camera-based features
Browser permission for microphone and camera access

No external Python packages are required for the basic offline version.

Step 1: Download the Project

Download or clone the project repository and open the project folder in a terminal or VS Code.

Step 2: Optional AI Configuration

The application can run without an API key.

If you want to use an AI provider, copy the example environment file:

cp .env.example .env

On Windows PowerShell:

Copy-Item .env.example .env

Then open .env and configure the required provider.

For example, for Gemini:

LLM_PROVIDER=gemini
GEMINI_API_KEY=your-api-key-here

For OpenAI-compatible services, configure the corresponding provider and API key according to the project's .env.example file.

For Ollama, which can run locally:

ollama pull llama3.2

Then configure:

LLM_PROVIDER=ollama

Ollama allows local text-based AI functionality without sending the conversation to an external AI provider.

Note that local text-only models do not provide camera or screen-image analysis. Those features require a vision-capable AI provider.

API Key Security

API keys should never be placed directly inside the frontend HTML or JavaScript files.

Store them in the .env file.

Example:

GEMINI_API_KEY=your-real-key

Never commit .env to GitHub or share your API keys publicly.

The .env.example file should contain placeholders rather than real API credentials.

How to Run the Project
Step 1: Open the Project Folder

Open a terminal in the project directory.

Step 2: Start the Python Server

Run:

python server.py

If your system uses python3:

python3 server.py

The application requires Python 3.8 or newer.

Step 3: Open the Application

After starting the server, open:

http://localhost:8000

in Google Chrome or Microsoft Edge.

Step 4: Enable Browser Permissions

Allow the browser to access:

Microphone
Camera, when using camera features
Screen sharing, when using project demonstration features

The browser handles speech recognition, speech synthesis, camera access, and screen sharing.

Camera Features

The camera can be enabled from the application interface.

The local camera functionality provides:

Mirrored self-view
Lighting feedback
Basic movement tracking
Basic framing checks
Face-in-frame information where browser support is available

When an appropriate AI vision provider is configured, camera snapshots can additionally be analyzed for:

Eye contact
Posture
Framing
Expression
Gestures

The local camera measurements are approximate indicators intended for practice rather than professional measurements.

Project Structure
AI Performance Coach/
│
├── server.py
├── index.html
├── .env.example
├── .gitignore
├── README.md
└── ...
Running Without an API Key

The project can be started directly without configuring any external AI service:

python server.py

Then open:

http://localhost:8000

The offline features will remain available.

This makes the application usable even when external AI services or API credentials are unavailable.

Running With an AI Provider

If an API key becomes available, configure the provider in .env and restart the server.

For example:

LLM_PROVIDER=gemini
GEMINI_API_KEY=your-real-key

The optional AI functionality will then be available according to the capabilities of the selected provider.

Important Note for Evaluation

The project was developed with a separation between core local functionality and optional external AI functionality.

Therefore:

The application does not require an API key to demonstrate its core functionality.
Several features operate completely on the user's device.
Optional AI functionality requires access to a supported AI provider.
During the current demonstration, some AI-powered features could not be tested because Gemini, OpenAI, and Groq API access was temporarily unavailable.
This is an external API availability limitation rather than a failure of the application's core functionality.
The corresponding AI features can be enabled when valid API credentials are available.
License

This project is intended for educational, demonstration, and development purposes.
