# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a static HTML portfolio website for Matthew Frank, hosted on GitHub Pages at https://maafrank.github.io/. The site showcases skills, projects, and academic background in Machine Learning and Data Science.

## Architecture

**Static Site Structure:**
- `index.html` - Main single-page application with all sections
- `assets/` - All static resources organized by type:
  - `css/` - Stylesheets including Bootstrap, animations, and custom styles
  - `js/` - JavaScript libraries (jQuery, Bootstrap, Owl Carousel, custom scripts)
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

- `index.html` - All content sections, structure, and HTML
- `assets/css/style.css` - Primary custom styles
- `assets/js/custom.js` - Custom JavaScript functionality
- `assets/download/MatthewFrankResume.pdf` - Resume file for download
- `assets/images/` - Update portfolio images, profile photos, project screenshots

## Content Sections (in index.html)

The single-page site includes these main sections:
1. Home/Banner - Introduction and navigation
2. About Me - Background and professional summary  
3. Education - Academic timeline
4. Skills - Technical skills with progress bars
5. Experience - Professional work history
6. Projects - Portfolio showcase with image carousel
7. Contact - Contact form and information

## GitHub Pages Deployment

- Site automatically deploys from the main branch
- Accessible at https://maafrank.github.io/
- No custom Jekyll or build configuration needed
