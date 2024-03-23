import { defineCollection, z } from "astro:content";

const postsCollection = defineCollection({
  type: "content",
  schema: ({image}) => z.object({
    title: z.string(),
    publishedAt: z.date(),
    description: z.string(),
    isPublish: z.boolean(),
    isDraft: z.boolean().default(false),
    image: z.object({source: image(), description: z.string(), link: z.string().optional()}),
  }),
});

export const collections = { posts: postsCollection };
