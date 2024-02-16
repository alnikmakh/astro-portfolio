import {defineCollection, getCollection, z} from "astro:content";

const postsCollection = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    publishedAt: z.date(),
    description: z.string(),
    isPublish: z.boolean(),
    isDraft: z.boolean().default(false),
  }),
});

export const collections = { posts: postsCollection };

export const getPosts = async () => {
  const posts = [];
  try {
    const postsFromApi = await getCollection("posts");
    posts.push(...postsFromApi);
    return posts.sort(function (first, second) {
      // @ts-ignore
      return second.data.publishedAt.getTime() - first.data.publishedAt.getTime();
    });
  } catch (e) {
    console.error(e);
  }
  return posts;
}
