import { defineCollection, z } from "astro:content";

import { glob } from "astro/loaders";

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

const alumni = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./alumni",
  }),
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      course: z.string(),
      email: z.string().email(),
      image: image(),
      graduate: z.date(),
      interest: z.string().optional(),
      website: z.string().url().optional(),
      status: z.string().optional(),
    }),
});

const faculty = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./faculty",
  }),
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      role: z.string(),
      email: z.string().email(),
      website: z.string().url().optional(),
      image: image(),
    }),
});

const staff = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./staff",
  }),
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      role: z.string(),
      email: z.string().email(),
      website: z.string().url().optional(),
      image: image(),
    }),
});

const students = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./students",
  }),
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      course: z.string(),
      email: z.string().email(),
      image: image(),
      enrollment: z.date(),
      interest: z.string().optional(),
      website: z.string().url().optional(),
    }),
});

export const collections = {
  news,
  alumni,
  faculty,
  staff,
  students,
};
