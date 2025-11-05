# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a static HTML portfolio website for Matthew Frank, hosted on GitHub Pages at https://maafrank.github.io/. The site showcases skills, projects, and academic background in Machine Learning and Data Science.

## Architecture

**Static Site Structure:**
- `index.html` - Main single-page application with all core sections (about, education, skills, experience, projects, contact)
- Secondary pages linked from main navigation:
  - `games.html` - Interactive browser games (Snake, Tetris, Space Shooter, Pong, etc.) in `games/` subdirectory
  - `ml-academy.html` - Educational courses hub linking to three course tracks in `lessons/` subdirectory:
    - `fundamentals-course.html` - ML fundamentals lessons
    - `tensorflow-course.html` - TensorFlow/MNIST lessons
    - `quant-course.html` - Quantitative trading lessons
  - `webapps.html` - AI-powered web apps using WebLLM (ChatBot, CodeReviewer, CourseCreator, StockAnalyzer, AIPlayground) in `webapps/` subdirectory
  - `hobbies.html` - Personal interests and photography
- `assets/` - All static resources organized by type:
  - `css/` - Stylesheets including Bootstrap, animations, custom styles, and common styles for games/lessons
  - `js/` - JavaScript libraries (jQuery, Bootstrap, Owl Carousel, custom scripts, lesson-complete.js)
  - `images/` - Portfolio images, banners, client logos organized in subdirectories
  - `fonts/` - Font files for various icon sets and typography
  - `download/` - Downloadable resume PDF
  - `logo/` - Site favicon and branding

**Technology Stack:**
- Pure HTML5/CSS3/JavaScript (no build system or framework)
- Bootstrap for responsive grid and components
- jQuery for DOM manipulation and interactions
- Owl Carousel for image sliders
- Font Awesome and Flaticon for icons
- Custom CSS animations and styling
- WebLLM (via @mlc-ai/web-llm) for browser-based AI chat widget on main page and AI web apps

## Development Commands

Since this is a static site with no build system, development is straightforward:

**Local Development:**
```bash
# Serve locally (Python 3)
python -m http.server 8000

# Or with Python 2
python -m SimpleHTTPServer 8000

# Or with Node.js http-server (if installed)
npx http-server -p 8000
```

**Deployment:**
- Changes are deployed automatically via GitHub Pages when pushed to the main branch
- No build step required - files are served directly

## Key Files for Modifications

- `index.html` - Main portfolio page with all content sections and embedded WebLLM chat widget
- `assets/css/style.css` - Primary custom styles
- `assets/css/game-common.css` - Shared styles for all game pages
- `assets/css/lesson-common.css` - Shared styles for all lesson pages
- `assets/js/custom.js` - Custom JavaScript functionality
- `assets/js/lesson-complete.js` - Lesson progress tracking functionality
- `assets/download/MatthewFrankResume.pdf` - Resume file for download
- `assets/images/` - Update portfolio images, profile photos, project screenshots

## Content Sections (in index.html)

The main portfolio page includes these sections:
1. Home/Banner - Introduction and navigation
2. About Me - Background and professional summary
3. Education - Academic timeline (three horizontal timeline cards)
4. Skills - Technical skills with animated progress bars
5. Experience - Professional work history (vertical timeline)
6. Projects - Portfolio showcase with 8 project cards arranged in two rows:
   - Row 1: AI/ML Academy, Interactive Games, AI Web Apps, Hobbies (4 cards)
   - Row 2: InfraSketch, PitCrew, NetSmith, Medium Article (4 cards)
7. Contact - Contact form and information
8. Chat Widget - Fixed bottom-right chat button that opens WebLLM-powered AI assistant (inline ES6 module at end of index.html)

## Multi-Page Structure

**Games Section:**
- Each game is a standalone HTML file in `games/` with embedded JavaScript
- Games use HTML5 Canvas for rendering
- Common styling via `assets/css/game-common.css`

**ML Academy Section:**
- Three course tracks, each with multiple lesson pages
- Lessons are in subdirectories: `lessons/fundamentals/`, `lessons/tensorflow-mnist/`, `lessons/quant-trading/`
- Common styling via `assets/css/lesson-common.css`
- Progress tracking using `assets/js/lesson-complete.js` with localStorage

**Web Apps Section:**
- Each app in `webapps/[AppName]/index.html`
- All apps use WebLLM for browser-based AI inference
- AI Playground includes CNN Trainer with MNIST data loaded from large JS files

## GitHub Pages Deployment

- Site automatically deploys from the main branch
- Accessible at https://maafrank.github.io/
- No custom Jekyll or build configuration needed

## Important Instructions

**When Adding New Content:**
- ALWAYS prefer editing an existing file to creating a new one
- NEVER proactively create documentation files (*.md) or README files unless explicitly requested
- Only use emojis if the user explicitly requests it
- When adding projects to the Projects section in index.html, maintain the two-row grid structure with proper Bootstrap column classes (`col-sm-3` for 4 columns per row)
- The last card in each row should have the `profile-no-border` class