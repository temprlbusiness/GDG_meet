<p align="center">
  <img src="https://business.temprl.pro/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo_with_pro.20f29042.png&w=384&q=75" alt="Temprl Business Logo" height="120">
</p>

# 🚀 Google Developer Group (GDG) Meet - Demo Agents

## 🎯 About This Repository
This repository is created to **showcase how AI agents are developed and utilized**. The demo projects provide insights into building AI-powered assistants using **Ollama Qwen2.5-0.5B** and deploying them both locally and on the cloud with **VLLM Runpod**. 

### 🛠️ Technologies Used
- **Ollama Qwen2.5-0.5B**: A powerful AI model for conversational AI.
- **LangChain**: For managing and integrating AI agents with various tools.
- **VLLM Runpod**: Efficient cloud-based deployment for scalable AI inference.

---

## 📌 Demo Agents

### 1️⃣ Ollama Agent
🔹 **Description**: An interactive AI-powered assistant leveraging **Ollama Qwen2.5-0.5B** for conversational AI.

🔹 **Features**:
- Context-aware chat
- Supports both local and cloud (VLLM Runpod) deployment
- Optimized for quick responses and low-latency interactions

🔹 **Usage**:
```bash
# Local Deployment
ollama run Qwen2.5-0.5B

# Cloud Deployment using Runpod
python ollama_agent.py --model Qwen2.5-0.5B
```

---

### 2️⃣ Weather Agent
🔹 **Description**: A weather assistant that fetches real-time weather updates based on user queries.

🔹 **Features**:
- Provides current weather and forecasts
- Supports both local and cloud deployment
- Uses **Ollama Qwen2.5-0.5B** for intelligent query handling

🔹 **Usage**:
```bash
# Local Deployment
ollama run Qwen2.5-0.5B --task weather

# Cloud Deployment using Runpod
python weather.py --model Qwen2.5-0.5B
```

---

## 🛠️ Setup and Installation
### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai/) installed
- [Runpod CLI](https://runpod.io/) for cloud execution

### Installation Steps
```bash
# Clone the repository
git clone https://github.com/your-repo/gdg-demo-agents.git
cd gdg-demo-agents

# Install dependencies
pip install -r requirements.txt
```

---

## 🌐 Cloud Deployment with VLLM Runpod
To deploy the agents on **VLLM Runpod**, use the following command:
```bash
runpodctl start --image vllm-runpod/qwen2.5-0.5B --config config.json
```

---

## 🔗 Reference Links
📌 [LangChain DuckDuckGo Tool](https://python.langchain.com/docs/integrations/tools/ddg/)  
📌 [VLLM Quickstart Guide](https://docs.vllm.ai/en/stable/getting_started/quickstart.html)  
📌 [Ollama Structured Outputs](https://ollama.com/blog/structured-outputs)  

---

## 📢 Contact & Support
For any queries, feel free to reach out!
- **Google Developer Group (GDG)**
- Email: [contact@gdgmeet.com](mailto:contact@gdgmeet.com)
- GitHub Issues: [Open an Issue](https://github.com/your-repo/gdg-demo-agents/issues)

Happy Coding! 🎉