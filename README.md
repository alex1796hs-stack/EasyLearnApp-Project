<div align="center">
  <h1>🚀 EasyLearn</h1>
  <p><strong>AI-Powered Adaptive English Learning Platform</strong></p>
  
  [![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
  [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
  [![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
  [![Vite](https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E)](https://vitejs.dev/)
</div>

<br/>

*Read this in other languages: [English](#english) | [Nederlands](#nederlands) | [Español](#español)*


<a name="nederlands"></a>
## 🇳🇱 Nederlands

### Overzicht

**EasyLearn** is een moderne, data-gestuurde educatieve full-stack webapplicatie ontworpen om het leren van de Engelse taal te transformeren. Door gebruik te maken van adaptieve algoritmen en *spaced repetition*-methodologieën stemt het platform oefeningen dynamisch af op het individuele vaardigheidsniveau van elke student—over het gehele Europees Referentiekader (**ERK / CEFR**), van **A1 (Beginner)** tot **C2 (Gevorderd)**.

Gebouwd met een responsieve **React + Vite + Tailwind CSS** frontend en een krachtige **Python + FastAPI + PostgreSQL** backend, biedt EasyLearn een vloeiende, interactieve en gamified leerervaring.

---

### ✨ Belangrijkste Kenmerken

- **🎯 Diagnostische Niveautest (Placement Test):**
  - Dynamische diagnostische toets die grammatica, woordenschat, lees- en luistervaardigheid evalueert.
  - Bepaalt automatisch de sterke en zwakke punten en wijst een initieel ERK-niveau toe (A1–C2).
  - Slaat gedetailleerde antwoordanalyses op om de vervolglessen te personaliseren.

- **🔁 Slim Herhalingssysteem (Spaced Repetition):**
  - Algoritme dat foute antwoorden registreert en patronen van veelvoorkomende vergissingen analyseert.
  - Genereert op maat gemaakte herhalingsquizzen specifiek gericht op verbeterpunten.
  - Ingebouwde **Text-to-Speech (TTS)** spraaksynthese voor natuurlijke Engelse uitspraakoefeningen.

- **📅 Activiteiten-Heatmap & Consistentiekalender:**
  - Visuele, op GitHub geïnspireerde heatmap die dagelijkse leerreeksen (*streaks*), voltooide tests en studieconsistentie bijhoudt.
  - Stimuleert een gezonde dagelijkse leergewoonte via visuele feedback en mijlpalen.

- **🏆 Leerlingprofiel & Gamificatie:**
  - Ervaringspunten (XP), badges, niveauvoortgangsbalken en voltooide leereenheden.
  - Historische testresultaten, uitgebreide foutenanalyses en prestatiegrafieken.

- **💎 Modern Glassmorphic Dark UI:**
  - Geavanceerde donkere interface met matglazen kaarten (*frosted glass*), sfeervolle kleurverlopen, responsieve lay-outs en soepele micro-animaties.

- **🔒 Betrouwbare Beveiliging & Sessiebeheer:**
  - Veilige gebruikersauthenticatie via **JWT** (JSON Web Tokens).
  - Wachtwoordversleuteling met **Bcrypt**, beveiligde FastAPI-routes en geoptimaliseerde CORS-beveiliging.

---

### 🛠️ Architectuur & Technologieën

| Laag | Technologieën |
| :--- | :--- |
| **Frontend** | React, Vite, Tailwind CSS, Lucide Icons, Axios, Web Speech API (TTS) |
| **Backend** | Python 3.10+, FastAPI, SQLAlchemy, Pydantic, Uvicorn |
| **Beveiliging** | OAuth2 Password Flow, Python-Jose (JWT), Passlib (Bcrypt) |
| **Database** | PostgreSQL, Alembic (Database-migraties) |
| **DevOps & Tools** | Docker, Docker Compose, Git, GitHub |

---

### 🚀 Aan de Slag

#### Vereisten
- [Node.js](https://nodejs.org/) (v18.0 of hoger)
- [Python](https://www.python.org/) (v3.10 of hoger)
- [Docker & Docker Compose](https://www.docker.com/) (Aanbevolen voor databasebeheer)

---

#### Optie 1: Snel starten met Docker Compose (Aanbevolen)

1. **Kloon de repository:**
   ```bash
   git clone https://github.com/alex1796hs-stack/EasyLearnApp-Project.git
   cd EasyLearnApp-Project

---

<a name="english"></a>
## 🇬🇧 English

EasyLearn is a modern, data-driven full-stack application designed to revolutionize English language learning. By leveraging adaptive algorithms, the platform dynamically adjusts to the student's level (from A1 to C2) and provides targeted reviews to reinforce weak areas.

### ✨ Key Features

*   **Dynamic Placement Tests:** Intelligent diagnostic exams that accurately gauge the user's CEFR level and persist detailed answer analytics for future review.
*   **Smart Review System:** A targeted spaced-repetition module that identifies historically failed questions and builds customized, interactive quizzes. Features integrated Text-to-Speech (TTS) pronunciation.
*   **Activity Heatmap (Calendar):** A GitHub-style contribution graph providing visual feedback on learning streaks, tests completed, and overall engagement.
*   **Premium Glassmorphism UI:** Built with Tailwind CSS, the interface boasts a modern, responsive, and immersive aesthetic with complex gradient backgrounds and frosted glass components.
*   **Full CEFR Curriculum:** Database architecture capable of supporting and deploying comprehensive grammatical structures across 26 discrete educational units.

### 🛠️ Technology Stack

*   **Frontend:** React, Vite, Tailwind CSS, React Router, Axios.
*   **Backend:** Python, FastAPI, SQLAlchemy, Pydantic, JWT Authentication.
*   **Database:** PostgreSQL (Dockerized).

### 🚀 Getting Started

#### Prerequisites
*   Node.js (v18+)
*   Python (3.10+)
*   Docker & Docker Compose

#### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/EasyLearn.git
    cd EasyLearn
    ```

2.  **Start the entire stack (Database, Backend, and Frontend):**
    ```bash
    docker compose up --build
    ```

3.  **Seed the Database (First time only):**
    Open a new terminal and run:
    ```bash
    docker exec -it easylearn-backend-1 python -m scripts.generate_units
    ```

4.  **Access the application:**
    *   Frontend: `http://localhost:5173`
    *   Backend API Docs: `http://localhost:8000/docs`

---

<br/><br/>

<a name="español"></a>
## 🇪🇸 Español

EasyLearn es una aplicación full-stack moderna y orientada a datos, diseñada para revolucionar el aprendizaje del idioma inglés. Mediante el uso de algoritmos adaptativos, la plataforma se ajusta dinámicamente al nivel del estudiante (de A1 a C2) y proporciona repasos específicos para reforzar sus puntos débiles.

### ✨ Características Principales

*   **Exámenes de Nivel Dinámicos:** Pruebas de diagnóstico inteligentes que calculan con precisión el nivel MCER (CEFR) del usuario, almacenando estadísticas detalladas de cada respuesta para su posterior revisión.
*   **Sistema de Repaso Inteligente:** Un módulo avanzado que identifica las preguntas falladas históricamente y genera cuestionarios interactivos personalizados. Cuenta con integración de síntesis de voz (Text-to-Speech) para mejorar la pronunciación.
*   **Mapa de Calor de Actividad:** Un calendario estilo GitHub que proporciona retroalimentación visual sobre rachas de aprendizaje, exámenes completados y nivel de compromiso diario del estudiante.
*   **Interfaz Premium Glassmorphism:** Construida con Tailwind CSS, la interfaz destaca por una estética moderna, responsiva y envolvente, con fondos degradados y componentes de cristal esmerilado.
*   **Plan de Estudios Completo:** Arquitectura de base de datos diseñada para desplegar el currículo gramatical completo distribuido en 26 unidades educativas.

### 🛠️ Stack Tecnológico

*   **Frontend:** React, Vite, Tailwind CSS, React Router, Axios.
*   **Backend:** Python, FastAPI, SQLAlchemy, Pydantic, Autenticación JWT.
*   **Base de Datos:** PostgreSQL (Dockerizado).

### 🚀 Guía de Inicio Rápido

#### Requisitos Previos
*   Node.js (v18+)
*   Python (3.10+)
*   Docker & Docker Compose

#### Instalación

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/EasyLearn.git
    cd EasyLearn
    ```

2.  **Iniciar todo el entorno (Base de Datos, Backend y Frontend):**
    ```bash
    docker compose up --build
    ```

3.  **Poblar la Base de Datos (Solo la primera vez):**
    Abre una nueva terminal y ejecuta:
    ```bash
    docker exec -it easylearn-backend-1 python -m scripts.generate_units
    ```

4.  **Acceder a la aplicación:**
    *   Frontend: `http://localhost:5173`
    *   Documentación API: `http://localhost:8000/docs`
