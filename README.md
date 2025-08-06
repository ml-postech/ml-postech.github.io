# ml.postech.ac.kr

The official website for the Machine Learning Lab at POSTECH (Pohang University of Science and Technology).

## 🚀 Quick Start

To get the development server running locally:

```bash
git clone https://github.com/ml-postech/ml-postech.github.io.git
cd ml-postech.github.io
bun install
bun dev
```

The site will be available at `http://localhost:4321`

## 📋 Available Commands

All commands are run from the root of the project:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `bun install`             | Install project dependencies                     |
| `bun dev`                 | Start development server at `localhost:4321`    |
| `bun build`               | Build production site to `./dist/`              |
| `bun preview`             | Preview production build locally                 |
| `bun astro ...`           | Run Astro CLI commands (`add`, `check`, etc.)   |
| `bun astro -- --help`     | Get help using the Astro CLI                    |

## 🛠️ Tech Stack

This website is built with modern web technologies:

### Core Framework

- **[Astro](https://astro.build/)** - Static site generator with component islands architecture
- **[TypeScript](https://www.typescriptlang.org/)** - Type-safe JavaScript development
- **[Bun](https://bun.sh/)** - Fast JavaScript runtime and package manager

### Styling & UI

- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS framework
- **[Motion](https://motion.dev/)** - Animation library for smooth interactions

### Content & SEO

- **[Astro Content Collections](https://docs.astro.build/en/guides/content-collections/)** - Type-safe content management
- **[Astro SEO](https://github.com/jonasmerlin/astro-seo)** - SEO optimization
- **[Citation.js](https://citation.js.org/)** - Academic citation processing with BibTeX support

### Development Tools

- **ESLint & Prettier** - Code linting and formatting

## 📝 Content Management

This website uses Astro's Content Collections for type-safe content management. All content is stored in markdown files with frontmatter metadata.

### 👨‍🏫 Faculty

Faculty member profiles are located in the `faculty/` directory. Each profile is a Markdown file with the following frontmatter structure:

```yaml
email: <email>
image: <image-path>
name: <name>
role: <role>
website: <url>
```

### 🎓 Students

Current student profiles are in the `students/` directory. Each profile follows this frontmatter format:

```yaml
course: <M.S., M.S./Ph.D., or Ph.D.>
email: <email>
enrollment: <YYYY-MM-DD>
image: <image-path>
interest: <interest>
name: <name>
website: <url>
```

### 🎖️ Alumni

Alumni profiles are stored in the `alumni/` directory with the following structure:

```yaml
course: <M.S. or Ph.D.>
email: <email>
graduate: <YYYY-MM-DD>
image: <image-path>
name: <name>
status: <current-job>
```

### 📰 News

News articles are in the `news/` directory. Each article uses this frontmatter:

```yaml
title: <article-title>
date: <YYYY-MM-DD>
```

### 🔬 Research

Research topics are documented in the `research/` directory with the following frontmatter:

```yaml
title: <topic-title>
advisor: <id-of-faculty-member>
mentor: <id-of-student-member>
```

*Note: The `advisor` and `mentor` fields use Astro's [content references](https://docs.astro.build/en/guides/content-collections/#accessing-referenced-data) for type-safe relationships.*

### 📚 Publications

Academic publications are managed through a BibTeX file located at `publications/publications.bib`. All publication entries should follow standard BibTeX formatting and will be automatically processed using Citation.js.

## 📁 Project Structure

```text
├── src/
│   ├── components/     # Reusable UI components
│   ├── layouts/        # Page layout templates
│   ├── pages/          # Route pages
│   ├── styles/         # Global styles
│   └── content.config.ts # Content collection configuration
├── alumni/             # Alumni profiles (markdown)
├── faculty/            # Faculty profiles (markdown)
├── students/           # Student profiles (markdown)
├── news/               # News articles (markdown)
├── research/           # Research topics (markdown)
├── publications/       # Academic publications (BibTeX)
└── public/             # Static assets
```

## 📄 License

This project is maintained by the POSTECH Machine Learning Lab. Please contact the lab for usage permissions and guidelines.
