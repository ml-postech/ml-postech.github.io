import { defineCollection, reference, z } from "astro:content";
import { file, glob } from "astro/loaders";
import { Cite } from "@citation-js/core";
import "@citation-js/plugin-bibtex";

const news = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./news",
  }),
  schema: z.object({
    title: z.string(),
    date: z.date(),
  }),
});

const publications = defineCollection({
  loader: file("publications/publications.bib", {
    parser: (fileContent) => {
      const cite = new Cite(fileContent);
      return cite.get();
    },
  }),
});

const research = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./research",
  }),
  schema: z.object({
    title: z.string(),
    advisor: reference("advisors"),
    mentor: reference("students").optional(),
  }),
});

const advisors = defineCollection({
  loader: glob({
    pattern: "**/advisor-*.md",
    base: "./people",
  }),
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      role: z.string(),
      email: z.string().email(),
      webpage: z.string().url().optional(),
      image: image(),
    }),
});

const students = defineCollection({
  loader: glob({
    pattern: "**/student-*.md",
    base: "./people",
  }),
  schema: ({ image }) =>
    z
      .object({
        name: z.string(),
        role: z.string(),
        email: z.string().email(),
        webpage: z.string().url().optional(),
        enrollment_year: z.number(),
        areas_of_interest: z.array(z.string()).optional(),
        image: image(),
      })
      .transform(({ enrollment_year, areas_of_interest, ...data }) => ({
        ...data,
        enrollmentYear: enrollment_year,
        areasOfInterest: areas_of_interest,
      })),
});

const alumnis = defineCollection({
  loader: glob({
    pattern: "**/alumni-*.md",
    base: "./people",
  }),
  schema: ({ image }) =>
    z
      .object({
        name: z.string(),
        role: z.string(),
        email: z.string().email(),
        webpage: z.string().url().optional(),
        graduation_year: z.number(),
        current_position: z.string().optional(),
        image: image(),
      })
      .transform(({ graduation_year, current_position, ...data }) => ({
        ...data,
        graduationYear: graduation_year,
        currentPosition: current_position,
      })),
});

const officers = defineCollection({
  loader: glob({
    pattern: "**/officer-*.md",
    base: "./people",
  }),
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      role: z.string(),
      email: z.string().email(),
      webpage: z.string().url().optional(),
      image: image(),
    }),
});

export const collections = {
  news,
  publications,
  research,
  advisors,
  students,
  alumnis,
  officers,
};
