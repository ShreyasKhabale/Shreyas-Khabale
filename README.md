# Shreyas Bajeerao Khabale

**B.Tech Information Technology Student | Software Developer | AI/ML & Full-Stack Project Builder**

I'm a second-year B.Tech Information Technology student at **MIT Academy of Engineering (MITAOE)**, interested in building practical software products across AI/ML, web development, Android development, and data-driven applications.

I enjoy taking projects from an initial concept through implementation, testing, deployment, and documentation. My work includes decentralized emergency communication, AI-assisted career tools, adaptive user interfaces, and GIS/ML-based analysis platforms.

---

## About Me

- **Name:** Shreyas Bajeerao Khabale
- **Education:** B.Tech in Information Technology, MIT Academy of Engineering (MITAOE)
- **Current academic year:** Second year
- **Primary interests:** Software engineering, artificial intelligence, machine learning, full-stack development, Android development, and problem-solving
- **Working approach:** Practical implementation, iterative testing, preserving working functionality, and clear project documentation

## Technical Skills

| Area | Technologies / Skills |
|---|---|
| Programming | Python, C, C++ |
| Web development | HTML, CSS, JavaScript |
| Backend and APIs | Flask, FastAPI, REST API integration |
| Frontend | React, Next.js |
| Android | Kotlin, Jetpack Compose, Material 3 |
| AI / ML | NLP, scikit-learn, AI-assisted application features |
| Data and productivity | Excel |
| Databases / geospatial | PostgreSQL, Neon, PostGIS (project integration work) |
| Tools and platforms | Git, GitHub, Android Studio, Replit, Google AI Studio, Cloudflare Workers |

*The table reflects technologies used or explored across projects; it does not imply equal depth of experience in every technology.*

---

# Projects

## 1. DisasterMesh — Smart Disaster Communication Network Using Mesh Networking

