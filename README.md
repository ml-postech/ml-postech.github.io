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

### 👥 People

All people profiles (advisors, students, alumni, and officers) are stored in the `people/` directory at the project root. Files are named with prefixes to indicate their role:

**Advisors** (`advisor-*.md`):

```yaml
name: <name>
role: <role>
email: <email>
webpage: <url>
image: <image-path>
```

**Students** (`student-*.md`):

```yaml
name: <name>
role: <role>
email: <email>
webpage: <url>
enrollment_year: <YYYY>
areas_of_interest: [<interest1>, <interest2>, ...]
image: <image-path>
```

**Alumni** (`alumni-*.md`):

```yaml
name: <name>
role: <role>
email: <email>
webpage: <url>
graduation_year: <YYYY>
current_position: <current-job>
image: <image-path>
```

**Officers** (`officer-*.md`):

```yaml
name: <name>
role: <role>
email: <email>
webpage: <url>
image: <image-path>
```

### 📰 News

News articles are in the `news/` directory at the project root. Each article uses this frontmatter:

```yaml
title: <article-title>
date: <YYYY-MM-DD>
```

### 🔬 Research

Research topics are documented in the `research/` directory at the project root with the following frontmatter:

```yaml
title: <topic-title>
advisor: <id-of-advisor>
mentor: <id-of-student> # optional
```

*Note: The `advisor` and `mentor` fields use Astro's [content references](https://docs.astro.build/en/guides/content-collections/#accessing-referenced-data) for type-safe relationships. The `advisor` field references the `advisors` collection, and the optional `mentor` field references the `students` collection.*

### 📚 Publications

Academic publications are managed through a YAML file located at `publications.yaml` at the project root. Each publication entry includes:

```yaml
- bibtex: |
    @inproceedings{authorYYYYkeyword,
        author = "Last, First and ...",
        title = "Publication Title",
        booktitle = "Conference/Journal Name",
        year = "YYYY",
        url = "https://..."  # optional
    }
  category: <category-name>  # e.g., theory, graph, science, acceleration, language, vision
  id: authorYYYYkeyword
  url: https://...  # optional, for direct linking
```

**Categories**: Publications are organized into categories such as `theory`, `graph`, `science`, `acceleration`, `language`, and `vision` for filtering and organization.

**Source BibTeX**: The original BibTeX file is maintained at `publications/publications.bib` for reference and import purposes.

## 📁 Project Structure

```text
├── src/
│   ├── assets/         # Images and other assets
│   ├── components/     # Reusable UI components
│   ├── layouts/        # Page layout templates
│   ├── pages/          # Route pages
│   ├── styles/         # Global styles
│   └── content.config.ts # Content collection configuration
├── people/             # People profiles (advisors, students, alumni, officers)
├── news/               # News articles (markdown)
├── research/           # Research topics (markdown)
├── publications.yaml   # Publications data (YAML format with categories)
└── public/             # Static assets
```

## 📄 License

This project is maintained by the POSTECH Machine Learning Lab. Please contact the lab for usage permissions and guidelines.
