# ai-devops-bot


[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen)](https://streamlit.io/cloud)

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Installation & Setup](#installation--setup)
* [Running Locally](#running-locally)
* [Deployment](#deployment)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgements](#acknowledgements)

---

## Project Overview

The **AI DevOps Bot** is an intelligent assistant designed to automate key development operations such as:

* Issue summary generation from ticket descriptions
* Automated test case generation
* Code review suggestions and analysis

Built to streamline and accelerate software development workflows, this project leverages AI and natural language processing models to provide actionable insights and assistance directly through a user-friendly web interface.

The app is developed using Python and deployed as an interactive web application using [Streamlit](https://streamlit.io/).

Absolutely! Here's a section you can add under **Deployment** or as a separate **CI/CD & Cloud Usage** section explaining your GitLab and Google Cloud usage clearly and transparently:

---

## CI/CD and Cloud Usage

### GitLab CI/CD

We use **GitLab** as our code repository and continuous integration (CI) platform to manage and maintain the project’s source code. GitLab CI pipelines help us automate:

* Running tests and static analysis on every commit to ensure code quality
* Building Docker images for containerized environments
* Preparing deployment artifacts

However, due to project constraints and resource optimization, the full automated deployment pipeline was not finalized.

### Google Cloud Usage

Google Cloud (GC) was used primarily to **run and test our application code once** on a virtual machine instance. This allowed us to verify the app's functionality in a cloud environment and ensure compatibility with cloud infrastructure.

**Important:** The app was *not* deployed as a fully managed or production-ready service on Google Cloud due to **storage constraints**. Instead, we opted to deploy the app on **Streamlit Cloud** for easy public access and simpler maintenance.

This approach balanced demonstrating cloud compatibility and keeping the deployment straightforward for reviewers and users.

---

If you want, I can help you integrate this neatly into your full README!


---

## Features

* **Issue Summarization:** Automatically generates concise summaries from verbose issue descriptions.
* **Test Generation:** Creates initial test cases based on code and issue context to accelerate QA processes.
* **Code Review:** Provides AI-powered suggestions and highlights potential issues in code snippets.
* **Interactive UI:** User-friendly, real-time interface accessible via any modern browser.

---

## Tech Stack

* Python 3.12
* Streamlit (for web UI)
* AI/ML libraries (e.g., transformers, OpenAI API integration, or any specific NLP models used)
* Docker (optional, for containerization)
* GitHub (code repository)
* Streamlit Cloud (for deployment)

---

## Installation & Setup

To run this app locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/ai-devops-bot.git
   cd ai-devops-bot
   ```

2. **Create and activate a Python virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API keys or environment variables:**

   If your app uses any external APIs (OpenAI, etc.), create a `.env` file or export environment variables accordingly.

---

## Running Locally

Start the Streamlit app locally by running:

```bash
streamlit run app.py
```

This will launch the app on `http://localhost:8501` in your default web browser.

---

## Deployment

The app is deployed on **Streamlit Cloud** for easy access without local setup.

### Deploying on Streamlit Cloud:

1. Push your latest code to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Sign in with GitHub and create a new app by connecting your repository.
4. Select the main file (`app.py`) and branch (usually `main` or `master`).
5. Click **Deploy** — the app will automatically build and be available at a public URL.

**Note:** Update your API keys in the Streamlit Cloud secrets manager if needed.

---

## Usage

* Open the deployed Streamlit app URL or run it locally.
* Use the sidebar or main interface to enter issue descriptions, code snippets, or test requirements.
* Receive generated summaries, test cases, or code review feedback interactively.
* Iterate by updating inputs and refining outputs.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request describing your changes.

Please adhere to the existing code style and include tests where applicable.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

* Thanks to the [Streamlit](https://streamlit.io/) team for making deployment easy.
* AI model providers and open-source contributors whose work powers this app.
* [Google Cloud](https://cloud.google.com/) for sponsoring and supporting the hackathon environment.

---