**Type:** Android application / decentralized emergency communication  
**Platform:** Android  
**Repository:** [GitHub – DisasterMesh](https://github.com/ShreyasKhabale/DisasterMesh)  
**Branch:** `development`  
**Application package:** `com.example.disastermesh`

### Overview

DisasterMesh is designed to support emergency communication when conventional communication infrastructure is unavailable or unreliable. The project focuses on enabling nearby phones to exchange and relay emergency messages through a decentralized network.

The long-term objective is an infrastructure-independent emergency communication system. The current Android implementation uses Google Nearby Connections, with a peer-to-peer cluster strategy, as its communication layer.

### Implemented functionality

- Nearby device discovery and advertising.
- Device-to-device connections using Google Nearby Connections.
- SOS message creation and transmission.
- Automatic SOS forwarding/relay between connected devices.
- Multi-hop message routing with a configured hop limit.
- Duplicate-message suppression using message IDs.
- Message path tracking.
- Acknowledgement-based clearing of pending SOS messages.
- Local pending-message storage and retry support.
- Sender display names and persistent device IDs.
- Notifications for received SOS alerts and ordinary messages.
- Connection states and activity logs.
- Persistent dark/light theme preference and editable display name.

### Architecture and implementation notes

- Kotlin and Jetpack Compose with Material 3.
- Google Nearby Connections using `P2P_CLUSTER`.
- SharedPreferences for local persistence.
- SOS messages use structured JSON envelopes containing fields such as message ID, origin, origin device ID, message, remaining hops, path, and timestamp.
- Duplicate IDs are tracked to prevent repeated forwarding.
- Acknowledgements are used to confirm next-hop delivery before clearing a pending copy.
- Runtime permissions are handled according to Android version, including Bluetooth, nearby Wi-Fi, location on older Android versions, and notifications.

### Testing

The application has been tested across multiple Android phones. Tests reported successful SOS delivery and relay across devices, including a scenario where a phone sent an SOS that was received by multiple connected phones. The latest reported implementation test was working.

### Planned direction

1. Strengthen infrastructure-independent operation.
2. Improve multi-hop routing and scalability.
3. Add emergency-response features such as SOS location sharing, missing-person tracking, and rescue coordination.
4. Add offline map support for Pune and surrounding areas, including Alandi and nearby college areas.

**Important scope note:** The long-term goal is operation without cellular networks, internet, Wi-Fi infrastructure, or Bluetooth. The current working prototype uses Nearby Connections; fully infrastructure-independent operation beyond the current transport capabilities remains a development goal. The project is currently software-focused, with no smartphone modem hardware component in scope.

---

## 2. GreenMap — GIS and ML-Based Renewable Energy Analysis Platform

**Type:** Web application / geospatial data and machine-learning platform  
**Backend:** FastAPI  
**Frontend / runtime:** Web application with a Node.js server/proxy  
**Database direction:** Neon PostgreSQL with PostGIS

### Overview

GreenMap is a geospatial analysis website being developed around renewable-energy assessment. The project includes GIS and machine-learning backend functionality, including wind analysis for selected regions and hub heights.

### Technical work and integration

- Inspected the existing backend and deployment architecture before making changes.
- Worked with a FastAPI backend and Node/Express proxy.
- Investigated API routes for wind analysis, including a route shaped like `/api/v1/wind/analyze` with region and hub-height parameters.
- Worked on Neon PostgreSQL connectivity using `DATABASE_URL`.
- Added or planned PostgreSQL/PostGIS support through `psycopg`.
- Addressed SSL requirements for Neon-hosted PostgreSQL connections.
- Worked to prevent silent SQLite fallback when PostgreSQL/Neon is configured.
- Sanitized connection errors to avoid exposing database credentials.
- Investigated deployment environment configuration and API fetch failures.

### Deployment / configuration notes

A verified deployment blocker was identified: `DATABASE_URL` was not present in the running server environment at the time of inspection. This prevented the configured Neon database connection from working in the deployed environment.

### Current status

The project has an existing FastAPI backend and a web-server proxy architecture. Database deployment and live API connectivity have been active integration/debugging areas. Confirm the latest deployment state before presenting the application as fully operational.

---

## 3. AI Resume Analyzer — Resume Insight AI

**Type:** AI/ML web application  
**Live project:** [Resume Insight AI](https://resume-insight-ai--jarviscyb07.replit.app/)  
**Stack:** React, Flask, Python, NLP, scikit-learn

### Overview

An AI-assisted resume analysis tool that evaluates uploaded resumes and provides structured feedback to help users improve their applications for jobs.

### Features

- ATS-style resume scoring.
- Skill extraction.
- Job-role prediction.
- Keyword analysis.
- Improvement suggestions.
- PDF and DOCX resume upload.

### Team

- Shreyas Khabale
- Kartik Vijay Gawande
- Om Farate

---

## 4. AI Adaptive UI

**Type:** Browser extension / AI-assisted interface adaptation  
**Platforms:** Microsoft Edge and Chromium-based browsers  
**Project version reference:** `AI-Adaptive-UI-Pro-2.3.0`

### Overview

AI Adaptive UI explores how AI can help adapt website interfaces and improve the user's interaction with web content.

### Development work

- Developed an Edge/Chrome extension project.
- Worked on the AI-assisted chat integration.
- Integrated a Cloudflare Worker endpoint using `/api/chat`.
- Used a Worker secret named `Project_KEY` for protected configuration.
- Preserved the existing dark-mode behavior during updates.
- Established `#22D3EE` as the intended website text color in the requested UI styling.
- Worked from the project archive `AI-Adaptive-UI-v2-pro(3).zip`.

### Technical areas

- Browser extension development.
- Frontend UI customization.
- API integration.
- Cloudflare Workers.
- Secret-based configuration.

---

## 5. Techify / Tecthify

**Type:** Web application / technical problem-solving  
**Project:** [Tecthify on Replit](https://replit.com/@jarviscyb07/Tecthify)  
**Technologies:** HTML, CSS, JavaScript; AI/ML-oriented functionality

### Overview

A web-based project intended to help users with technical issues and problem-solving. It combines a web interface with AI/ML-oriented functionality.

---

## Hackathons and Collaborative Work

### Claude FirstHack 2026

- Participated in Claude FirstHack 2026 with a team.
- The team reached **Round 3**.
- Interested in building technically meaningful AI/software products rather than simple AI wrappers.
- Focus areas include practical utility, implementation quality, and working prototypes.

---

# Other Development Experience

Across projects, I have also worked on:

- Building and refining React-based websites and dashboards.
- Designing responsive interfaces and improving visual consistency.
- Exploring component libraries and community UI components, including [21st.dev](https://21st.dev/community/components).
- Connecting frontend applications to backend APIs.
- Debugging deployment and runtime configuration issues.
- Working with GitHub repositories and development branches.
- Preparing project reports, presentations, and technical explanations for academic evaluation.
- Testing Android applications on physical devices.

# GitHub

- **DisasterMesh repository:** [github.com/ShreyasKhabale/DisasterMesh](https://github.com/ShreyasKhabale/DisasterMesh)

Add other repositories here as they become public or ready to showcase.

# Current Focus

My current development interests and project priorities are:

1. **DisasterMesh:** Improve reliable emergency communication, message routing, and offline location support.
2. **GreenMap:** Complete database configuration, GIS/ML API integration, and deployment verification.
3. **AI Adaptive UI:** Continue improving browser-based AI integration and interface adaptation.
4. **AI/ML applications:** Build useful products with measurable functionality and complete workflows.
5. **Software engineering:** Strengthen programming, backend architecture, database design, testing, and deployment skills.

# Professional Interests

I'm interested in opportunities involving:

- Software development and engineering.
- Artificial intelligence and machine learning.
- Full-stack web development.
- Android application development.
- Backend systems and API engineering.
- Geospatial applications and data-driven software.
- Hackathons and collaborative product development.

---

## Contact and Links

- **GitHub:** [ShreyasKhabale](https://github.com/ShreyasKhabale)
- **Resume Insight AI:** [Live application](https://resume-insight-ai--jarviscyb07.replit.app/)
- **Tecthify:** [Replit project](https://replit.com/@jarviscyb07/Tecthify)

*Add your preferred professional email, LinkedIn profile, and portfolio URL here.*

---

## Notes on Accuracy

This README is a consolidated profile based on project details and development work discussed so far. Some projects are prototypes or ongoing builds. Feature descriptions distinguish implemented functionality from planned work where that distinction is known. Update project status, public links, and individual contribution details as the projects evolve.
