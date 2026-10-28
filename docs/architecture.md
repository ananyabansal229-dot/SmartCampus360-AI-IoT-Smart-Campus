
# System Architecture — Smart Campus 360

## Overview

Smart Campus 360 is designed as a unified platform for campus resource information, sustainability, navigation, and student services.

## Proposed Architecture

1. **IoT Sensors:** Planned collection of electricity, water, waste, temperature, and air-quality readings.
2. **Messaging/API Layer:** MQTT or HTTP APIs are planned for transporting sensor information.
3. **Backend Server:** Python FastAPI provides API endpoints and application logic in the current prototype.
4. **Database:** SQLite stores demonstration complaint records locally.
5. **Frontend:** HTML, CSS, and JavaScript display summaries and support complaint submission.
6. **AI/ML Engine:** Future integration for consumption prediction, anomaly detection, waste classification, and resource optimisation.
7. **Admin and Student Services:** Planned modules include campus maps, food menus, library information, verified contacts, clubs, and events.

## Current Data Flow

Browser → FastAPI endpoint → SQLite database → API response → Browser.

The dashboard summary includes illustrative resource values. It does not receive live sensor readings.

## Future Data Flow

IoT Sensors → MQTT/API Layer → Backend → Database and AI/ML Analytics → Dashboard and Alerts.

## Design Goals

- Centralised campus information
- Modular feature development
- Clear separation between frontend and backend
- Transparent distinction between sample and live data
- Future support for secure, role-based access

## Current Limitations

Real IoT ingestion, MQTT messaging, trained AI/ML models, live route calculation, authentication, and production cloud deployment are not implemented in this prototype.
