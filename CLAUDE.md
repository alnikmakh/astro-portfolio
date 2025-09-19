# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- `npm run dev` or `npm start` - Start development server
- `npm run build` - Build the project for production
- `npm run preview` - Preview the production build locally
- `npm run check` - Run Astro type checking

## Architecture Overview

This is an Astro-based portfolio blog with the following key architectural patterns:

### Content Management
- **Content Collections**: Blog posts are managed via Astro's content collections in `src/content/posts/`
- **Content Schema**: Posts must include `title`, `publishedAt`, `description`, `isPublish`, `isDraft`, and `image` fields (defined in `src/content/config.ts:5-12`)
- **MDX Support**: Posts use MDX format with rehype-pretty-code for syntax highlighting and remark-toc for table of contents

### Project Structure
- **Data Layer**: Configuration and content data stored in `src/data/` (config, presentation, projects, theme)
- **Utilities**: Helper functions in `src/utils/` for date formatting, path generation, and variant mapping
- **Components**: Reusable Astro components in `src/components/` with shared components in `src/components/shared/`
- **Layout System**: Single main layout in `src/layouts/Layout.astro` with consistent styling and SEO

### Styling & Design
- **Tailwind CSS**: Primary styling framework with custom configuration in `tailwind.config.cjs`
- **Dark Theme**: Default dark neutral color scheme (neutral-950 background, neutral-300 text)
- **Typography**: Open Sans font family with responsive design patterns
- **Path Aliases**: `@/*` maps to `./src/*` for cleaner imports

### Content Publishing
- **Publication Control**: Posts require `isPublish: true` to appear on the site
- **Sorting**: Posts automatically sorted by `publishedAt` date (newest first)
- **Path Generation**: Custom slug generation via `generatePathFromTitleAndSlug` utility

### Deployment
- **Docker**: Containerized deployment with GitHub Actions workflow
- **CI/CD**: Automatic build and deployment to VPS on main branch pushes
- **Registry**: Uses GitHub Container Registry (ghcr.io)

## Important Notes

- ESLint configuration exists but has known issues (see comment in `.eslintrc.cjs:1`)
- Site URL configured in `src/data/config.ts:1` as "https://regulardev.click/"
- Prettier configured with Tailwind and Astro plugins for consistent formatting