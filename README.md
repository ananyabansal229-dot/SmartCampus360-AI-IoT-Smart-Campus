
# Smart Campus 360
### AI + IoT Smart Campus Intelligence

**Team Name:** Alpha  
**Hackathon:** Build With RW 2.0  
**Tracks:** AI/ML, Sustainability, Internet of Things, Open Innovation

## 1. Problem Statement

Campus information is often scattered across different services. Electricity, water, waste, infrastructure issues, student complaints, clubs, events, and campus facilities may be managed separately. This can delay issue detection, reduce resource efficiency, and make information difficult to access.

## 2. Our Solution

Smart Campus 360 proposes a unified digital platform that brings campus resource monitoring, student services, campus navigation, and sustainability insights into one place.

## 3. Key Features

- **AI + IoT Monitoring:** Electricity, water, waste, temperature, and air-quality monitoring.
- **AI Analytics:** Planned consumption prediction, anomaly detection, and resource optimisation.
- **Student Portal:** Report campus problems and track complaints.
- **Admin Dashboard:** View resource summaries, alerts, and reported issues.
- **Campus Maps:** Explore buildings, facilities, and campus destinations.
- **Food & Canteen Explorer:** Display sample menus and prices.
- **Library Explorer:** Organise books by subject and section.
- **Campus Connect:** Discover clubs, coordinators, and events.
- **Neighbourhood Intelligence:** Plan to show useful places within 50 km of campus.

## 4. System Architecture

                ┌─────────────────────┐
                │    IoT Sensors      │
                │ Electricity / Water │
                │ Waste / Environment │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   MQTT / API Layer  │
                │ Data & Protocol Mgmt │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Backend Server   │
                │ Business Logic      │
                │ Processing & APIs    │
                └──────────┬──────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
   ┌──────────────────┐       ┌──────────────────┐
   │ AI / ML Engine   │       │ Database         │
   │ Prediction       │       │ PostgreSQL /     │
   │ Anomaly Detection│       │ MongoDB          │
   │ Classification   │       │ Secure Storage   │
   └────────┬─────────┘       └────────┬─────────┘
            │                          │
            └────────────┬─────────────┘
                         ▼
               ┌─────────────────────┐
               │   Web Dashboard     │
               │ Students / Admin    │
               └─────────────────────┘

## 5. Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- Database: SQLite
- Planned extensions: MQTT, IoT sensors, React, and AI/ML models

## 6. Current Prototype Status

This repository is a prototype. Sample dashboard values and campus records are illustrative. Real sensor integrations, trained AI/ML predictions, live route calculation, authentication, and production deployment are future development tasks.

## 7. Run Locally

1. Install Python 3.11 or newer.
2. Create and activate a virtual environment.
3. Install dependencies using `python -m pip install -r requirements.txt`.
4. Start the server using `python -m uvicorn backend.app:app --reload`.
5. Open `http://127.0.0.1:8000` in your browser.
6. Open `http://127.0.0.1:8000/docs` to inspect the API.

Detailed instructions: `docs/setup.md`.

## 8. Project Architecture

IoT Sensors (planned) → MQTT/API Layer (planned) → Backend Server → Database → Web Dashboard.

The current prototype uses a backend API and local database, with illustrative data for features that are not yet connected to real systems.

## 9. Team Alpha

- Ananya Bansal — AI/ML & Data Analytics Lead
- Arushi Shrikar — Frontend & Student Portal Lead
- Akshay Singhal — Backend & Database Lead
- Sparsh Dheer — IoT & System Integration Lead

## 10. Roadmap

1. Foundation: Campus database, facilities, and dashboard.
2. Intelligence: IoT integration, analytics, and anomaly detection.
3. Student Layer: Campus maps, routes, menus, library, and student services.
4. Smart Campus: Sustainability insights and neighbourhood information.

## 11. Limitations and Future Scope

This prototype does not yet connect to real IoT sensors, train prediction models, calculate live routes, or provide production-grade authentication. These features require further development and testing.

## 12. Supporting Materials

See the `docs/` and `supporting-materials/` folders for architecture, setup instructions, risks, screenshots, and demonstration materials.
